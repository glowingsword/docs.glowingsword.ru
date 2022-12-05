---
title: 
authors: Удаление бэкапов Plesk на VPS
 - glowingsword
tags:
 - Plesk
date: 2020-04-04
---
# Удаление бэкапов Plesk на VPS

Останавливаеем httpd и psa

``` bash
service httpd stop
service psa stop
```
после чего удаляем с помощью команды

``` bash
rm -f /var/lib/psa/dumps/domains/projektdoma.com/*_user-data_*.tgz
```
файлы резервных копий, занимающий больше всего дискового пространства и
запускаем панель управления командой

``` bash
service psa start
```