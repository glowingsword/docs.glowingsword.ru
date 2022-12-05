---
title: "InnoDB: Your database may be corrupt or you may have copied the InnoDB"
authors: 
 - glowingsword
tags:
 - MySQL
 - Ошибки MySQL
date: 2020-04-06
---
# InnoDB: Your database may be corrupt or you may have copied the InnoDB

Если mysqld падает с ошибкой вида

```
InnoDB: Your database may be corrupt or you may have copied the InnoDB
InnoDB: tablespace but not the InnoDB log files. See InnoDB:
<http://dev.mysql.com/doc/refman/5.5/en/forcing-innodb-recovery.html>
InnoDB: for more information.
```
то, для решения данной проблемы, бэкапим текущее состояние базы, после
чего в конфигурационный файл /etc/my.cnf добавляем параметр
``` ini
innodb_force-recovery=6
```
и запускаем mysql.