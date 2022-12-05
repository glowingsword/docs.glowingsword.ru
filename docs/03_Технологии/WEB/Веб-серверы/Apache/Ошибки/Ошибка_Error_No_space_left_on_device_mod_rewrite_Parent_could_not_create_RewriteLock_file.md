---
title: 'Ошибка Error: No space left on device: mod rewrite: Parent could not create RewriteLock file'
authors: 
 - glowingsword
tags:
 - Apache
 - Ошибки Apache
date: 2020-04-06
---
# Ошибка Error: No space left on device: mod rewrite: Parent could not create RewriteLock file
```
Ошибка Error: No space left on device: mod rewrite: Parent could not create RewriteLock file
```
и
```
Ошибка No space left on device: AH00023: Couldn't create the rewrite-map mutex
```
Возникает из-за того, что на сервере закончились доступные семафоры. 
Список семафоров можно получить командой

``` bash
ipcs -s | grep nobody
```

Очистить семафоры можно командой

``` bash
ipcs -s | grep nobody | awk '{print $2}' | xargs -n 1 ipcrm sem
```

Увеличить количество доступных семафоров и увеличить аптайм apache
можно, изменив параметры вида

``` bash
kernel.msgmni = 512
kernel.sem = 250 128000 32 512
```

в файле /etc/sysctl.conf и выполнив команду

``` bash
sysctl -p
```

для применения новых настроек.

Полезная информация
<https://enlook.wordpress.com/2013/06/20/error-no-space-left-on-device-mod_rewrite-parent-could-not-create-rewritelock-file/>