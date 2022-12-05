---
title: 'Ошибка ERR_SSL_PROTOCOL_ERROR при обращении к phpmyadmin на VPS с ISPManager 5'
authors: 
 - glowingsword
tags:
 - ISPManager
 - ISPManager 5
 - phpMyAdmin
date: 2020-05-08
---
# Ошибка ERR_SSL_PROTOCOL_ERROR при обращении к phpmyadmin на VPS с ISPManager 5

Открываем  ==/etc/nginx/vhosts-includes/phpmyadmin.conf== и заменяем 
``` nginx
proxy_set_header Host $host;
```
на
``` nginx
proxy_set_header Host $host:443;
```

Если это не помогает, изменяем файл ==/var/lib/phpmyadmin/config.inc.php==, добавляем в его конце строку вида
``` php
$cfg['PmaAbsoluteUri'] = 'https://'.$_SERVER['SERVER_NAME'].'/phpmyadmin/';
```