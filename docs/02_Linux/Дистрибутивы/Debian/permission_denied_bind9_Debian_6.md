---
title: 'Ошибка "none:0: open: /etc/bind/named.conf: permission denied" при запуске bind9 на Debian 6'
authors: 
 - glowingsword
tags:
 - Debian
date: 2020-04-05
---
# Ошибка "none:0: open: /etc/bind/named.conf: permission denied" при запуске bind9 на Debian 6

Проблема возникала из-за не корректных прав доступа на каталог ==/etc/named==
``` bash
root@mx:\~\# ls -ld /etc/bind 
drw-r--r-- 3 root bind 4096 Nov 2 13:37 /etc/bind
```
что приводило к ошибке вида
!!! failure
   ``` bash
   open(/etc/bind/named.conf, O\_RDONLY\|O\_LARGEFILE) = -1 EACCES (Permission denied)
   ```

в трейсе, а также к

!!! failure
   ``` bash 
   none:0: open: /etc/bind/named.conf: permission denied 
   ```
в консоли при запуске bind вручную командой
``` bash
/usr/sbin/named -fg -u bind -d 10
```
и

!!! failure!!! failure
    ``` bash
    Nov 2 14:34:08 mx named\[17948\]: none:0: open: /etc/bind/named.conf: permission denied
    ```

в ==syslog== при запуске службы ==bind9==.

Cменил права на каталог ==/etc/bind== на корректные
``` bash
chmod 775 /etc/bind
```
после чего bind успешно запустился
``` bash
root@mx:\~\# /etc/init.d/bind9 start 
Starting domain name service...: bind9. 
root@mx:\~\# /etc/init.d/bind9 status bind9 is running.
```