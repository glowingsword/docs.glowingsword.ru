---
title: Решение проблемы с лицензией ISPManager 5
authors: 
 - glowingsword
tags:
 - ISPManager
 - ISPManager 5
date: 2020-04-04
---
# Решение проблемы с лицензией ISPManager 5

Переименовываем файл /usr/local/mgr5/etc/ispmgr.lic в /usr/local/mgr5/etc/ispmgr.lic_old после чего скачиваем заново лицензию командой
``` bash
wget -O /usr/local/mgr5/etc/ispmgr.lic
<http://lic.ispsystem.com/ispmgr.lic?ip=123.123.123.123>
```
и убиваем процесс core
``` bash
killall -9 core
```
если не помогает, делаем
``` bash
/usr/local/mgr5/sbin/licctl fetch ispmgr
```
После чего лицензия должна подхватиться панелькой.

Если сообщение об отсутствии лицензии или необходимости активации
продолжает отображаться, выполняем
``` bash
/usr/local/mgr5/sbin/licctl list
```
и смотрим состояние лицензии, если оно имеет вид
``` json
ispmgr.lic bad format
```
значит скорее всего файл лицензии не валидный, или версия панели
отличается от той, для которой был выпущен файл лицензии. 

Получаем редакцию панели ISPManager 5 с помощью команды
``` bash
/usr/local/mgr5/bin/core ispmgr -F 
```
Видим что-то вроде 
```
ISPmanager Lite
```

Получаем номер версии панели ISPManager 5 командой
``` bash
/usr/local/mgr5/bin/core ispmgr -v
```
Видим что-то вроде
```
 5.31.1
```
Информация о лицензии
``` bash
/usr/local/mgr5/sbin/licctl info /usr/local/mgr5/etc/ispmgr.lic
```
Если у клиента заблокирована сеть, дополнительно необходимо добавить в
iptables на хосте следующие правила

``` bash
IP=123.123.123.123 
iptables -I vpsctl 1 -s $IP -d 82.146.40.41 -p tcp -j ACCEPT 
iptables -I vpsctl 1 -s $IP -d 62.109.29.191 -p tcp -j ACCEPT
iptables -I vpsctl 1 -s $IP -d 212.109.222.131 -p tcp -j ACCEPT 
iptables -I vpsctl 1 -s $IP -d 144.76.174.134 -p tcp -j ACCEPT
```
и сохранить их на случай перезагрузки.