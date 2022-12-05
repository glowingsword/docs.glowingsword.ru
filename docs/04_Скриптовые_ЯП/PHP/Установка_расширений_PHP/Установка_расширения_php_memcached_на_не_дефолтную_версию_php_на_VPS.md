---
title: 'Установка расширения php memcached на не дефолтную версию php на VPS'
authors: 
 - glowingsword
tags:
 - PHP
 - Установка расширения PHP
 - PHP extension
date: 2020-06-14
todo: 'Доработать статью'
---

# Установка расширения php memcached на не дефолтную версию php на VPS
## Собираем и ставим ручками libmamcached
Ставим необходимые зависимости

```bash
yum install cyrus-sasl-devel zlib-devel gcc-c++ 
```
```bash
wget https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz
```
```bash
tar -xvf libmemcached-1.0.18.tar.gz
```
```bash
cd libmemcached-1.0.18
```
```bash
./configure --disable-memcached-sasl
```
```bash
make
```
```bash
make install
```

## Собираем rpm-пакет c libmemcached
```bash
yum install cyrus-sasl-devel zlib-devel gcc-c++ python-sphinx libuuid-devel libevent-devel rpm-build rpmdevtools rpmdev-setuptree
```
```bash
/usr/sbin/useradd makerpm
```
```bash
su -- makerpm
```
```bash
rpmdev-setuptree
```
```bash
tree
```
```bash
cd
```
```bash
wget https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz
```
```bash
tar -xvf libmemcached-1.0.18.tar.gz
```
```bash
cd libmemcached-1.0.18
```
```bash
./configure 
```
```bash
make rpm
```
```bash
find . -name ‘*rpm*’
```

```bash
cp /home/makerpm/rpmbuild/SRPMS/libmemcached-1.0.18-1.src.rpm /home/makerpm/rpmbuild/RPMS/x86_64/libmemcached-1.0.18-1.x86_64.rpm /home/makerpm/rpmbuild/RPMS/x86_64/libmemcached-devel-1.0.18-1.x86_64.rpm /home/makerpm/rpmbuild/RPMS/x86_64/libmemcached-debuginfo-1.0.18-1.x86_64.rpm /root/
```
```bash
yum localinstall libmemcached-1.0.18-1.x86_64.rpm libmemcached-devel-1.0.18-1.x86_64.rpm
```


## установка самого расширения memcached для не дефолтной сборки php 7

```bash
cd /root
```
```bash
pecl channel-update pecl.php.net
```
```bash
pecl download memcached
```
```bash
tar xf memcached-3.0.3.tgz
```
```bash
/opt/php70/bin/phpize
```
```bash
./configure --with-php-config=/opt/php70/bin/php-config
```
```bash
make
```
```bash
make install
```
```bash
echo "extension=memcached.so" > /opt/php70/etc/php.d/memcached.ini
```
```bash
/opt/php70/bin/php -m|grep memcached
```

## установка самого расширения memcached для не дефолтной сборки php 5

```bash
cd /root
```
```bash
pecl channel-update pecl.php.net
```
```bash
pecl download memcached-2.2.0
```
```bash
tar xf  /root/memcached-2.2.0.tgz
```
```bash
cd memcached-2.2.0
```
```bash
/opt/php56/bin/phpize
```
```bash
./configure --with-php-config=/opt/php56/bin/php-config
```
```bash
make
```
```bash
make install
```
```bash
echo "extension=memcached.so" > /opt/php56/etc/php.d/memcached.ini
```
```bash
/opt/php56/bin/php -m|grep memcached
```