---
title: 'Использование API ISPManager 4'
authors: 
 - glowingsword
tags:
 - ISPManager
 - 'ISPManager 4 API'
date: 2020-04-04
---
# Использование API ISPManager 4

## Включить учётную запись клиента

``` bash
/usr/local/ispmgr/sbin/mgrctl -m ispmgr user.enable u1234567
```

## Отключить учётную запись клиента

``` bash
/usr/local/ispmgr/sbin/mgrctl -m ispmgr user.disable u1234567
```

## Вход в панель управления ISPManager, если нет пароля root, но есть root-доступ к серверу

Формируем ключ

``` bash
pwgen 20
```

создаём пользовательскую сессию для авторизации по созданному ключу

``` bash
/usr/local/ispmgr/sbin/mgrctl -m ispmgr session.newkey username=user key=123456789abcdefg
```

Переходим по ссылке

``` bash
https://ip/manager/ispmgr?func=auth&username=user&key=123456789abcdefg&checkcookie=no
```

Ссылки на полезную информацию
<http://ru.5.ispdoc.com/index.php/%D0%92%D0%B7%D0%B0%D0%B8%D0%BC%D0%BE%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D0%B5_%D1%87%D0%B5%D1%80%D0%B5%D0%B7_API#.D0.90.D0.B2.D1.82.D0.BE.D1.80.D0.B8.D0.B7.D0.B0.D1.86.D0.B8.D1.8F_.D1.81_.D0.B8.D1.81.D0.BF.D0.BE.D0.BB.D1.8C.D0.B7.D0.BE.D0.B2.D0.B0.D0.BD.D0.B8.D0.B5.D0.BC_authinfo>

<http://www.stableit.ru/search/label/ISPManager>
