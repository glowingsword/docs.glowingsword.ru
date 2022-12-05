---
title: 'Ищем зону с ошибками, из-за которой не стартует named на Centos 7'
authors: 
 - glowingsword
tags:
 - DNS
date: 2021-09-01
---

Ищем проблемную зону, что не грузится

```bash
/usr/sbin/named-checkconf -z /etc/named.conf|grep -i error
```

к примеру, этоу нас example.domain.

Проверяем файл зоны на ошибки

```
named-checkzone  example.domain /var/named/example.domain
```

Видим что-то вроде 

```bash
/var/named/example.domain:21: warning: _minecraft._tcp: bad name (check-names)
zone dk-p.ru/IN: mc.example.domain/SRV '_minecraft._tcp' (out of zone) has no addresses records (A or AAAA)
```

Исправляем(или, по обстоятельствам, удаляем) проблемную запись. Перезапускаем named 

```bash
systemctl start named
```
и named запускается успешно. Бывает, что не запускается, так как битая зона была не одна. Ищем проблемную зону, ищем в ней ошибки, исправляем. И так, по кругу, пока все проблемные записи в не загружавшихся зона не будут исправлены.