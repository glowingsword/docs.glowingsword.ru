---
title: 'Установка memcache на не дефолную версию php на VPS'
authors: 
 - glowingsword
tags:
 - PHP
 - 'Установка расширений PHP'
 - Memcache
date: 2020-04-05
---
# Установка memcache на не дефолную версию php на VPS
``` bash
cd /root
```
``` bash
pecl channel-update pecl.php.net 
```
``` bash
pecl download memcache
```
``` bash 
tar xf memcache-*.tgz
```
``` bash 
cd memcache-*
```
``` bash 
/opt/php56/bin/phpize
```
``` bash 
./configure --with-php-config=/opt/php56/bin/php-config
```
``` bash
make 
```
``` bash
make install 
```
``` bash
echo "extension=memcache.so" > /opt/php56/etc/php.d/memcache.ini
```
``` bash
/opt/php56/bin/php -m | grep memcache
```