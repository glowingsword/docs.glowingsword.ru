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
# Пересборка GD c поддержкой WebP и Freetype для php 7.4 на Debian и Ubuntu
## Подготовительный этап
### Ставим зависимости, необходимые для сборки
Для начала ставим зависимости

``` bash
apt install autoconf gcc make pkg-config libgd-dev pkg-config libjpeg62-turbo-dev libtiff5-dev libturbojpeg0-dev libpng-dev libjpeg-dev libwebp-dev libfreetype6-dev libxpm-dev
```
### Смотрим точную версию необходимой нам сборки php
Смотрим, какой точно версии php у нас на тачке, вплоть до минорной версии.

=== "Команда"
    ``` bash
    /opt/php74/bin/php  -v
    ```

=== "Результат"
    ```
    # /opt/php74/bin/php  -v
    PHP 7.4.3 (cli) (built: Dec 23 2019 09:25:38) ( NTS )
    Copyright (c) The PHP Group
    Zend Engine v3.4.0, Copyright (c) Zend Technologies
    with Zend OPcache v7.4.3, Copyright (c), by Zend Technologies
    ```

###  Качаем исходники именно этой версии
качаем исходники точно такой же версии(это важно)

``` bash
wget https://www.php.net/distributions/php-7.4.3.tar.gz
```
### Распаковка каталога с исходниками и переход в него
Распаковываем их

``` bash
tar -vxzf  php-7.4.3.tar.gz
```

Переходим в распакованный каталог php-7.4.3

``` bash
cd php-7.4.3
```

## Сборка нужного модуля
### Этап настройки будущей собираемого модуля
Выполняем phpize

``` bash
/opt/php74/bin/phpize
```
Выполняем ./configure с нужными нам параметрами, обязательно указываем --with-webp и --with-freetype

``` bash
./configure --with-freetype=shared,/usr --with-webp=shared,/usr --with-jpeg=shared,/usr --with-xpm=shared,/usr/X11R6 --enable-shared --with-php-config=/opt/php74/bin/php-config
```

### Сборка модуля GD
Выполняем make для сборки

``` bash
make
```

Выполняем установку нашего пересобранного расширения

``` bash
 make install
```
## Проверка расботоспособности модуля и его возможностей
Проверяем, что у нас получилось

=== "Команда для проверки"
    ``` php
    /opt/php74/bin/php -r 'print_r(gd_info());'
    ```

=== "Результат"
    ``` bash
    /opt/php74/bin/php -r 'print_r(gd_info());'
    Array
    (
        [GD Version] => bundled (2.1.0 compatible)
        [FreeType Support] => 1
        [FreeType Linkage] => with freetype
        [GIF Read Support] => 1
        [GIF Create Support] => 1
        [JPEG Support] => 1
        [PNG Support] => 1
        [WBMP Support] => 1
        [XPM Support] => 1
        [XBM Support] => 1
        [WebP Support] => 1
        [BMP Support] => 1
        [TGA Read Support] => 1
        [JIS-mapped Japanese Font Support] => 1
    )
    ```

Как видно, всё получилось. 

Лочим пакет php, чтобы он не обновлялся, а то наш GD слетит
``` bash
apt-mark hold isp-php73
```

Проверяем
``` bash
apt-mark showhold
```

https://github.com/docker-library/php/issues/931
https://github.com/docker-library/php/issues/912#issuecomment-559918036