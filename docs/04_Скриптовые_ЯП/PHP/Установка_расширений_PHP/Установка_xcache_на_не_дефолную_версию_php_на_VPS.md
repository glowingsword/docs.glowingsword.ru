---
title: 'Установка xcache на не дефолную версию php на VPS'
authors: 
 - glowingsword
tags:
 - Linux
 - PHP
 - 'Установка расширений PHP'
date: 2020-04-19
---
# Установка xcache на не дефолную версию php на VPS

Делаем
``` bash
yum install
``` 
``` bash
autoconf
```
``` bash
make gcc
```
``` bash
wget http://xcache.lighttpd.net/pub/Releases/3.2.0/xcache-3.2.0.tar.bz2
```
``` bash
tar xjf xcache-3.2.0.tar.bz2
```
``` bash
rm -rf xcache-3.2.0.tar.bz2
```
``` bash
cd xcache-3.2.0 
```
``` bash
/opt/php53/bin/phpize --clean
```
``` bash
/opt/php53/bin/phpize
```
``` bash 
./configure --enable-xcache --with-php-config=/opt/php56/bin/php-config
```
``` bash
make
```
``` bash
make install
```
``` bash
cat xcache.ini > /opt/php56/etc/php.d/xcache.ini
```
``` bash
/opt/php56/bin/php -i | grep xcache
```
<http://alexxkn.ru/node/6>
