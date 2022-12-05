---
title: 'Проблема с редиректом на не корректный порт при использовании Nginx'
authors: 
 - glowingsword
tags:
 - Nginx
date: 2020-04-05
---
# Проблема с редиректом на не корректный порт при использовании Nginx

В случае возникновения проблемы с редиректом на не корректный порт при использовании Nginx в связке с другим сервером, к примеру apache, при обращении к страницам без завершающего слэша(trailing slash) убеждаемся, что для соответствующих локейшенов вместо

``` nginx
proxy_set_header Host $host;
```

указана директива

``` nginx
proxy_set_header Host $http_host; 
```

Dажно, что-бы вместо $host использовалась директива `$http_host`.

Также, в некоторых случаях проблему решает добавление директивы

``` nginx
proxy_set_header X-Forwarded-Host $http_host;
```

где также в качестве значения заголовка `X-Forwarded-Host` необходимо
указать `$http_host`.

Полезные ссылки:

-   <http://serverfault.com/questions/351212/nginx-redirects-to-port-8080-when-accessing-url-without-slash>
-   <http://www.linuxquestions.org/questions/linux-server-73/strange-nginx-redirects-without-trailing-slash-930876/>