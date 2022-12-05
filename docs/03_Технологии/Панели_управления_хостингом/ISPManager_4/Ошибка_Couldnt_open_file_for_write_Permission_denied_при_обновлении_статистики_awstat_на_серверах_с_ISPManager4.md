---
title: 'Ошибка Couldnt open file for write: Permission denied при обновлении статистики awstat на серверах с ISPManager4'
authors: 
 - glowingsword
tags:
 - ISPManager 4
 - Настройка ISPManager 4
 - phpMyAdmin
date: 2020-04-18
---

# Ошибка Couldn't open file for write: Permission denied при обновлении статистики awstat на серверах с ISPManager4

Ошибка вида

``` bash
Create/Update database for config
"/etc/awstats/awstats.example.com.conf" by AWStats version 7.0 (build
1.971) From data in log file
"/var/www/testuser/data/logs/example.com.access.log"... Phase 1 : First
bypass old records, searching new record... Direct access to last
remembered record has fallen on another record. So searching new records
from beginning of log file... Phase 2 : Now process new records (Flush
history on disk after 20000 hosts)... Error: Couldn't open file
"/var/www/testuser/data/www/example.com/webstat/awstats082016.example.com.tmp.16953"
for write: Permission denied Setup
('/etc/awstats/awstats.example.com.conf' file, web server or
permissions) may be wrong. Check config file, permissions and AWStats
documentation (in 'docs' directory).
```

как правило возникает из-за заданий вида
``` bash
cat /etc/cron.d/awstats MAILTO=root
```

``` bash
*/10 * * * * www-data [ -x /usr/share/awstats/tools/update.sh ] && /usr/share/awstats/tools/update.sh
```
``` bash
0 3 * * * www-data [ -x /usr/share/awstats/tools/buildstatic.sh ] && /usr/share/awstats/tools/buildstatic.sh
```
указанных в файле /etc/cron.d/awstats. Для решения данной проблемы необходимо удалить данный файл.