---
title: 'Декодируем utf7 в utf8 и обратно и переименовываем каталоги с помощью doveadm'
authors: 
 - glowingsword
tags:
 - почта
date: 2021-12-04
---

# Декодируем utf7 в utf8 и обратно и переименовываем каталоги с помощью doveadm

Имея utf8 получаем  строку в представлении utf7

```bash
doveadm mailbox mutf7 -8 "my@test.domain INBOX.Тест"
```

получаем
```bash
my@test.domain INBOX.&BCIENQRBBEI-
```
Наоборот
```bash
doveadm mailbox mutf7 -7 "my@test.domain INBOX.&BCIENQRBBEI-"
```

получаем
```bash
my@test.domain INBOX.Тест
```
Переименовываем каталог

```bash
doveadm mailbox rename -u $user -s "$utf8_mailbox_name" "$utf7_mailbox_name"
```

Важно: если каталог переименовываем с utf8 в utf7, на момент переименования в выхлопе 

```bash
dovecot user mailuser@example.domain
```

должна присутствовать строка

```bash
mail    maildir:/var/qmail/mailnames/example.domain/mailuser/Maildir:UTF-8
```

а не 

```bash
mail    maildir:/var/qmail/mailnames/example.domain/mailuser/Maildir
```

Если это не так, перед переименованием редактируем /etc/dovecot/users, заменяем строку

```r
mailuser@example.domain:!:10236:30::/var/qmail/mailnames/example.domain/mailuser
```

на

```r
mailuser@example.domain:!:10236:30::/var/qmail/mailnames/example.domain/mailuser::userdb_mail=maildir:/var/qmail/mailnames/example.domain/mailuser/Maildir:UTF-8
```

делаем 

```bash
systemctl reload dovecot
```

и после этого переименовываем.

## Полезная информация 
https://dovecot.org/list/dovecot/2016-July/105077.html
https://wiki.dovecot.org/Tools/Doveadm/Mailbox