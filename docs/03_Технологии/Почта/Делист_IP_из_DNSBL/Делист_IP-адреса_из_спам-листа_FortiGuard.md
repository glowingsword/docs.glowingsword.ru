---
title: 'Делист IP-адреса из спам-листа FortiGuard'
authors: 
 - glowingsword
tags:
 - 'Почта'
 - 'Делист из DNSBL'
date: 2020-08-21
---
# Делист IP-адреса из спам-листа FortiGuard

Проверить IP-адрес на присутствие в их спам-листе можно на `[`https://fortiguard.com/learnmore#as`](https://fortiguard.com/learnmore#as)

Для удаления из их спам-листа переходим на страницу <https://fortiguard.com/faq/antispam/blacklist?url=IP> где вместо IP должен быть указан IP-адрес сервера, который нужно делистнуть из DNSBL. 

Заполняем форуму, указав в качестве значения полей

* URL/IP \* - IP-адрес сервера 
* Contact Name - своё имя 
* Contact Email \* - рабочий email 
* Company - название компании

В качестве значения Your Comment указываем

```
The source of the spam is deleted.
```

Отправляем.

