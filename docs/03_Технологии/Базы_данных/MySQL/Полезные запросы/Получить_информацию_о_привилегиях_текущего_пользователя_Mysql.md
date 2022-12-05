---
title: Получить информацию о привилегиях текущего пользователя Mysql
authors: 
 - glowingsword
tags:
 - MySQL
 - Полезные запросы MySQL
date: 2020-04-04
---
# Получить информацию о привилегиях текущего пользователя Mysql

Смотрим

``` mysql
SHOW GRANTS;
SHOW GRANTS FOR CURRENT_USER;
SHOW GRANTS FOR CURRENT_USER();
```