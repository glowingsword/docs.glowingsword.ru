---
title: 'Что делать если в Plesk зависло задание на добавление домена'
authors:
 - glowingsword
tags:
 - Plesk
date: 2021-12-27
---
# Что делать если в Plesk зависло задание на добавление домена

Бэкапим базу на случай факапа

```bash
plesk db dump > /root/psa_dump.sql
```

после чего идём в базу Plesk, чтобы найти там повисший таск.

```bash
plesk db
```

Ищем по домену таски, связанные с ним

```sql
select * from longtaskparams where val like '%some.domain%'\G
```

ищем длинные таски, для которых тип таска равен domain-create

```sql
select * from longtasks where type = "domain-create";
```
и среди них выбираем нужный нам таск по id(id в longtasks должен совпадать с task_id из longtaskparams)

```sql
select * from longtaskparams where task_id = 8532\G
```

!!! info "Внимание"
    У нас **task_id** из **longtaskparams** должен совпадать с **id** из **longtasks**.

Удаляем таск и его параметры

```sql
delete from longtasks where type = "domain-create" and id = 8532 limit 1;
delete from longtaskparams where task_id = 8532 limit 10;
```
где limit 10 во втором случае равен количеству rows с парамтерами таска из последнего запроса с select.

