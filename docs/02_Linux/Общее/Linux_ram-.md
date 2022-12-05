---
title: 'Описание процесса комирования корневого раздела Linux в ram-диск'
authors: 
 - glowingsword
tags:
 - Linux
date: 2020-04-19
---
# Описание процесса комирования корневого раздела Linux в ram-диск

Выполняем команды вида
``` bash
mkdir /ramroot
```
``` bash 
mount -n -t tmpfs -o size=2G none /ramroot 
```
``` bash
cd /
```
``` bash
find / -depth -xdev -print | cpio -pd --quiet /ramroot 
```
cd /ramroot
```
``` bash 
mkdir oldroot
```
``` bash
mount --make-private /
``` bash 
mount --make-private /proc/
```
``` bash 
pivot_root . oldroot
```
``` bash 
for i in dev run sys proc; do mount --move $i /ramboot/$i ; done
```
полезные ссылки

<http://unix.stackexchange.com/questions/226872/how-to-shrink-root-filesystem-without-booting-a-livecd>
<https://habrahabr.ru/company/ruvds/blog/308348/>