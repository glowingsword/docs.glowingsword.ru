---
title: 'Запуск ihttpd на сервере с ISPmanager 5'
authors:
 - glowingsword
tags:
 - ISPManager
 - ISPManager 5
date: 2020-04-04
---
# Запуск ihttpd на сервере с ISPmanager 5

## На шареде

sudo /usr/local/bin/killisp

## на VPS-ках

Если ihttpd не запускается, или запускается и сразу падает, ищем
зависшие процессы и завершаем их с помощью killall -9. После чего
выполняем

service ihttpd start

Если это не решает проблему, а в логах мелькает что-то вроде

Jul 1 09:47:16 \[13276:1\] log INFO Init logs for 'ihttpd' defaults is:
level 5 color is on Jul 1 09:47:16 \[13276:1\] main INFO Adding binding.
IP:'0.0.0.0', port: 1500, cert key: '', cert path: '', ca cert path: '',
cgi path: 'cgi', fd: -1 Jul 1 09:47:16 \[13276:1\] main WARNING Failed
to listen: ip '0.0.0.0', port '1500'. Reason: bind

открываем /usr/local/mgr5/etc/ihttpd.conf и указываем корректные
настройки(ip-адрес и порт).
