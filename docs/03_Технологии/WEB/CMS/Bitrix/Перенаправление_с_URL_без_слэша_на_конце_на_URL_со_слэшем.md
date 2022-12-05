---
title: Перенаправление с URL без слэша на конце на URL со слэшем
authors: 
 - glowingsword
tags:
 - CMS
 - Bitrix
date: 2020-04-04
---
# Перенаправление с URL без слэша на конце на URL со слэшем

В хомяке сайта на Bitrix, в  файл .htaccess сайта правила

``` php
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-l
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteCond %{REQUEST_URI} ^(.*/[^/\.]+)$
  RewriteRule ^(.*)$ http://%{HTTP_HOST}/$1/ [R=301,L]
```