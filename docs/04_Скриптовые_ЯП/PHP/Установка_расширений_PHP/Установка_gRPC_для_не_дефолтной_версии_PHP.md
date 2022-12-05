---
title: 'Установка gRPC на не дефолтную версию PHP'
authors: 
 - glowingsword
tags:
 - PHP
 - 'Установка расширений PHP'
todo: 'Допилить статью, как будет время'
date: 2020-06-24
---
# Установка gRPC на не дефолтную версию PHP

```bash
cd /root/
```
```bash
pecl channel-update pecl.php.net
```
```bash
pecl download grpc
```
tar vzxf grpc-1.30.0.tgz
```bash
cd grpc-1.30.0
```
```bash
/opt/php72/bin/phpize
```
```bash
./configure --with-php-config=/opt/php72/bin/php-config
```
```bash
make
```
```bash
make install
```
```bash
echo "extension=grpc.so" > /opt/php72/etc/php.d/grpc.ini
```