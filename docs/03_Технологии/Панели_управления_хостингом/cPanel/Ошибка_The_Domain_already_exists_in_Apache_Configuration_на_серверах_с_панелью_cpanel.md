---
title: 'Ошибка The Domain already exists in Apache Configuration на серверах с панелью cpanel'
authors: 
 - glowingsword
tags:
 - cPanel
 - Ошибки cPanel
date: 2020-04-21
---
# Ошибка The Domain already exists in Apache Configuration на серверах с панелью cpanel
## Проверяем наличие домена в `/etc/userdomains`

``` bash
domain=<domain>
```
``` bash
grep $domain /etc/userdomains
```
и в случае обнаружения удаляем его из файла.


## Проверяем в /var/cpanel/users/* 
Выполняем

``` bash
grep $domain /var/cpanel/users/*`
```
## Проверяем /var/cpanel/userdata/*/main

Проверяем `/var/cpanel/userdata/*/main` 

``` bash
grep $domain /var/cpanel/userdata/*/main
```

что нашли, вычищааем.

## Проверяем не осталось ли в userdata учётки пользователя других файлов с упоминанием домена

``` bash
grep -R $domain /var/cpanel/userdata/<user>/
```

## Удаляем зону DNS домена
 Выполняем
``` bash
/scripts/killdns $domain`
```

## Выполняем скрипт пересоздания кэшей userdata

``` bash
/scripts/updateuserdatacache
```

## Выполняем обновление инфы о доменах

``` bash
/scripts/updateuserdomains
```

## Пересоздаём конфиг веб-сервера
``` bash
/scripts/rebuildhttpdconf
```

## Перезапускаем Apaache
``` bash
service httpd restart
```
Проверяем результат и добавляем заново домен.

> **_NOTE:_**  Возможно, в процессе нужно будет перезапустить панельку. В таком случае юзаем не обязательный пункт "Перезапуск cPanel"

## Перезапуск cPanel

``` bash
cd /etc/rc.d/init.d;./cpanel restart
```

[`https://www.hivelocity.net/kb/how-to-fix-cpanel-error-sorry-the-domain-is-already-set-up-3/`](https://www.hivelocity.net/kb/how-to-fix-cpanel-error-sorry-the-domain-is-already-set-up-3/)

<http://stackoverflow.com/questions/34861827/cpanel-wont-delete-add-on-domain-error-you-do-not-have-control-of-the-subdoma>
<https://crybit.com/how-to-remove-parked-domain-command-line-cpanel/>