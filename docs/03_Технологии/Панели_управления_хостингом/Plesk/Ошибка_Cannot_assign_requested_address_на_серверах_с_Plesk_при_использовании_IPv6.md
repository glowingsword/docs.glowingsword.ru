---
title: 'Ошибка "Cannot assign requested address на серверах с Plesk" при использовании IPv6'
authors:
 - glowingsword
tags:
 - Plesk
date: 2020-04-18
---
# Ошибка Cannot assign requested address на серверах с Plesk при использовании IPv6

Если видим, что на тачке отсутствует валидный IPv6, а в Plesk возникает ошибка
``` bash
Template\_Exception: nginx: \[emerg\] bind() to \[<IPv6>\]:80 failed
(99: Cannot assign requested address)
```
можно просто отключить поддержку проблемного IPv6 для панели.

Отключается IPv6 для Plesk измененим конифгурационного файла `/usr/local/psa/admin/conf/panel.ini`.
Добавляя в конфиг следующие директивы:
``` bash
\[ip\] blacklist="<IPv6>"
```
После чего необходимо перезапустить панель командой
``` bash
/etc/init.d/psa restart
```
После чего пересоздать конфигурационные файлы для сайта(сайтов).

Пересоздание конфигурационных файлов, в зависимости от ситуации, производится командой
``` bash
/usr/local/psa/admin/sbin/httpdmng --reconfigure-all
```
для всех сайтов, командой
``` bash
/usr/local/psa/admin/sbin/httpdmng --reconfigure-domains <список доменов через пробел>
```
для списка доменов, и командой
``` bash
/usr/local/psa/admin/sbin/httpdmng --reconfigure-domain <домен>
```
для одного домена.