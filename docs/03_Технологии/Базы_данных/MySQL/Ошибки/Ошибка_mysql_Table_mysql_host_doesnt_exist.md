---
title: "Ошибка mysql Table 'mysql.host' doesn't exist"
authors: 
 - glowingsword
tags:
 - MySQL
 - Ошибки MySQL
date: 2020-04-05
---
# Ошибка mysql Table 'mysql.host' doesn't exist

В случае возникновения ошибки вида
``` mysql
160424 9:00:37 \[ERROR\] Fatal error: Can't open and lock privilege
tables: Table 'mysql.host' doesn't exist
```
необходимо проверить реквизиты доступа к `/var/lib/mysql`. И, если с ними
всё в порядке - выполнить команду
``` bash
mysql\_install\_db --user=mysql --ldata=/var/lib/mysql
```
