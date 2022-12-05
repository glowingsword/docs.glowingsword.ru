---
title: Дамп баз данных Mysql
authors: 
 - glowingsword
tags:
 - MySQL
 - Дамп MySQL
date: 2020-04-04
---
# Дамп баз данных Mysql

## Дамп всех баз
### Дампим все базы, а также события, процедуры и триггеры
Если нужно сдампить все базы, дампим так
``` bash
mysqldump --events --routines --triggers --all-databases > /root/all-databases_$(LC_TIME='en_US.UTF-8' date '+%Y%m%d').sql
```
### Дампим все базы, а также события, процедуры и триггеры
``` bash
mysqldump --events --routines --triggers --all-databases --ignore-table=some_base.specific_table > /root/all-databases_$(LC_TIME='en_US.UTF-8' date '+%Y%m%d').sql
```

если нужно сдампить все базы и таблицы, кроме одной повреждённой.

Если часть системных таблиц тоже побито, не нужно дампить все базы, дампим только нужные клиенту базы по одной. 

## Дамп одной базы данных
### Дамп одно базы данных, и всех событий, процедур и триггеров
Дампим по одной базе за раз
``` bash
mysqldump --events --routines --triggers some_db01  > /root/some_db01_$(LC_TIME='en_US.UTF-8' date '+%Y%m%d').sql
```
### Дамп одно базы данных, и всех событий, процедур и триггеров кроме битых
Если какую-то таблицу повредило так, что даные с неё не считываются, делаем так
``` bash
mysqldump --events --routines --triggers some_db01 --ignore-table=some_db01.specific_table > /root/some_db01_$(LC_TIME='en_US.UTF-8' date '+%Y%m%d').sql
```

где some_db01 - наша базы, а specific_table - повреждённая талица, которую не нужно дампить.

## Дампим информацию о пользователях и доступных им базах
Cмотрим что за пользователи добавлены в базу, дампим инфу о них, если нужно, в отдельный дамп.
``` bash
mysqldump mysql user > /root/mysql_user_(LC_TIME='en_US.UTF-8' date '+%Y%m%d').sql
```
Делаем тоже самое для инфы о базах данных
``` bash
mysqldump mysql db > /root/mysql_db_(LC_TIME='en_US.UTF-8' date '+%Y%m%d').sql
```
это поможет нам потом восстановить пользователей и права на доступ к нужной базе.