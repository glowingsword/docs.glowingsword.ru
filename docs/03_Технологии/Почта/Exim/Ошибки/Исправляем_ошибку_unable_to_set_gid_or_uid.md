---
title: Исправляем ошибку unable to set gid or uid
authors: 
 - glowingsword
tags:
 - Exim
 - Ошибки Exim
date: 2020-04-04
---
# Исправляем ошибку unable to set gid or uid


В случаях, когда при доставке сообщений возникает ошибка

``` bash
2014-12-14 15:46:46 1Y07dN-0002zX-0D unable to set gid=65 or uid=65 (euid=73): local delivery to info <info@test.ru> transport=procmail_pipe
2014-12-14 15:46:46 1Y07dN-0002zX-0D failed to read delivery status for \1\info@urist-senin.ru from delivery subprocess
```

необходимо проверить права на файл /usr/sbin/exim , и при необходимости
добавить suid bit командой

``` bash
sudo chmod u+s /usr/sbin/exim
```