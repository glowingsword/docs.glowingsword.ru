---
title: 'Ошибка \"Поле \'Почтовые ящики\' имеет недопустимое значение\" на ISPManager 5'
authors: 
 - glowingsword
tags:
 - ISPManager 5
date: 2021-03-22
---

# Ошибка "Поле 'Почтовые ящики' имеет недопустимое значение" на ISPManager 5

Причин появления ошибки несколько:
1. Ящик удалили, mailbox-каталога уже нет, а запись о нём в dovecot.passwd осталась.
2. Каталог ящика на месте, но у учётной записи владельца ящика забилась дисковая квота.

Находим проблемный ящик 

```bash
/usr/bin/doveadm quota get -A | egrep -v "STORAGE|MESSAGE"
```

если видим сообщения вида


```bash
doveadm(admin@domain.example): Error: write_full(/var/www/u1234567/data/email/domain.example/admin/.maildir/maildirsizeourgood.server.31383.73e519672ce25b51) failed: Disk quota exceeded
doveadm(admin@domain.example): Error: write_full(/var/www/u1234567/data/email/domain.example/admin/.maildir/maildirsizeourgood.server.31383.f9447c4a678e2a72) failed: Disk quota exceeded
```

у нас просто забилась квота у клиента. Для решения проблемы необходимо или подчистить старые, не нужные логи, или клиенту квоту временно поднять и уведомить его, что нужно повышать ТП или чистить дисковое.

Если в результате работы команды "doveadm quota get -A" видим ошибки, связанные с "Initialization failed", и отсылкой к отсутствию нужного каталога .maildir и отсутствием возможности его создать(нет учётки соответсвующего пользователя на сервере, нет каталога /var/www/u1234567/data/email у этого пользователя) – мы имеем дело с ситуацией, когда пользователь-владелец ящика был удалён с сервера(смигрировали, или удалили), а записи в dovecot.passwd для ящиков данного пользователя остались. Редко, но бывает, что по какой-то причине панель забывает подчищать за собой эти записи.

Для решения проблемы удаляем запись о проблемном ящике из  dovecot.passwd, повторно проверяем выхлоп 

```bash
/usr/bin/doveadm quota get -A | egrep -v "STORAGE|MESSAGE"
```

строк с ошибками в нём быть не должно.

Если адресов много, то можно сделать так

```bash
for i in 1@emai.ru 2@email.ru 3@email.ru;do sed -i "/$i/d" /etc/dovecot/dovecot.passwd;done
```

где ==1@emai.ru==, ==2@email.ru==, ==3@email.ru== – какие-то адреса. 

Перед этим желательно ==dovecot.passwd== себе куда-то закинуть в качестве бэкапа.

Получить список адресов можно так

```bash
/usr/bin/doveadm quota get -A 2>&1| egrep -v "STORAGE|MESSAGE"|grep 'Initialization failed'|awk '{print $4}'
```

После чего проблема перестаёт проявляться.