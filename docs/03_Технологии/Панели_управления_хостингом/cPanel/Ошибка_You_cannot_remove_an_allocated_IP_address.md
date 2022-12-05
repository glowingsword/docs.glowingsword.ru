---
title: 'Удаляем IP указанный в ошибке "You cannot remove an allocated IP address" на cPanel'
authors: 
 - glowingsword
tags:
 - cPanel
 - Ошибки cPanel
date: 2020-05-02
---

# Удаляем IP указанный в ошибке 'You cannot remove an allocated IP address' на cPanel

Делаем

``` bash
ip=SOME_IP
```
где SOME_IP - IP-адресс что не хочет удаляться.

После чего используем эту переменную в командах

``` bash
grep $ip /etc/userips
```

``` bash
grep -R $ip /var/cpanel/userdata/
```

Чистим в конфигах упоминания об IP, если они ещё остались.

Если упоминания остались только в файлах кэша, как тут

=== "Команда"

    ``` bash
    grep -Rl $ip /var/cpanel/userdata/
    ```

=== "Результат"
    
    ``` bash
    grep -Rl $ip /var/cpanel/userdata/
    /var/cpanel/userdata/u1234567/cache.json
    /var/cpanel/userdata/u1234567/cache
    ```

удаляем данные файлы кэша. 

После чего обновляем кэш userdata командой
``` bash
/scripts/updateuserdatacache
```
И пересобираем пул IP панели cPanel командой
``` bash
/usr/local/cpanel/3rdparty/bin/perl /scripts/rebuildippool
```
