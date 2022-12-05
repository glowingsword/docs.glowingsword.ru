---
title: 'Ошибка "read data timeout in 40 seconds"'
authors: 
 - glowingsword
tags:
 - Nginx
 - Ошибки Nginx
date: 2020-04-04
---
# Ошибка "read data timeout in 40 seconds"
Для решения данной проблемы необходимо в файл /etc/httpd/conf.d/fcgid.conf добавить директиву

``` apacheconf
IPCCommTimeout 300
```
или повысить значение данной директивы, если в конфигурационном файле
она уже присутствует.
