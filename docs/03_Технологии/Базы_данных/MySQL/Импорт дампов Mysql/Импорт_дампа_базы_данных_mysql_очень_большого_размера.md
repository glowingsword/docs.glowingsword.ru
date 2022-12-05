---
title: 'Импорт дампа базы данных mysql очень большого размера'
authors: 
 - glowignsword
tags:
 - MySQL
 - 'Импорт дампов'
date: 2020-04-26
---
# Импорт дампа базы данных mysql очень большого размера

!!! warning "Ахтунг!"
    Так как ограничения у не привилегированных пользователей с большой долей вероятности не дадут импортировать большой дамп, лучше делать это от учётки root базы данных MySQL.

Подключаемся к базе

``` bash
mysql -u root -p
```

Смотрим значения net_buffer_length 

=== "Команда"
    ``` sql
    show variables like "net_buffer_length";
    ```
=== "Результат"
    ``` sql
    mysql> show variables like "net_buffer_length";
    +-------------------+-------+
    | Variable_name     | Value |
    +-------------------+-------+
    | net_buffer_length | 16384 |
    +-------------------+-------+
    1 row in set (0.00 sec)
    ```
и max_allowed_packet 

=== "Команда"
    ``` sql
    show variables like "max_allowed_packet";
    ```

=== "Результат"
    ``` sql
    mysql> show variables like "max_allowed_packet";
    +--------------------+---------+
    | Variable_name      | Value   |
    +--------------------+---------+
    | max_allowed_packet | 4194304 |
    +--------------------+---------+
    1 row in set (0.00 sec)
    ```
И сохраняем их куда-то в текстовый файл, так так они нам ещё понадобятся.


Увеличиваем значение параметра ==net_buffer_length==

``` sql
set global net_buffer_length=1000000;
```

Устанавливаем максимально разрешённый ==max_allowed_packet==

``` sql
set global max_allowed_packet=1000000000;
```

Отключаем проверку foreign key checking для предотвращения задержек, ошибок и не ожидаемого поведения в процессе импорта.

``` sql
SET foreign_key_checks = 0;
```

А теперь тут же, в консоли mysql, в сессии с изменёнными настройками, импортируем дамп с помощью запроса ==source==

``` sql
source file.sql
```

Возвращаем настройки ==mysql== к состоянию, в каком они пребывали до того, как мы начали их изменять

``` sql
SET foreign_key_checks = 1;
```
``` sql
set global max_allowed_packet=4194304;
```
``` sql
set global net_buffer_length=16384;
```

---

Полезная информация, использованная для решения проблемы с импортом больших дампов, благодаря которой появилось это руководство

* <http://stackoverflow.com/questions/13717277/how-can-i-import-a-large-14-gb-mysql-dump-file-into-a-new-mysql-database>
* <http://onedev.net/post/170>
* <https://stackoverflow.com/questions/12425287/mysql-server-has-gone-away-when-importing-large-sql-file>
