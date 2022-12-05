---
title: "Получаем IP с которых пытаются брутить учётные записи MYSQL"
authors: 
 - glowingsword
tags:
 - MySQL
date: 2020-04-04
---
# Получаем IP с которых пытаются брутить учётные записи MYSQL

Выполняем запрос

```mysql
SELECT IP,COUNT_AUTHENTICATION_ERRORS,FIRST_ERROR_SEEN,LAST_ERROR_SEEN from performance_schema.host_cache WHERE COUNT_AUTHENTICATION_ERRORS > "3" ORDER BY COUNT_AUTHENTICATION_ERRORS;  
```

если нужны только последние 10 записей

```mysql
SELECT * FROM ( SELECT IP,COUNT_AUTHENTICATION_ERRORS,FIRST_ERROR_SEEN,LAST_ERROR_SEEN from performance_schema.host_cache WHERE COUNT_AUTHENTICATION_ERRORS > "3" ORDER BY COUNT_AUTHENTICATION_ERRORS DESC LIMIT 10 ) sub ORDER BY COUNT_AUTHENTICATION_ERRORS ASC;
```

получаем таблицу с IP, количеством ошибок подключения, временем появления первой и последней ошибки. Анализируем. Блокируем наиболее буйных, если необходимо.

