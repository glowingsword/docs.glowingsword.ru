---
title: 'Решаем проблему с не доступными данными сенсоров PSU в ipmitool на серверах Supermicro'
authors: 
 - glowingsword
tags:
 - Supermicro
date: 2021-12-30
---

# Решаем проблему с не доступными данными сенсоров PSU в ipmitool на серверах Supermicro

Если после ребута сервера команда 

```bash
/usr/bin/ipmitool sensor|grep psu
```

возвращает

```bash
No data available
Get Device ID command failed
```

делаем

```bash
systemctl stop ipmievd
```
```bash
rmmod ipmi_si ipmi_devintf
```
```bash
modprobe ipmi_devintf ipmi_si
```
```bash
systemctl start ipmievd
```

Проверяем

```bash
/usr/bin/ipmitool sensor
```

если после этого ещё наблюдается проблема, выполняем 

```bash
/usr/bin/ipmitool bmc reset cold
```
