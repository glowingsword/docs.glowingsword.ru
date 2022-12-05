---
title: PHPMyAdmin error – Access Denied Unable to establish a PHP session на CPanel
authors: 
 - glowingsword
tags:
 - cPanel
 - phpMyAdmin
date: 2020-04-04
---
# PHPMyAdmin error – Access Denied Unable to establish a PHP session на CPanel

Проверяем есть ли в хомяке юзера каталог tmp, и какие на него выставлены
права

``` bash
ls -la ~u1234567/tmp
```
Если каталога нет - создаём его, и устанавливаем на него права доступа
755. Если каталог есть, просто фиксим права доступа к каталогу.