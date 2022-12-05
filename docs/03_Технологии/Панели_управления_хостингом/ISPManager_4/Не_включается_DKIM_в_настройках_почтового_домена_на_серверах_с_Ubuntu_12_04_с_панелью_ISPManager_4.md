---
title:  "Не включается DKIM в настройках почтового домена на серверах с Ubuntu 12.04 с панелью ISPManager 4"
authors: 
 - glowingsword
tags:
 - 'ISPManager 4'
 - 'DKIM'
date: 2020-06-04
---
# Не включается DKIM в настройках почтового домена на серверах с Ubuntu 12.04 с панелью ISPManager 4

Проблема с включением dkim возникает из-за ошибки при выполнении команды opendkim-genkey

```bash
Mar 26 18:18:18 [ 7555:8] EXTINFO Execute (/usr/bin/opendkim-genkey -D /etc/exim4/ssl -d test.domain -s dkim -r) return=127 exited
```

которая в свою очередь проявляется из-за того, что в Ubuntu Precise утилиту opendkim-genkey перенесли из opendkim в пакет opendkim-tools, который панелька ISPManager 4 не устанавливает вместе с dkim.  В результате чего выполнение opendkim-genkey завершается не удачно из-за отсутствия необходимой утилиты

```bash
root@testserver:/# /usr/bin/opendkim-genkey -D /etc/exim4/ssl -d test.domain -s dkim -r 
-bash: /usr/bin/opendkim-genkey: No such file or directory
```

Устаналиваем пакет

```bash
apt-get install opendkim-tools
```

после чего проблема перестаёт проявляться.

Подробности:
* https://bugs.launchpad.net/ubuntu/+source/opendkim/+bug/1297080