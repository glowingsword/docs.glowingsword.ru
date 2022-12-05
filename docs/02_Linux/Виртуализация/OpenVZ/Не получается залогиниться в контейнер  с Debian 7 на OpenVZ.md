---
title: 'Не получается залогиниться в контейнер с Debian 7 Wheezy на OpenVZ'
authors: 
 - glowingsword
tags:
 - Debian
date: 2021-01-11
---

Если при попытке залогиниться в контейнер мы делаем
```bash
vzctl enter $CTID
```
где в $CTID указан числовой CTID нашего контейнера, к примеру 1010, мы видим что-то сообщение об ошибке вида

```bash
enter into CT 1010 failed
Unable to open pty: No such file or directory
```

Выполняем

```bash
vzctl exec $CTID "cd /dev; /sbin/MAKEDEV pty"
```
```bash
vzctl exec $CTID "cd /dev; /sbin/MAKEDEV tty"
```
```bash
vzctl exec $CTID "cd /dev; /sbin/MAKEDEV pts"
```
после чего опять пробуем войти в консоль контейнера командой

```bash
vzctl enter $CTID
```

на этот раз vzctl enter должен отработь корректно.