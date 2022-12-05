---
title: 'Устраняем ошибку "Premature end of script headers"'
authors: 
 - glowingsword
tags:
 - Nginx
 - Apache
 - Ошибки Apache
 - Ошибки Nginx
 - настройка Apache
 - Настройка Nginx
todo: 'Разбросать статью по трём небольшим статьям.'
date: 2020-04-05
---
# Устраняем ошибку "Premature end of script headers"

Зачастую данная ошибка соседствует с ошибкой вида "mod_fcgid: read data timeout in 40 seconds" и возникает из-за превышения лимитов, указанных в настройках nginx. Для решения данной проблемы в конфигурационном файле nginx приводим к следующему виду параметры.

``` nginxconf
proxy_connect_timeout 600s;
proxy_send_timeout 600s;
proxy_read_timeout 600s;
send_timeout 600s;
```

Часто после увеличения данных параметров возникает ошибка "\*11119
upstream timed out (110: Connection timed out) while reading response
header from upstream", для устранения которой необходимо скорректировать
настройки Apache

``` apacheconf
FcgidIdleTimeout 600 
IPCCommTimeout 600
```
в файле /etc/httpd/conf.d/fcgid.conf

Кроме того, важно проверить, что-бы в файле php.ini значение параметров
соответствовало периоду времени, указанному в изменённых на предыдущем
этапе настройках

``` phpini
max_input_time = 600 
max_execution_time = 600
```