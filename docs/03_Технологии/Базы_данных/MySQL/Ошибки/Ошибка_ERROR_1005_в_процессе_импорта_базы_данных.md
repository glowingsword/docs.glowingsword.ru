---
title: "Ошибка \"ERROR 1005 (errno: 150)\" в процессе импорта дампа базы данных MySQ"
authors: 
 - glowingsword
tags:
 - MySQL
 - Ошибки MySQL
date: 2023-02-27
---
# Ошибка "ERROR 1005 (errno: 150)" в процессе импорта дампа базы данных MySQL

При импорте дампа базы данных с CONSTRAINT **могут возникать** ошибки errno: 150 или errno 121.
[Подробности](https://stackoverflow.com/questions/4061293/mysql-cant-create-table-errno-150)

Выглядит это, обычно, так

```
ERROR 1005 (HY000) at line 102: Can't create table 'base1.table1' (errno: 150)
```

Эта проблема, как правило, возникает из-за того, что в процессе восстановления mysql восстанавливает некоторые ограничения(CONSTRAINT) до того, как будут восстановлены таблицы, для которых устанавливаются эти ограничения.

Для того, что-бы подобный дамп импортировался правильно, необходимо импортировать его так:
1. убеждаемся что база данных, куда будет идти импорт не содержит таблицы с частично импортированными данными от предыдущей попытки восстановления:
2. подключаемся к базе с помощью mysql.
Пример
```bash
-bash-4.1# cd /path/to/dump/
-bash-4.1# mysql -uuser1 -p  base1
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 388237
Server version: 5.1.52-log Source distribution

Copyright (c) 2000, 2010, Oracle and/or its affiliates. All rights reserved.
This software comes with ABSOLUTELY NO WARRANTY. This is free software,
and you are welcome to modify and redistribute it under the GPL v2 license

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
```
3. Отключаем SET FOREIGN_KEY_CHECKS
```sql
mysql> SET FOREIGN_KEY_CHECKS = 0;
Query OK, 0 rows affected (0.00 sec)
```
4. Собственно, импортируем дамп. 
```sql
mysql> SOURCE base1.sql
```
5. Возвращаем дефолтное значение FOREIGN_KEY_CHECKS после импорта
```sql
mysql> SET FOREIGN_KEY_CHECKS = 1;
Query OK, 0 rows affected (0.00 sec)
```

Также можно изменить импортируемый дамп, в самое его начало добавив ```SET FOREIGN_KEY_CHECKS = 0;```, а в конец ```SET FOREIGN_KEY_CHECKS = 1;```.