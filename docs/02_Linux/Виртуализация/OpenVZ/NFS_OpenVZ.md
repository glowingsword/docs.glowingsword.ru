---
title: 'Отключаем поддержку NFS на уровне ядра у контейнера OpenVZ'
authors: 
 - glowingsword
tags:
 - OpenVZ
 - NFS
date: 2020-04-05
---
# Отключаем поддержку NFS на уровне ядра у контейнера OpenVZ

Убеждаемся что поддержка включена командой
``` bash
grep nfs /etc/vz/conf/100500.conf FEATURES="<nfs:on>"
```
После чего отключаем её командой
``` bash
vzctl set 100500 --features "<nfs:off>" --save
```
и применяем изменения, перезапуская контейнер
``` bash
vzctl restart 100500
```
Где 100500 - container id.
