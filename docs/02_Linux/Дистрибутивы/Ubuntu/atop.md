---
title:  Установка atop на Ubuntu и Debian
authors: 
 - glowingsword
tags:
 - Ubuntu
 - Настройка Ubuntu
 - atop
 - мониторинг системных  показателей
date: 2020-04-04
---

# Установка atop на Ubuntu и Debian

## Установка на версии без systemd

``` bash
apt-get install atop
vim /etc/init.d/atop
update-rc.d  atop enable defaults
service atop restart
```
Однострочник для быстрой установки

``` bash
apt-get install -y atop; sed -i 's/-a -w /var/log/atop.log 600/-a -w /var/log/atop.log 10/g' /etc/init.d/atop;sed -i 's/INTERVAL=600/INTERVAL=10/g' /etc/default/atop; update-rc.d atop enable defaults; service atop restart
```

## Установка на Ubuntu с systemd

``` bash
apt-get install -y atop
sed -i 's/INTERVAL=600/INTERVAL=10/g' /etc/default/atop
systemctl daemon-reload
systemctl enable atop
systemctl start atop
```

Однострочник для быстрой установки

``` bash
apt-get install -y atop; sed -i 's/INTERVAL=600/INTERVAL=10/g' /etc/default/atop;systemctl daemon-reload; systemctl enable atop;systemctl start atop
```