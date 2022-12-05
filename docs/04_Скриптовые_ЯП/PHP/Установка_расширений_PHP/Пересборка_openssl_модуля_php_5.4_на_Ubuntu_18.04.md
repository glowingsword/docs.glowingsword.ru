---
title: 'Пересборка GD c поддержкой WebP и Freetype для php 7.4 на Debian и Ubuntu'
authors: 
 - glowingsword
tags:
 - PHP
 - 'Установка расширений PHP'
 - GD
todo: 'Допилить статью, как будет время'
date: 2020-04-21
---
# Пересборка openssl модуля php 5.4 на Ubuntu 18.04

## Подготовительные работы перед сборкой

Логинимся под рута, чтобы не вбивать перед каждой командой sudo

```bash
sudo -i
```
Обновляем информацию о доступных версиях пакетов

```bash
apt update
```
Устанавливаем необходимые для сборки зависимости, если они не были установлены ранее

```bash
apt install wget php build-essential libcurl4-openssl-dev libmcrypt-dev libssl-dev autoconf
```

## Установка кастомной версии openssl в отдельный каталог
### Получаем исходники openssl 1.0.2
```bash
cd /usr/local/src/
```

```bash
wget https://www.openssl.org/source/openssl-1.0.2o.tar.gz
```
```bash
tar -xzvf openssl-1.0.2o.tar.gz
```
```bash
pushd openssl-1.0.2o
```

### Собираем openssl 1.0.2 в /opt/openssl102
```bash
mkdir -p /opt/openssl102
```

```bash
./config -fPIC shared --prefix=/opt/openssl102 --openssldir=/opt/openssl102/openssl
```

```bash
make
```
```bash
make test
```

### Устаналиваем openssl 1.0.2 

Устанавливаем собранную нами версию openssl 1.0.2 в кастомный каталог /opt/openssl102

```bash
sudo make install
```
Возвращаемся в /usr/local/src

```bash
popd
```
## Устанавливаем модуль openssl для php 5.4.45
### Качаем исходники php 5.4
Качаем исходники нужной нам версии php 5.4.45

```bash
wget https://www.php.net/distributions/php-5.4.45.tar.gz
```
### Распаковываем php 5.4

```bash
tar -vzxf php-5.4.45.tar.gz
```
### Настраиваем нужный нам модуль перед сборкой

```bash
cd php-5.4.45/ext/openssl
```

```bash
cp config0.m4 config.m4
```

```bash
/opt/php54/bin/phpize
```

```bash
./configure --with-openssl=/opt/openssl102 --with-php-config=/opt/php54/bin/php-config
```
### Собираем модуль openssl

```bash
make
```


```bash
make test
```

### Устанавливаем модуль openssl

```bash
make install
```

### Включаем собранный модуль openssl

```bash
echo "extension=openssl.so" > /opt/php54/etc/mods-available/openssl.ini
```


```bash
ln -s /opt/php54/etc/mods-available/openssl.ini /opt/php54/etc/php.d/openssl.ini
```

### Проверяем, корректность установки собранного нами модуля openssl

```bash
/opt/php54/bin/php -m|grep -i openssl
```

Видим в выхлопе

```bash
openssl
```

Значит мы собрали модуль верно, а это значит,  самое время устроить перерыв, и пойти пить кофе...