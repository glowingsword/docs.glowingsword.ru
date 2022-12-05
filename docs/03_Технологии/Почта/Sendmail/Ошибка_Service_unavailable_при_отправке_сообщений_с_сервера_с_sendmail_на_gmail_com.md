---
title: 'Ошибка Service unavailable при отправке сообщений с сервера с sendmail на gmail.com'
authors: 
 - glowingsword
tags:
 - semdmail
 - ошибки semdmail
date: 2020-04-21
---
# Ошибка Service unavailable при отправке сообщений с сервера с sendmail на gmail.com

Возникает при не корректно сконфигурированном `sendmail`. 
Для начала необходимо проверить домен, указанный в качестве локального почтового домена. 
Если значение LOCAL_DOMAIN равно
``` s
LOCAL_DOMAIN(`localhost.localdomain')dnl
```
изменяем его на
``` s
LOCAL_DOMAIN(`domain.ru')dnl
```
где вместо domain.ru нужно указать доменное имя хоста. 

Также убеждаемся что PTR и SPF для сервера настроены корректно.
