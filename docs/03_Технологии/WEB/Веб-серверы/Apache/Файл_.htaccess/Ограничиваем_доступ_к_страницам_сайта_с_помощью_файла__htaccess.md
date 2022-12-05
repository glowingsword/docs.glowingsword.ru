---
title:  "Ограничиваем доступ к страницам сайта с помощью файла .htaccess"
authors: 
 - glowingsword
tags:
 - Apache
 - .htaccess
 - Правила перенаправления
 - Редиректы
date: 2020-07-15
---

# Ограничиваем доступ к страницам сайта с помощью файла .htaccess
## Ограничиваем доступ к сайту для всех посетителей,разрешаем доступ к сайту для определённого IP-адреса

```apacheconf
Order deny,allow
Deny from all
Allow from IP
```

## Ограничиваем доступ к сайту для всех с помощью диалога базовой авторизации, разрешаем доступ без прохождения диалога базовой авторизации для определённого IP-адреса(для Apache 2.2.x)

```bash
Order deny,allow
Deny from all
AuthType Basic
AuthUserFile /www/.site_htpasswd
AuthName "Protected Area"
require valid-user
Allow from IP
Satisfy Any
```

## Ограничиваем доступ к сайту для всех с помощью диалога базовой авторизации, разрешаем доступ без прохождения диалога базовой авторизации для определённого IP-адреса(для Apache 2.4.x)

```bash
AuthType Basic
AuthUserFile /www/.site_htpasswd
AuthName "Protected Area"

<RequireAny>
    Require ip IP
    Require valid-user
</RequireAny>
```