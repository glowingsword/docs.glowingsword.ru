---
title: 'Ошибка Client intended to send too large body'
authors: 
 - glowingsword
tags:
 - Nginx
 - Ошибки Nginx
date: 2020-04-04
---
# Ошибка Client intended to send too large body

Если в логах веб-сервера nginx мелькают записи вида
```
2016/04/30 08:07:28 \[error\] 3175\#0: \*859 client intended to send too
large body: 110771865 bytes, client: 122.122.122.122, server:
localhost.loc, request: "POST /myadmin/import.php HTTP/1.1", host:
"123.123.123.123", referrer:
"<http://123.123.123.123/myadmin/db_import.php>"
```

значит ограничение, указываемое в конфигурационном файле nginx с помощью
директивы `client_max_body_size`, ограничивающей размер тела запросов,
было превышено. 

Для решения данной проблемы значение данного параметра
необходимо увеличить до размера, указанного в сообщении об ошибке(или
большего размера). Изменяем значение `client_max_body_size` в файле
`/etc/nginx/nginx.conf` на нужное нам, к примеру

``` nginx
client_max_body_size 256M;
```
после чего перезапускаем nginx.
