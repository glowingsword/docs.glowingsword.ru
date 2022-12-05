---
title: 'Ошибка Apache does not start: No such file or directory: mod fcgid: Cant create shared memory for size 1200712 bytes'
authors: 
 - glowingsword
tags:
 - Apache
 - Ошибки Apache
date: 2020-04-05
---
# Ошибка Apache does not start: No such file or directory: mod fcgid: Can't create shared memory for size 1200712 bytes

Ошибка `Apache does not start: No such file or directory: mod\_fcgid:
Can't create shared memory for size 1200712 bytes` чаще всего возникает
из-за отсутствия директории, указанной в параметре `FcgidIPCDi`r в файле
`/etc/httpd/conf.d/fcgid.conf`

Для устранения ошибки проверяем в данном файле значение параметров
``` bash
FcgidIPCDir /var/run/mod\_fcgid FcgidProcessTableFile
/var/run/mod\_fcgid/fcgid\_shm
```
и права на файлы и каталоги в данном каталоге
``` bash
ls -la /var/run/mod\_fcgid/
```
в случае отсутствия данного каталога и файла, создаём необходимый
каталог с помощью
``` bash
mkdir -p /var/run/mod\_fcgid
```
Полезные материалы

<http://kb.odin.com/en/121494>
