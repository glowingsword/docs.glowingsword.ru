---
title: 'Установка profobuf на не дефолтную версию PHP'
authors: 
 - glowingsword
tags:
 - PHP
 - 'Установка расширений PHP'
todo: 'Допилить статью, как будет время'
date: 2020-06-24
---
# Установка profobuf на не дефолтную версию PHP

```bash
cd /usr/local/src/
```
```bash
pecl channel-update pecl.php.net
```
```bash
pecl download protobuf
```
```bash
tar vzxf protobuf-3.12.2.tgz
```
```bash
cd protobuf-3.12.2
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
echo "extension=protobuf.so" > /opt/php72/etc/php.d/protobuf.ini
```