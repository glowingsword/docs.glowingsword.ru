---
title: "InnoDB: Tablespace for table exists. Please DISCARD the tablespace before IMPORT"
authors: 
 - glowingsword
tags:
 - MySQL
 - Ошибки MySQL
date: 2020-06-04
---
# InnoDB: Tablespace for table exists. Please DISCARD the tablespace before IMPORT

Если mysql упал и не запускается из-за того, что побились файлы InnoDB, при этом в логах мы видим ошибки вида

```yaml
InnoDB: The error means the system cannot find the path specified.
InnoDB: If you are installing InnoDB, remember that you must create
InnoDB: directories yourself, InnoDB does not create them. 
InnoDB: Error: could not open single-table tablespace file
./some\_db/some\_table.ibd InnoDB: We do not continue the crash
recovery, because the table may become InnoDB: corrupt if we cannot
apply the log records in the InnoDB log to it. InnoDB: To fix the
problem and start mysqld: InnoDB: 1) If there is a permission problem in
the file and mysqld cannot InnoDB: open the file, you should modify the
permissions. InnoDB: 2) If the table is not needed, or you can restore
it from a backup, InnoDB: then you can remove the .ibd file, and InnoDB
will do a normal InnoDB: crash recovery and ignore that table. InnoDB:
3) If the file system or the disk is broken, and you cannot remove
InnoDB: the .ibd file, you can set innodb\_force\_recovery &gt; 0 in
my.cnf InnoDB: and force InnoDB to continue crash recovery here.
```

Для решения подобной проблемы необходимо удалить соответствующий ibd-файл таблицы InnodDB.
После чего следует запустить mysql. При запуске файл ibd будет создан заново.

После чего, если есть резервная копия этой базы данных, стоит попытаться восстановить её из резервной копии.
Если в процессе восстановления базы данных из дампа этой базы, полученного ранее при бэкапе, возникнет ошибка вида

```
Tablespace for table exists. Please DISCARD the tablespace before IMPORT
```
необходимо снова удалить созданный ранее автоматически ibd-файл, на этот раз сделать это необходимо при запущенном mysql.

!!! warn "Внимание"
    Ни в коем случае не останавливаем перед этим mysql, так как в процессе последующего запуска файл опять будет создан автоматически, а мы столкнёмся всё с той же ошибкой при импорте, что и ранее.

Удалили ibd-файл при запущенном mysql? Значит пора удалить соответствующую таблицу(или базу, содержащую эту битую таблицу).
Если восстаналиваем всю базу, а не отдельную таблицу, лучше удалить её перед этим с помощью панели управления, или вручную запросом 

```mysql
DROP DATABASE имя_нашей_базы
```

где вместо ==имя_нашей_базы== указываем имя базы данных, что неободимо удалить.

После чего создаём удалённую ранее базу заново, и запускаем импорт данных в созданную базу данных, на этот раз импорт пройдёт без ошибок.