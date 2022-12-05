---
title: 'Редирект с HTTP на HTTPS в конфигурационном файле nginx'
authors: 
 - glowingsword
tags:
 - Nginx
 - Настройка Nginx
date: 2020-04-04
---
# Редирект с HTTP на HTTPS в конфигурационном файле nginx

Просто добавляем для хоста в конец блока server директивы

``` nginx
if ($ssl_protocol = "") {                                
  rewrite ^/(.*) https://$server_name/$1 permanent;
}
```
