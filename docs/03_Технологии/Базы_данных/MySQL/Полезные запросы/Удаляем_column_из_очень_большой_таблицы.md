---
title: Удаляем column из очень большой таблицы
authors: 
 - glowingsword
tags:
 - MySQL
 - Полезные запросы MySQL
 - Полезные приёмы работы с MySQL
date: 2020-04-04
---
# Удаляем column из очень большой таблицы
## Если важны только данные соответствющих колонок
Так как прямое удаление колонки из очень большой таблицы с индексами - дело очень ресурсоёмкое и небыстрое, вместо удаления column из оригинальной таблицы делаем

``` mysql
create table newTable as select id1, id2 from oldTable;
```

где oldTable - старая таблица, newTable - название новой таблицы, а id1 и id2 - колонки, которые необходимо сохранить(указываем те колонки, что не должны быть затронуты удалением).


## Если важно сохранить типы и индексы значений как у оригинальной таблицы

``` mysql
create table newTable like oldTable;
alter table newTable drop column unusedId;
insert into newTable(id1, id2) select id1, id2 from oldTable;
```

В данном случае мы создаём newTable со структурой и индексами как у оригинальной oldTable, удаляем из неё не нжуный column( в нашем случае unusedId), после чего копируем в таблицу значения тех колонок, которые необходимо сохранить.



[Инфа по теме](https://stackoverflow.com/questions/23173789/mysql-drop-column-from-large-table)