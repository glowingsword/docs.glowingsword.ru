---
title: 'Ошибка вида SSL ERROR RX RECORD TOO LONG после установки SSL-сертификата'
authors: 
 - glowingsword
tags:
 - Nginx
 - Ошибки Nginx
 - Ошибки Apache
date: 2020-04-04
---

# Ошибка вида SSL ERROR RX RECORD TOO LONG после установки SSL-сертификата

Причина возникновения данной проблемы определяется командой 
```bash
openssl s_client -connect yourdomain.tld:*port*
```

## Фикс для nginx

Ищем в конфигурационном файле nginx вхождения вида 
```
listen IP;
```
и заменяем на 

```bash
listen IP:80;
```
Если этого оказалось не достаточно, ищем вхождения вида
```bash
listen IP:443;
```
и заменяем на 
```bash
listen IP:443 ssl;
```
или

```bash
listen IP:443;
ssl on;
```
в зависимости от предпочтений(лучше первый вариант, второй считается устаревшим и скоро перестанет поддерживаться).

## Фикс для Apache

Заменяем вхождения вида 
```apacheconf
NameVirtualHost *
```
в конфиге на 
```apacheconf
NameVirtualHost *:80
```
а 

```apacheconf
<VirtualHost *>
```
на 
```apacheconf
<VirtualHost *:80>
```
где нужно добавляем также Virtualhost для 443-го порта
```bash
<VirtualHost *:443>
```
Cохраняем изменения в конфигурационном файле, после чего перезапускаем веб-сервре apache.
