---
title: 'Запросы InternalDummyConnection'
authors: 
 - glowingsword
tags:
 - MySQL
 - Ошибки MySQL
date: 2020-04-05
---
# Запросы InternalDummyConnection

Запросы вида

``` bash
1 - - \[17/Jun/2016:11:37:54 +0400\] "OPTIONS \* HTTP/1.0" 200 - "-"
"Apache/2.2.15 (CentOS) (internal dummy connection)"
1 - - \[17/Jun/2016:11:44:33 +0400\] "OPTIONS \* HTTP/1.0" 200 - "-"
"Apache/2.2.15 (CentOS) (internal dummy connection)"
1 - - \[17/Jun/2016:11:44:57 +0400\] "OPTIONS \* HTTP/1.0" 200 - "-"
"Apache/2.2.15 (CentOS) (internal dummy connection)"
1 - - \[17/Jun/2016:11:45:02 +0400\] "OPTIONS \* HTTP/1.0" 200 - "-"
"Apache/2.2.15 (CentOS) (internal dummy connection)"
```

используются веб-сервером Apache для передачи данных о соединении. Как
правило, основной процесс веб-сервера apache создаёт данные запросы для
того, что-бы вывести из спящего состояния свои дочерние процессы.

Подробно данный процесс освешается на странице
<http://wiki.apache.org/httpd/InternalDummyConnection>

Снизить количество данных запросов может изменение значения
`MaxRequestsPerChild` с 0 на 4096 в конфигурационном файле Apache, а также
увеличение значения `MaxSpareServers`.
