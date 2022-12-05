---
title: 'Ошибка 404 при обращении к phpmyadmin или roundcube на серверах с ISPManager 5 и nginx'
authors: 
 - glowingsword
tags:
 - ISPManager
 - ISPManager 5
 - phpMyAdmin
date: 2020-04-04
---

# Ошибка 404 при обращении к phpmyadmin или roundcube на серверах с ISPManager 5 и nginx

В случае возникновения подобной проблемы при обращении к серверу по адресу вида [https://ip/phpmyadmin](https://ip/phpmyadmin) или [https://ip/roundcube](https://ip/roundcube) необходимо проверить содержимое файла `/etc/nginx/conf.d/isp.conf`. 

Вероятно в нём отсутствует строка вида:
``` nginx
include /etc/nginx/vhosts-includes/*.conf;
```
в результате чего все запросы к IP-адресу сайта без указания доменного
имени перенаправляются к сервису панели управления. Исправляется данная
ошибка простым добавлением упомянутой выше строки в начало блока server
в файле `/etc/nginx/conf.d/isp.conf` и рестартом веб-сервера nginx:
``` bash
nginx -t 
```
``` bash
nginx -s reload
```