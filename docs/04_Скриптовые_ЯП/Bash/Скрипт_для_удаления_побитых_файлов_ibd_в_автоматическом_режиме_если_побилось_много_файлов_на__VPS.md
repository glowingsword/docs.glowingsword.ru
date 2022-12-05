---
title: "Скрипт для удаления побитых файлов ibd в автоматическом режиме, если побилось много файлов(для VPS)"
authors: 
 - glowingsword
tags:
 - MySQL
 - "Полезные ссылки на информацию о MySQL"
date: 2020-06-04
---
# Скрипт для удаления побитых файлов ibd в автоматическом режиме, если побилось много файлов(для VPS)

Создаём скрипт с функцией

```bash
 #!/bin/bash

function fix_table {
service mysqld start
exit_status=$?

if [ $exit_status -ne 0 ]; then
    bad_table=$(tail -30 /var/lib/mysql/<hostname>.err|grep -A 1 'Error: could not open single-table tablespace file'|grep <database_name>|awk -F'./|!' '{print $3}'|awk -F'.ibd' '{print $1}');
    echo "Removing  table $bad_table";
    rm /var/lib/mysql/<base_name>/$bad_table.{frm,ibd}
    echo 'Done'
    fix_table
else 
    exit
fi
}
fix_table
```