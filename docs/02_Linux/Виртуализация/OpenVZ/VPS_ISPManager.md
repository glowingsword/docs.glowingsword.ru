---
title: 'Не работает квота на VPS с ISPManager'
authors: 
 - glowingsword
tags:
 - 'OpenVZ'
date: 2020-08-21
---

# Не работает квота на VPS с ISPManager

Если в логе ISPmanager видим примерно такое:

```bash
Feb 3 10:37:17 [1040:120] account ERROR Failed to set quota:
'setquota: Cannot stat() mounted device simfs: No such file or directory
setquota: Mountpoint (or device) / not found or has no quota enabled.
setquota: Not all specified mountpoints are using quota.
```

Проверяем, включены ли квоты для / в /etc/fstab

```bash
cat /etc/fstab mount
```
если не включены квоты для корня, включаем. Если включены, а проблема проявляется, то на услуге с ISPmanager 5 выполняем:

```bash
ln -s /simfs /usr/local/mgr5/simfs
```
для ISPmanager 4 выполняем:

```bash
ln -s /simfs /usr/local/ispmgr/simfs
```
Если указанный выше способ проблему не решает, делаем так:

```bash
mv /simfs /simfs_
```
```bash
ln -s /dev/simfs /simfs
```
```bash
unlink /usr/local/mgr5/simfs
```
```bash
ln -s /dev/simfs /usr/local/mgr5/simfs
```
```bash
killall core
```
Если и это не помогло, то значит дело в квотах OpenVZ.

```bash
vzctl stop $CTID
```
```bash
vzquota drop $CTID
```
```bash
vzctl start $CTID
```

## Источник информации по решенид данной проблемы
<https://blog.amet13.name/2016/02/ispmanager-5.html>