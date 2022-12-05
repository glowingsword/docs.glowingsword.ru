---
title: 'ISPManager 4 не отображаются почтовые ящики'
authors: 
 - glowingsword
tags:
 - 'ISPManager 4'
date: 2020-04-06
---
# ISPManager 4 не отображаются почтовые ящики

Как правило, данная проблема возникает в случае, если в процессе создания почтового домена не был указан владелец почтового домена. В результате чего владельцем ящиков указывается пользователь root. Так делать не рекомендуется, при создании почтового домена необходимо сразу корректно указать пользователя, который будет владельцем почтового домена.

Для решения данной проблемы необходимо проверить корректность путей к почтовым ящикам в файле /etc/dovecotdovecot.passwd и при необходимости корректировать их, а также скорректировать значения uid и gid.

Пример содержимого dovecot.passwd до исправления
``` bash
-bash-4.1# 
```
``` bash
cat dovecot.passwd
```
Видим выхлоп
```
admin@localhost.com:$1$oC.rOaaJ$hVQuB5Cd8ttTZdHWvvRZA1:0:0::/root/email/localhost.commail/localhost.com/admin:::maildir:/var/www/user1/data/email/localhost.com/admin/.maildir
```
и после
``` bash
cat dovecot.passwd
```
```
admin@localhost.com:$1$oC.rOaaJ$hVQuB5Cd8ttTZdHWvvRZA1:501:502::/var/www/user1/data/email/localhost.com/admin:::maildir:/var/www/user1/data/email/locahost.com/admin/.maildir
```
Кроме того, важно убедиться что выбранный нами пользователь указан в качестве владельца домашнего каталога ящика, и вложенных файлов и каталогов. 
При необходимости указываем корректного владельца.

Исправил командой
``` bash 
chown -R kirildm: /var/www/user1/data/email/localhost.com
```
Перезапустил dovecot и ispmanager командами
``` bash
service dovecot restart
```
``` bash 
killall ispmgr
```
После чего все почтовые ящики должны начать отображаться корректно.