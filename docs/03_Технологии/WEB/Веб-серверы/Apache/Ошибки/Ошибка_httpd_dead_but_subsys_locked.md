---
title: 'Ошибка httpd dead but subsys locked'
authors: 
 - glowingsword
tags:
 - Apache
 - Ошибки Apache
date: 2020-04-05
---
# Ошибка httpd dead but subsys locked

Ошибка `httpd dead but subsys locked` возникает после не корректного завершения работы httpd. 
Для решения проблемы нужно завершить процессы httpd(если подобные процессы запущены) командой

``` bash
ipcs -s | grep apache 
ipcs -s | grep apache |  perl -e 'while (`<STDIN>`` ) { @a=split(/\s+/); print `ipcrm sem $a[1]`}'
```
и удалить файл `/var/lock/subsys/httpd` командой

``` bash
rm /var/lock/subsys/httpd
```