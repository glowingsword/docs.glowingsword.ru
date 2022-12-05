---
title: Настройка logrotate для atop
authors: 
 - glowingsword
tags:
 - Logrotate
 - логи
 - ротация логов
date: 2020-04-04
---
# Настройка logrotate для atop

Если отсутствует, добавляем в /etc/cron.daily/ скрипт /etc/cron.daily/logrotate

``` bash
  vim /etc/cron.daily/logrotate
```

следующего содержания

``` bash
#!/bin/sh

/usr/sbin/logrotate /etc/logrotate.conf >/dev/null 2>&1
EXITVALUE=$?
if [ $EXITVALUE != 0 ]; then
    /usr/bin/logger -t logrotate "ALERT exited abnormally with [$EXITVALUE]"
fi
exit 0
```

Создаём кофиг для настройки ротации логов atop

``` bash
  vim /etc/logrotate.d/atop
```

следующего содержания

``` yaml
/var/log/atop/*.log
/var/log/atop/atop.log {
    missingok
    daily
    rotate 2
    notifempty
    create 0600 root root
}
```

Проверка работы logrotate

``` bash
/usr/sbin/logrotate --debug /etc/logrotate.conf
```
