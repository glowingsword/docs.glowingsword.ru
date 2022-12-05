---
title: 'Ошибка Client intended to send too large body'
authors: 
 - glowingsword
tags:
 - Nginx
 - 'Ошибки Nginx'
date: 2020-08-21
---
# Поддержка HTTP/2 в Nginx

Поддержка HTTP2 с ALPN появилась в версиях Nginx 1.9.5+, собранных с OpenSSL версии 1.0.2h, или выше.

На серверах с Centos 6 для поддержки HTTP/2 с ALPN необходимо пересобирать Nginx со свежим OpenSSL из исходных кодов.
То же самое касается и некоторых древних версий Debian.

Получить версию Nginx и используемой им библиотеки OpenSSL можно командой

```bash
nginx -V
```
выполненной от рута в консоли сервера.