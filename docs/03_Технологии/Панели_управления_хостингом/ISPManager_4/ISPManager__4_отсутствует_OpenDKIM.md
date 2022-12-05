---
title: 'ISPManager отсутствует OpenDKIM'
authors: 
 - glowingsword
tags:
 - 'ISPManager 4'
 - DKIM
date: 2020-04-04
---
# ISPManager отсутствует OpenDKIM

Фиксми проблему с недоступностью epel  

``` bash
 yum --disablerepo="epel" update nss
 
```

Решаем проблему возникновения ошибки corrupt-rpmdb-recover

``` bash
 rm  /var/lib/rpm/__db.00*
 rpm --rebuilddb
 yum clean all
 rpm -qa | wc -l
```

Ставим ручками opendkim

``` bash
 yum install opendkim
```

Если возникает ошибка Не удалось получить список доступных приложений
Проверяем наличие нужного файла

``` bash
 ls /usr/local/ispmgr/etc/pkg-ispmgr.conf
```

Если файл есть, чистим кэш pkgctl

``` bash
   /usr/local/ispmgr/sbin/pkgctl -D cache
   killall -9 -r ispmgr
   /usr/local/ispmgr/sbin/pkgctl activate opendkim
```

Dkim в панели появляется.