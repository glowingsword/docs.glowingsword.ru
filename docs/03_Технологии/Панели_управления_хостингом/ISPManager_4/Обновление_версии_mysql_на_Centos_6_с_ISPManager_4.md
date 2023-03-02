---
title: 'Обновление версии mysql на Centos 6 с ISPManager 4'
authors: 
 - glowingsword
tags:
 - 'ISPManager 4'
 - 'MySQL'
date: 2020-04-05
---
# Обновление версии mysql на Centos 6 с ISPManager 4

Обновляемся mysql из репозитория atomic
``` bash
yum remove mysql-* 
yum --enablerepo=atomic info mysql-server 
yum --enablerepo=atomic install mysql-server mysql-devel
```
Смотрим обновились ли все нужные нам пакеты
``` bash
rpm -qa | grep mysql
```
Обновляем системные таблицы базы данных mysql
``` bash
mysql_upgrade -u root -p
```
и перезапускаем mysqld
``` bash
/etc/init.d/mysqld restart
```
Устанавливаем и включаем smtp и exim, если ранее они были выключены
``` bash
/usr/local/ispmgr/sbin/pkgctl install smtp exim4
```
``` bash
/usr/local/ispmgr/sbin/pkgctl activate smtp exim4
```
формируем заново кэш установленных ранее приложений, что-бы mysql был отмечен как активный в разделе "Возможности"
``` bash
/usr/local/ispmgr/sbin/pkgctl -D cache
```
и перезапускаем панельку
``` bash
killall -9 -r ispmgr
```