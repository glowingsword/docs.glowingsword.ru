---
title: 'Ошибка mod rewrite: Parent could not create RewriteLock file при запуске апачика'
authors: 
 - glowingsword
tags:
 - Apache
 - Ошибки Apache
date: 2020-04-04
---
# Ошибка mod rewrite: Parent could not create RewriteLock file при запуске апачика

В случае возникновения ошибки mod rewrite: Parent could not create
RewriteLock file при запуске апачика необходимо почистить семафоры на
сервере

Смотрим сколько семафоров занято

``` bash
ipcs -s | grep nobody
```

Удаляем старые семафоры

``` bash
ipcs -s | grep nobody | awk '{print $2}' | xargs -n 1 ipcrm sem
```

После чего повторно смотрим,сколько их занято. Количество семафоров
должно заметно уменьшится. После чего успешно перезапускаем апачик.

Материалы

-   <http://crybit.com/parent-could-not-create-rewritelock/>
-   <https://enlook.wordpress.com/2013/06/20/error-no-space-left-on-device-mod_rewrite-parent-could-not-create-rewritelock-file/>