---
title: 'Не работает сайт при переключении на php как модуль apache'
authors: 
 - glowingsword
tags:
 - Apache
 - Проблемы Apache
 - настройка Apache
 - PHP
date: 2020-04-22
---
# Не работает сайт при переключении на php как модуль apache

Проверяем установлен ли ==php== как модуль ==apache==, в частности присутствует ли на сервере ==/etc/httpd/modules/libphp5.so==, проверяем содержимое ==/etc/httpd/conf.d/php.conf== и права на файлы и каталоги сайта. 

Также проверяем, нет ли в конфиге проблемного виртуального хоста директивы open_basedir, и удаляем или комментируем данную директиву при обнаружении`
``` apacheconf
php_admin_value open_basedir "/var/www/www-root/data:."
```