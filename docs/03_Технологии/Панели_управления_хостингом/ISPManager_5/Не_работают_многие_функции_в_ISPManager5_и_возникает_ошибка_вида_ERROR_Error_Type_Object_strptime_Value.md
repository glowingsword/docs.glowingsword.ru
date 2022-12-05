---
title: "Не работают многие функции в ISPManager5 и возникает ошибка вида ERROR Error: Type: 'date' Object: 'strptime' Value: '"
authors: 
 - glowingsword
tags:
 - ISPManager 5
 - Ошибки ISPManager 5
date: 2020-04-05
---

# Не работают многие функции в ISPManager5 и возникает ошибка вида "ERROR Error: Type: 'date' Object: 'strptime' Value: '"

Если в ISPManager5  не работают многие функции, при этом возникает ошибка "An error occurred while executing the request" при обращении к нужному функционалу, и в лог `/usr/local/mgr5/var/ispmgr.log` падают ошибки вида
``` bash
Jun 27 02:40:01 \[4554:55\] err ERROR Error: Type: 'date' Object:
'strptime' Value: ' Jun 27 02:40:01 \[4554:55\] action EXTINFO Get
message for error in action 'sysinfostat' for level 30 Jun 27 02:40:01
\[4554:55\] action EXTINFO Get message for error in action
'mgrerror\_date' for level 30 Jun 27 02:40:01 \[4554:55\] action EXTINFO
Get message for error in action 'msgerror' for level 30
```

необходимо попытаться синхронизировать время на сервере. 

Если не поможет - то следует закомментировать директиву ExpireLogsDays в файле
`/usr/local/mgr5/etc/ispmgr.conf`, после чего кильнуть панель

``` bash
killall -9 core
```
и проблема перестанет проявляться.
