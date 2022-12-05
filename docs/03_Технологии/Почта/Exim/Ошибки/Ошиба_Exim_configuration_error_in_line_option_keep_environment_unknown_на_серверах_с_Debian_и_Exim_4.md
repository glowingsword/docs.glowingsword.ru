---
title: "Ошиба 'Exim configuration error in line option keep environment unknown' на серверах с Debian и Exim 4"
authors: 
 - glowingsword
tags:
 - Exim
 - Ошибки Exim
 - Debian
date: 2020-04-04
---
# Ошиба 'Exim configuration error in line option keep environment unknown' на серверах с Debian и Exim 4

Нужно в /etc/exim4/update-exim4.conf.conf заменить сроку вида
```
dc_use_split_config='false'
```
на строку
```
dc_use_split_config='true'
```
После чего пересоздать конфиг и перезапустить exim4
```
update-exim4.conf
```
и
```
service exim4 reload
```
или
```
service exim4 restart
```
* [http://forum.ispsystem.ru/archive/index.php/t-30415.html](http://forum.ispsystem.ru/archive/index.php/t-30415.html)
* [http://tovld.com/archives/2775](http://tovld.com/archives/2775)
