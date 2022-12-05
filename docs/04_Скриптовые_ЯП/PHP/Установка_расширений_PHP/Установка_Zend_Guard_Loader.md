---
title: 'Установка Zend Guard Loader'
authors: 
 - glowingsword
tags:
 - PHP
 - 'Установка расширений PHP'
 - 'Zend Guard Loader'
date: 2020-04-05
---
# Установка Zend Guard Loader

На Debian/Ubuntu:
``` bash
wget http://downloads.zend.com/guard/6.0.0/ZendGuardLoader-70429-PHP-5.4-linux-glibc23-x86_64.tar.gz
``` 

Для 5.6 на Centos 6 
``` bash
wget https://downloads.zend.com/guard/7.0.0/zend-loader-php5.6-linux-x86_64_update1.tar.gz
```

Распаковываем
``` bash
tar -vzxf ZendGuardLoader-70429-PHP-5.4-linux-glibc23-x86_64.tar.gz
```

``` bash
cp ZendGuardLoader-70429-PHP-5.4-linux-glibc23-x86_64/php-5.4.x/ZendGuardLoader.so /usr/lib/php5/20100525 
```
``` bash
cd /etc/php5/cli/conf.d
```
``` bash
echo 'zend_extension=ZendGuardLoader.so' > zend_loader.ini
```

<https://serverpilot.io/docs/how-to-install-zend-guard-loader/>