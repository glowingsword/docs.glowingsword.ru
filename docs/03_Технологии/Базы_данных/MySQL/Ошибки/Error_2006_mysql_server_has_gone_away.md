---
title: "Ошибка \"ERROR 2006 (HY000): MySQL server has gone away\" в процессе импорта дампа в базу данных MySQL"
authors: 
 - glowingsword
tags:
 - MySQL
 - Ошибки MySQL
date: 2023-02-27
---
# Ошибка "ERROR 2006 (HY000): MySQL server has gone away" в процессе импорта дампа в базу данных MySQL

## Причина проявления ошибки ERROR 2006

Как правило, ошибка возникает из-за того, что сервер баз данных MySQL столкнулся с превышением ограничения на длину пакета(запрос, или несколько запросов, объединённых в рамках одной транзации), определённой в max_allowed_packet. Или с превышением длительности выполнения запроса, которая ограничена значением wait_timeout.

## Решение проблемы с импортом

В консоли mysql смотрим значения 

```bash
SELECT @@global.max_allowed_packet;
SELECT @@global.wait_timeout;
```

и повышаем их на время, чисто для импорта

```sql
SET GLOBAL max_allowed_packet=1073741824;
SET GLOBAL wait_timeout=86400;
```
затем импортируем дамп с помощью 

```sql
source db1.sql;
```

где, вместо db1.sql, указываем имя нужного дампа базы данных.