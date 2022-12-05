---
title:  Обновляем информацию о часовых поясах в Ubuntu
authors: 
 - glowingsword
tags:
 - Ubuntu
 - Настройка Ubuntu
 - Проблемы на Ubuntu Linux
date: 2020-04-19
---
# Не поднимается сетевое подключение на Ubuntu 16.04 из-за ошибки iptables-restore: not found

Причину, из-за которой в процессе запуска службы networking возникает ошибка нужно искать в journalctl и syslog(реже в dmesg). 

В нашем случае проблема возникает из-за ошибки вида
``` bash
Aug 11 10:43:22 localhost systemd\[1\]: Found device
/sys/subsystem/net/devices/venet0. Aug 11 10:43:22 localhost
systemd-tmpfiles\[178\]: \[/usr/lib/tmpfiles.d/var.conf:14\] Duplicate
line for path "/var/log", ignoring. Aug 11 10:43:22 localhost sh\[177\]:
/etc/network/if-pre-up.d/iptables: 2: /etc/network/if-pre-up.d/iptables:
iptables-restore: not found Aug 11 10:43:22 localhost sh\[177\]:
run-parts: /etc/network/if-pre-up.d/iptables exited with return code 127
Aug 11 10:43:22 localhost sh\[177\]: Failed to bring up venet0.
```
Смотрим содержимое `/etc/network/if-pre-up.d/iptables` и видим там:

``` bash
!/bin/sh
iptables-restore < /etc/iptables.conf
```
Проверяем, доступна ли на сервере команда `iptables-restore`, выполняем вручную в консоли

``` bash
/etc/network/if-pre-up.d/iptables
```
Видим в выхлопе

``` bash
/etc/network/if-pre-up.d/iptables: 2: /etc/network/if-pre-up.d/iptables:
iptables-restore: not found
```
Если данная команда не доступна, устанавливаем пакет `iptables`. Для этого
временно заменяем содержимое файла `/etc/network/if-pre-up.d/iptables` на
содержимое вида:

``` bash
!/bin/sh

exit 0
```

после чего перезапускаем службу networking командой:
``` bash
/etc/init.d/networking restart
```
и устанавливаем iptables командой
``` bash
apt-get install iptables
```
После того, как `iptables` будет установлен, восстанавливаем содержимое
файла `/etc/network/if-pre-up.d/iptables` и повторно перезапускаем службу
`networking`.
