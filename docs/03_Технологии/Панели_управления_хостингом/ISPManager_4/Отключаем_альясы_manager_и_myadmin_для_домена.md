---
title: 'Отключаем альясы manager и myadmin для домена'
authors: 
 - glowingsword
tags:
 - 'ISPManager 4'
 - 'Настройка ISPManager 4'
 - 'phpMyAdmin'
date: 2020-04-05
---
# Отключаем альясы manager и myadmin для домена(панель управения ISPManager 4)

Для отключения доступа к панели управления при обращении к альясу /manager необходимо закоментировать или удалить строку
``` nginx
include /usr/local/ispmgr/etc/nginx.inc;
```
в файле /etc/nginx/nginx.conf, в блоке server сайта,для которого
необходимо отключить данный яльяс, после чего перезапустить веб-сервер
nginx командой
``` bash
service nginx configtest && service nginx restart
```
Затем в файле `/usr/local/ispmgr/etc/ispmgr.conf` нужно заменить сроку
``` ini
extaction myadmin /myadmin/
```
на
``` ini
extaction myadmin <https://123.123.123.123/myadmin/>
```
где вместо `123.123.123.123` необходимо указать адрес сервера, после чего
необходимо в файле `/etc/httpd/conf.d/phpMyAdmin.conf`(или
`/etc/httpd/conf.d/phpmyadmin.conf` ) закоментировать строку
``` apacheconf
Alias /myadmin /usr/share/phpMyAdmin/
```
После чего необходимо будет перезапустить веб-сервер apache командой
``` bash
service httpd configtest && service httpd restart
```
После произведения данных действий панель управления и phpmyadmin по
адресу вашего сайта отображаться не должны.