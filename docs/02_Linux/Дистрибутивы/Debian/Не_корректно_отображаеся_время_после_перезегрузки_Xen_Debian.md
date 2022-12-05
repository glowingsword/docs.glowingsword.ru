---
title: 'Не корректно отображаеся время после перезегрузки Xen Debian'
authors: 
 - glowingsword
tags:
 - Debian
 - 'Настройка времени'
date: 2020-04-04
---
# Не корректно отображаеся время после перезегрузки Xen Debian

Для решения данной проблемы необходимо заменить строку

``` ini
UTC=no
```

в файле /etc/default/rcS

на

``` ini
UTC=yes
```

после чего выполнить следующие команды

``` bash
apt-get install ntp ntpdate
ntpdate -bs pool.ntp.org
dpkg-reconfigure tzdata
```