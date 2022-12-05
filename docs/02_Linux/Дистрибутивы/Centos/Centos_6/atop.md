---
title: Установка atop на Centos 6
authors: 
 - glowingsword
tags:
 - Centos 6
 - atop
date: 2020-04-04
---
# Установка atop на Centos 6

Ставим atop 

``` bash
yum install atop
```
Если нужен другой интервал обновления информации в логах(600 секунд, это 10 минут, что многовато для многих случаев)
``` bash
sed -i 's/INTERVAL=600/INTERVAL=10/g'  /etc/sysconfig/atop
```
Включаем сервис в автозагрузку
``` bash
chkconfig --level 12345 atop on
```

Запускаем сервис
``` bash
service atop start
```

## Однострочник

``` bash
yum -y install atop;sed -i 's/INTERVAL=600/INTERVAL=10/g'  /etc/sysconfig/atop; chkconfig --level 12345 atop on; service atop start
```