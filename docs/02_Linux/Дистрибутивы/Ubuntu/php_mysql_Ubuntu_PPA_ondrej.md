---
title:  'Установка свежих версий php и mysql на Ubuntu из PPA ondrej'
authors: 
 - glowingsword
tags:
 - Ubuntu
 - Настройка Ubuntu
 - php
todo: 'Доработать статью, добавить про php-fpm'
date: 2020-04-28
---
# Установка свежих версий php и mysql на Ubuntu из PPA ondrej

Ставим саму репу
``` bash
sudo apt install software-properties-common
```
``` bash
sudo add-apt-repository ppa:ondrej/php
```
Обновляем сведения о доступных пакетах

``` bash
sudo apt update
```

Стамим нужный нам пакет php 7.4

``` bash
sudo apt install php7.4
```
Нужные расширения ставятся с помощью

``` bash
sudo apt install php7.4-extension_name
```

К примеру, так устанавливается набор типичных расширений php, что используются большинством современных CMS

``` bash
sudo apt install php7.4-common php7.4-mysql php7.4-xml php7.4-xmlrpc php7.4-curl php7.4-gd php7.4-imagick php7.4-cli php7.4-dev php7.4-imap php7.4-mbstring php7.4-opcache php7.4-soap php7.4-zip php7.4-intl -y
```

Отключаем модуль apache системной сборки(в нашем случае версии 7.0)

``` bash
sudo a2dismod php7.0
```

Включаем наш

``` bash
sudo a2enmod php7.4
```
``` bash
sudo service apache2 restart
```
Для консоли и mod_fcgid изменить дефолтную версию php можно с помощью ==update-alternatives==

``` bash
sudo update-alternatives --set php /usr/bin/php7.4
```
``` bash
sudo update-alternatives --set php-cgi /usr/bin/php7.4-cgi
```

!!! info "Хозяйке на заметку..."
    Полный список приложений, путь к которым у вас может возникнуть необходимость(или желание) изменить

    * php
    * phpize
    * pear
    * peardev
    * pecl
    * phar
    * phar.phar
    * php-cgi
    * php-config
    * phpdbg


* [`https://github.com/oerdnj/deb.sury.org/wiki/PPA-migration-to-ppa:ondrej-php`](https://github.com/oerdnj/deb.sury.org/wiki/PPA-migration-to-ppa:ondrej-php)
* <https://gist.github.com/asakasinsky/a963b2a2ee0cce3a2c736ffadbf2ba7d>
* <https://tecadmin.net/switch-between-multiple-php-version-on-ubuntu/>