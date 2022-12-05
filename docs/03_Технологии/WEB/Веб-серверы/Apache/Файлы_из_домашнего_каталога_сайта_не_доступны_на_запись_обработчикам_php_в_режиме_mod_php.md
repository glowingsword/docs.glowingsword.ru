---
title: Файлы из домашнего каталога не доступны на запись, когда php используется в режиме mod php
authors: 
 - glowingsword
tags:
 - Apache
 - Настройка Apache
date: 2020-04-04
---
# Файлы из домашнего каталога не доступны на запись, когда php используется в режиме mod php

К примеру, у нас есть сайт пользователя user1, созданного так
``` bash
useradd -m -b /var/www/ -d /var/www/user1 user1
```

Для того, что-бы разные виртуальные хосты могли работать от разных пользователей нужно каждого из пользователей добавить в группу apache.
Добавляем

``` bash
usermod -a -G apache user1
```

После чего рекурсивно меняем права на файлы и каталоги сайта, примерно так:

``` bash
find /var/www/user1/sites/mysite.example -type f -exec chmod 664 {} \;
find /var/www/user1/sites/mysite.example -type d -exec chmod 775 {} \;
```
Где /var/www/user1/sites/mysite.example - хомяк соответствующего сайта.

