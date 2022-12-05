---
title: 'Ошибка squirrelmail при открытии ../data/default pref'
authors: 
 - glowingsword
tags:
 - Веб-приложения
 - squirrelmail
date: 2020-04-04
---
# Ошибка squirrelmail при открытии ../data/default pref

Ошибка вида
```
ошибка при открытии ../data/default\_pref Файл параметров по умолчанию
не найден или недоступен для чтения. Свяжитесь с системным
администратором.
```
Или
```
Error opening ../data/default\_pref Could not create initial preference
file! /var/spool/squirrelmail/pref/ should be writable by user httpd
Please contact your system administrator and report this error.
```
возникает из-за не корректно установленных прав доступа на файлы
`/var/spool/squirrelmail/pref` и `/var/spool/squirrelmail/attach`.

Для ее решения, нужно выполнить команды:

``` bash
chgrp mgrsecure /var/spool/squirrelmail/pref
chgrp mgrsecure /var/spool/squirrelmail/attach
chmod 770 /var/spool/squirrelmail/pref
```

И даём доступ к каталогу `/var/spool/squirrelmail/pref` пользователю
apache командой

``` bash
chown -R apache: /var/spool/squirrelmail/pref
```

также необходимо проверить корректность прав доступа к каталогу
`/var/spool/squirrelmail` и вложенным файлам и каталогам для пользователя
apache(или любого другого пользователя, указанного в файле конфига
apache в качестве юзера, от имени которого выполняются скрипты
squirrelmail), и по необходимости поправить права доступа и владельца.
