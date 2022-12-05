---
title: 'На VPS с ISPManager 5 наблюдается большое количество процессов metric панели управления'
authors: 
 - glowingsword
tags:
 - ISPManager 5
date: 2021-03-07
---

# На VPS с ISPManager 5 наблюдается большое количество процессов metric панели управления

Если на VPS с ISPManager 5(как правило, если всё настроили и решили не продлевать лицензию) внезапно начала расти LA, при этом в top/htop/atop вы видите множество процессов 

```bash
root      9635  0.0  0.0   9516   828 ?        Ss   10:30   0:00  |   \_ /bin/sh -c /usr/local/mgr5/sbin/cron-ispmgr sbin/metric >/dev/null 2>&1
root      9647  0.0  0.0   9516  1128 ?        S    10:30   0:00  |       \_ /bin/sh /usr/local/mgr5/sbin/cron-ispmgr sbin/metric
root      7948  0.1  0.2 133068  6128 ?        S    12:07   0:00  |           \_ sbin/mgrctl -m ispmgr problems.register name=cron id=sbin/metric level=error info=
root     18678  0.0  0.0   9516   832 ?        Ss   10:35   0:00  |   \_ /bin/sh -c /usr/local/mgr5/sbin/cron-ispmgr sbin/metric >/dev/null 2>&1
root     18684  0.0  0.0   9516  1132 ?        S    10:35   0:00  |       \_ /bin/sh /usr/local/mgr5/sbin/cron-ispmgr sbin/metric
root      7981  0.1  0.2 133068  6128 ?        S    12:07   0:00  |           \_ sbin/mgrctl -m ispmgr problems.register name=cron id=sbin/metric level=error info=
root     27665  0.0  0.0   9516   828 ?        Ss   10:40   0:00  |   \_ /bin/sh -c /usr/local/mgr5/sbin/cron-ispmgr sbin/metric >/dev/null 2>&1
root     27668  0.0  0.0   9516  1132 ?        S    10:40   0:00  |       \_ /bin/sh /usr/local/mgr5/sbin/cron-ispmgr sbin/metric
```

Необходимо остановить процессы metric. 

Если на сервере наблюдаются только  ==cron-ispmgr sbin/metric== изменяем файлы ==/usr/local/mgr5/etc/core.conf== и ==/usr/local/mgr5/etc/ispmgr.conf== удаляя из них параметр

```yaml
Option UsageStatAgree
```

после чего выполнить

```bash
/usr/local/mgr5/sbin/mgrctl -m core exit
```

В случае, когда кроме процесса ==cron-ispmgr sbin/metric== на сервере наблюдаются и процессы ==ispmgr problems.register== с ==id=sbin/metric== проблема уже так просто не решается.  Просто остановить процессы metric не достаточно, панель запустит их заново, так как система решения проблем панели пытается собрать информацию об ошибке, и повторить запуск проблемного процесса.

В результате, когда ошибки с metric ушли в problems, необходимо предварительно почистить записи в problems, и только потом останавливать процессы metric.

```bash
mv /usr/local/mgr5/var/run/mgrctl.ispmgr_problem_* /root/ispmgr_problem/
```

```bash
rm -fR /usr/local/mgr5/var/run/mgrctl.ispmgr_problem_*
```
```bash
sqlite3 /usr/local/mgr5/etc/ispmgr_problems.db
```

```sql
SQLite version 3.7.17 2013-05-20 00:56:22
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> delete from problems_log;
sqlite> delete from problems;
sqlite> delete from problems_desc;
sqlite> .exit
```

```bash
rm -fR /usr/local/mgr5/var/run/mgrctl.ispmgr_problem_*
```
```bash
kill -15 `ps auxfS | grep "ispmgr_problem\|core\|problems.autosolve\|ispmgr" | awk '{print $2}'`
```

если часть процессов осталась, повторяем с -9.


Проверяем, что их больше нет

```bash
ps auxf|grep metric
```
если что-то есть, выкашиваем его руками

```bash
killall -15 metric
```
```bash
killall -9 metric
```

Если кроме проблем с metric наблюдаются и другие, связанные с licctl процессами, останавливаем crond

```bash
systemctl stop crond
```

!!! info 'Внимание'
	Обязательно останавливаем его, иначе панель новые задания крон успеет прописать, и наши старания окажутся напрасными.

Затем выполняем
```bash
crontab -e
```
и комментируем символом № в начале строки все задания панели, над которыми выше есть строка комментария с упоминанием "## ISPmanager".

Сразу после этого останавливаем ihttpd

```bash
systemctl stop ihttpd
```
и вырубаем его из автозапуска

```bash
systemctl disable ihttpd
```
после чего останавливаем все связанные с панелью процессы

```bash
/usr/local/mgr5/sbin/mgrctl -m core exit
```
```bash
killall -9 ispmgr
```
```bash
killall -9 licctl
```
```bash
killall -9 metric
```

Запускаем crond 
```bash
systemctl start crond
```

Ждём пару минут, и смотрим вывод pstree|ps auxfS на предмет наличия процессов, которые мы останавливали выше.

Если не видно данных процессов – значит мы всё сделали верно, и проблема больше не будет проявляться.