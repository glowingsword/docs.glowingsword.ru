---
title: Получить список пользователей Mysql и их привилегий
authors: 
 - glowingsword
tags:
 - MySQL
 - Полезные запросы MySQL
date: 2020-04-04
---
# Получить список пользователей Mysql и их привилегий

 Смотрим

``` bash
SELECT user, host, password, select\_priv, insert\_priv, shutdown\_priv,
grant\_priv FROM mysql.user;
```
и

``` bash
SELECT user, host, db, select\_priv, insert\_priv, grant\_priv FROM
mysql.db;
```