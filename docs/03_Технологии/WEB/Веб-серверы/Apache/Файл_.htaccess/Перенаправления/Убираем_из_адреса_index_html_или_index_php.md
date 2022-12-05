---
title:  Убираем из адреса index.html или index.php
authors: 
 - glowingsword
tags:
 - Apache
 - .htaccess
 - Правила перенаправления
 - Редиректы
date: 2020-04-04
---
# Убираем из адреса index.html или index.php

``` apacheconf
# Включаем механизм RewriteRules 
Options +FollowSymLinks
RewriteEngine On
```

``` apacheconf
# Перенаправляем с index.html на чистый URL без указания индексного файла
RewriteCond %{THE_REQUEST} ^[A-Z]{3,9}\ /(.*)index\.html($|\ |\?)
RewriteRule ^ /%1 [R=301,L]
```

``` apacheconf
# Перенаправляем с index.html на чистый URL без указания индексного файла
RewriteCond %{THE_REQUEST} ^[A-Z]{3,9}\ /(.*)index\.php($|\ |\?)
RewriteRule ^ /%1 [R=301,L]
```