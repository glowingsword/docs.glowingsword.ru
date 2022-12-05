---
title: 'Не запускаются сервисы на Debian 7 Wheezy в OpenVZ-котейнере'
authors: 
 - glowingsword
tags:
 - Debian
 - init
date: 2020-04-05
---
# Не запускаются сервисы на Debian 7 Wheezy в OpenVZ-котейнере

## Что делать, когда при попытке войти в контейнер даже не доступна консоль

Если при попытке залогиниться в контейнер мы делаем
```bash
vzctl enter $CTID
```
где в $CTID указан числовой CTID нашего контейнера, к примеру 1010, мы видим что-то сообщение об ошибке вида

```bash
enter into CT 1010 failed
Unable to open pty: No such file or directory
```

Выполняем

```bash
vzctl exec $CTID "cd /dev; /sbin/MAKEDEV pty"
```
```bash
vzctl exec $CTID "cd /dev; /sbin/MAKEDEV tty"
```
```bash
vzctl exec $CTID "cd /dev; /sbin/MAKEDEV pts"
```
после чего опять пробуем войти в консоль контейнера командой

```bash
vzctl enter $CTID
```

на этот раз vzctl enter должен отработь корректно.

## Поиск причины возникновения проблемы

Если на Debian 7 Wheezy после dist-upgrade перестали запускаться сервисы,  хотя сам контейнер вроде стартует, проверяем что показывает команда

```bash
sudo dpkg -l|grep sysvinit
```
если результат команды выглядит примерно так(два пакета, присутствует sysvinit, не только sysvinit-utils)

```bash
ii  sysvinit                        2.88dsf-41+deb7u1                  amd64        System-V-like init utilities
ii  sysvinit-utils                  2.88dsf-41+deb7u1                  amd64        System-V-like utilities
```

а не так

```
ii  sysvinit-utils                  2.88dsf-41+deb7u1                  amd64        System-V-like utilities
```

стоит глянуть на результат выполнения

```bash
init --version
```
Если вместо

```
init --version
init (upstart 1.6.1)
Copyright (C) 2012 Scott James Remnant, Canonical Ltd.

This is free software; see the source for copying conditions.  There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

будет видно что-то другое – можете себя поздравить, вы только что обнаружили источник данной проблемы. 

Debian 7 на OpenVZ корректно запускается только с upstart, он не запускается нормально в контейнере с sysvinit. 
Подробно данная проблема описана на (странице)[https://bugs.openvz.org/browse/OVZ-5739]

## Решение проблемы
### Качаем пакет с upstart с архивного репозитория Debian 7 Wheezy
#### Внутри котейнера
Если сеть в контейнере вы уже подняли вручную командой

```bash
service networking start
```

или с помощью утилит ip/ifconfig/route, вам будет проще решить данную проблему. Хуже, когда сеть не заводится.

Для начала качаем куда-то, к примеру в /root/ файл [upstart_1.6.1-1_amd64.deb](http://archive.debian.org/debian/pool/main/u/upstart/upstart_1.6.1-1_amd64.deb).

!!! info "Внимание"
    Если у вашего контейнера другая архитектура, идём на [страницу](http://archive.debian.org/debian/pool/main/u/upstart/] и ищем ссылку на пакет нужной вам архитектуры).

Делаем это так

```bash
cd /root/
```
```bash
wget http://archive.debian.org/debian/pool/main/u/upstart/upstart_1.6.1-1_amd64.deb
```

#### С хост-ноды с копированием в каталог /root/ контейнера
Eсли не смогли вручую запустить сеть на самом конейнере, но у вас есть доступ к хост-ноде OpenVZ, на которой расположен контейнер, качаем пакет на хост-ноду

```bash
cd /tmp/
```
```bash
wget http://archive.debian.org/debian/pool/main/u/upstart/upstart_1.6.1-1_amd64.deb
```
и копируем куда-то в /root/ каталог контейнера
```bash
cp upstart_1.6.1-1_amd64.deb /vz/root/${CTID}/root/
```

где вместо ${CTID} указываем Container ID(CTID) вашего котейнера.

После чего заходим(переходим, если консоль котейнера у вас уже открыта в другом тайле/вкладке), с хост-ноды делаем это командой вида

```bash
vzctl enter ${CTID}
```
### Удаляем sysvinit

Выполняем

```bash
sudo apt-get remove sysvinit
```

### Ставим upstart

```bash
cd /root
```
```bash
sudo dpkg -i upstart_1.6.1-1_amd64.deb
```
и проверяем с помощью 

```bash
init --version
```
что у нас в /sbin/init точно upstart.

## Защищаем себя от подобных казусов в будущем

Открываем файл /etc/apt/preferences в своём любимом текстовом редакторе(у нубов это обычно nano, у всех остальных – vim/emacs)

```bash
sudo nano /etc/apt/preferences
```
где вместо nano ваш любимый редактор.

Добавляем в файл

```yaml
Package: sysvinit
Pin: release c=main
Pin-Priority: -1
```
и сохраняем изменения.

После чего выходим из редактора, и отправляем контейнер в ребут. Котейнер должен подняться успешно, сервисы будут запущены так, как ожидалось.







