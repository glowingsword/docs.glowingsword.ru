---
title: 'ISPManager отсутствует OpenDKIM'
authors: 
 - glowingsword
tags:
 - 'Dovecot'
 - 'Измение пароля почтового ящика'
date: 2020-04-22
---
# Изменение пароль от почтового ящика на серерах с Dovecot

Меняем пароль с помощью
``` bash
htpasswd /etc/dovecot/dovecot.passwd user
```
или
``` bash
doveadm pw -s CRAM-MD5 -u user
```
где user - почтовый ящик, для которого мувим пароль.
