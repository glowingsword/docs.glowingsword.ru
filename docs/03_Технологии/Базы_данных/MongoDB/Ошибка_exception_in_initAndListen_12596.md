---
title: 'Ошибка exception in initAndListen: 12596 old lock file, terminating при запуске MongoDB'
authors: 
 - glowingsword
tags:
 - Базы данных
 - MongoDB
 - Ошибки MongoDB
date: 2020-04-05
---
# Ошибка exception in initAndListen: 12596 old lock file, terminating при запуске MongoDB
## Суть проблемы
Ошибка вида
```
2016-04-24T14:58:05.235+0400 [initandlisten] exception in initAndListen: 12596 old lock file, terminating
```
лечится с помощью удаления файла mongod.lock, так как возникает из-за наличия старого, не удалённого ранее файла mongod.lock.

## Фикс на Debian
``` bash
rm -I /var/lib/mongodb/mongod.lock
```
## Фикс на Centos
``` bash
rm -I /var/lib/mongo/mongod.lock
```