---
title: 'Ошибка Duplicate entry for key при импорте  дампа sql в базу данных mysql'
authors: 
 - glowingsword
tags:
 - 'MySQL'
 - 'Импорт дампов MySQL'
date: 2020-05-13
---

# Ошибка Duplicate entry for key при импорте  дампа sql в базу данных mysql

Если видим ошибку вида 

``` bash
ERROR 1062 (23000) at line 393: Duplicate entry '11510-link="url:https%3a%2f%2ftest.site%2fo_nas-1' for key 'doctermitem'
```

при импорте дампа sql, смотрим в файле дампа в какую талицу пишет запрос, для этого делаем 

``` bash
sed -n '393p' our_dump.sql|head -c 100
```

Далее надим в дампе описание самой таблицы, к примеру в этом случае это 

``` sql
CREATE TABLE `wp_asp_index` (
  `doc` bigint(20) NOT NULL DEFAULT '0',
  `term` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '0',
  `term_reverse` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '0',
  `blogid` mediumint(9) NOT NULL DEFAULT '0',
  `content` mediumint(9) NOT NULL DEFAULT '0',
  `title` mediumint(9) NOT NULL DEFAULT '0',
  `comment` mediumint(9) NOT NULL DEFAULT '0',
  `tag` mediumint(9) NOT NULL DEFAULT '0',
  `link` mediumint(9) NOT NULL DEFAULT '0',
  `author` mediumint(9) NOT NULL DEFAULT '0',
  `category` mediumint(9) NOT NULL DEFAULT '0',
  `excerpt` mediumint(9) NOT NULL DEFAULT '0',
  `taxonomy` mediumint(9) NOT NULL DEFAULT '0',
  `customfield` mediumint(9) NOT NULL DEFAULT '0',
  `post_type` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT 'post',
  `item` bigint(20) NOT NULL DEFAULT '0',
  `lang` varchar(20) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '0',
  UNIQUE KEY `doctermitem` (`doc`,`term`,`blogid`),
  KEY `term_ptype_bid_lang` (`term`(20),`post_type`(20),`blogid`,`lang`(10)),
  KEY `rterm_ptype_bid_lang` (`term_reverse`(20),`post_type`(20),`blogid`,`lang`(10))
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
```

комментируем строку с проблемным ключом
``` sql
/*UNIQUE KEY `doctermitem` (`doc`,`term`,`blogid`),*/
```

сохраняем. Импортируем дамп, на этот раз импорт должен завершиться успешно.

Проверяем, попали ли в базу две записи с одинаковым составным ключом
``` sql
mysql> select doc,term from wp_asp_index where doc=11510 and blogid=1 and term='link="url:https%3a%2f%2ftest.site%2fo_nas';
+-------+----------------------------------------------------+
| doc   | term                                               |
+-------+----------------------------------------------------+
| 11510 | link="url:https%3a%2f%2ftest.site%2fo_nas |
| 11510 | link="url:https%3a%2f%2ftest.site%2fo_nas |
+-------+----------------------------------------------------+
2 rows in set (0.00 sec)
```

Теперь самое интересное. Одну из записей нужно удалить, но отличий у записей минимум, уникальных значений, отличающих их при выборке в обоих записях нет. При удалении с условиями в WHERE у нас дропнутся обе записи.

Чтобы удалить только одну из них, делаем 

``` sql
mysql> UPDATE wp_asp_index set doc=99999 where doc=11510 and blogid=1 and term='link="url:https%3a%2f%2ftest.site%2fo_nas' order by doc limit 1;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```

Теперь у нас две засписи с разным значением doc, так как limit в update делает так, что запрос затрагивает только одну из двух идентичных записей.

``` sql
mysql> select doc,term from wp_asp_index where doc=11510 and blogid=1 and term='link="url:https%3a%2f%2ftest.site%2fo_nas';
+-------+----------------------------------------------------+
| doc   | term                                               |
+-------+----------------------------------------------------+
| 11510 | link="url:https%3a%2f%2ftest.site%2fo_nas|
+-------+----------------------------------------------------+
1 row in set (0.00 sec)
```
``` sql
mysql> select doc,term from wp_asp_index where doc=99999 and blogid=1 and term='link="url:https%3a%2f%2ftest.site%2fo_nas';
+-------+----------------------------------------------------+
| doc   | term                                               |
+-------+----------------------------------------------------+
| 99999 | link="url:https%3a%2f%2ftest.site%2fo_nas |
+-------+----------------------------------------------------+
1 row in set (0.00 sec)
```

Удаляем лишнюю запись

``` sql
mysql> delete from wp_asp_index where doc=99999 and blogid=1 and term='link="url:https%3a%2f%2ftest.site%2fo_nas';
Query OK, 1 row affected (0.00 sec)
```

и возвращаем таблице её unique key

``` sql
mysql> ALTER TABLE wp_asp_index ADD CONSTRAINT doctermitem UNIQUE (`doc`,`term`,`blogid`);
Query OK, 459793 rows affected (11.64 sec)
Records: 459793  Duplicates: 0  Warnings: 0
```

Как видно, когда дубли записей в таблице отсутствуют, и каждое сочетание ==(`doc`,`term`,`blogid`)== у записей уникально, добавление  UNIQUE KEY для таблицы проходит безболезненно. 