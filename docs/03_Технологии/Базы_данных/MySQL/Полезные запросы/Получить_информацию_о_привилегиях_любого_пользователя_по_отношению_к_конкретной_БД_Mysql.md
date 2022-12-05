---
title: 'Получить информацию о привилегиях любого пользователя, который имеет доступ к конкретной базе данных Mysql'
authors: 
 - glowingsword
tags:
 - MySQL
 - Полезные запросы MySQL
date: 2020-04-04
---
# Получить информацию о привилегиях любого пользователя, который имеет доступ к конкретной базе данных Mysql

``` mysql
SELECT 'db', User, Host
FROM db
WHERE Db='mydatabase'

UNION

SELECT 'table', User, Host
FROM table
WHERE Db='mydatabase'

UNION

SELECT 'col', User, Host
FROM table
WHERE Db='mydatabase'
```

где mydatabase необходимо заменить на имя базы данных, для которой
необходимо получить список пользователей и привилегий.
