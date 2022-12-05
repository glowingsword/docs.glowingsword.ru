---
title: 'Проблема с кодировкой данных, получаемых скриптами клиента из базы данных MySQL'
authors: 
 - glowingsword
tags:
 - PHP
 - MySQL
date: 2020-04-19
---
# Проблема с кодировкой данных, получаемых скриптами клиента из базы данных MySQL

Лечится добавлением в скрипты двух вызовов вида
``` php
mysql_query("SET NAMES 'utf8'");
mysql_query("SET CHARACTER SET 'utf8'");
```
или, что гораздо лучше, одного вызова mysql_set_charset
``` bash
mysql_set_charset('utf8',$db_conn);
```