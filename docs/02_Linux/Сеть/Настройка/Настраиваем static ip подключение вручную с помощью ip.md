---
title: 'Настраиваем static ip подключение вручную с помощью ip'
authors: 
 - glowingsword
tags:
 - Сеть
date: 2021-08-13
---

# Настраиваем static ip подключение вручную с помощью ip

Смотрим какие на тачке есть интерфейсы

```
ip link
```
Поднимаем нужный интерфейс

```bash
ip link set eth0 up
```

Добавляем Static IP на него и broadcast

```bash
ip addr add 192.68.104.123/24 broadcast 192.68.104.255 dev eth0
```
где в нашем случае Static IP, назначаемый интерфейсу — 192.68.104.123, а Broadcast IP нужной сетки — 192.68.104.255.

Добавляем дефолтный маршрут

```bash
ip route add default via 192.68.104.1  dev eth0
```

Если /etc/resolv.conf на сервере пустой, или в нём указан не верный адрес DNS, выполняем 

```bash
echo "nameserver 8.8.8.8" > /etc/resolv.conf 
```

Если где-то ошиблись, делаем 

```bash
ip addr flush dev eth0
```
и

```bash
ip route flush dev eth0
```

После чего повторяем. 

Подробности
https://www.linuxsecrets.com/2898-manually-setup-archlinux-networking
https://bytefreaks.net/gnulinux/how-to-set-a-static-ip-address-from-the-command-line-in-gnulinux-using-ip-addr-and-ip-route

