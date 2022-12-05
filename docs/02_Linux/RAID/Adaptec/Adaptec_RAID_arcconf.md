---
title:  "Управление Adaptec RAID с помощью arcconf"
authors: 
 - glowingsword
tags:
 - Linux
 - Adaptec
date: 2020-07-15
---
# Управление Adaptec RAID с помощью arcconf

Управление Adaptec RAID с помощью arcconf

Смотрим статус рейда

```bash
 /usr/StorMan/arcconf getstatus 1
```
Смотрим лог рейда

```bash
 /usr/StorMan/arcconf getlogs 1 device
```

Смотрим серийники и модель винтов

```bash
/usr/StorMan/arcconf getconfig 1 | grep 'Device \#\|Model\|Serial number'
```

Смотрим состояние винтов(State)

```bash
 /usr/StorMan/arcconf getconfig 1 pd|egrep "Device #|State\>"
```

Понижение приоритета таска на ребилд, если процесс ребилда создавая нагрузку на диски, снижает скорость копирования данных с проблемной тачки на новую

```bash
ARCCONF SETPRIORITY <Controller#> [TASK ID] <New Priority> [current]
```

Где Controller - номер контроллера, не обязательный параметр [TASK ID] — id таска(берём из arcconf getstatus 1), новый приоритет — HIGH, MEDIUM или LOW, и не обязательный параметр [current], указывающий что применяем изменение не к конкретному таску, а к текущим таскам, выполняемым контроллером.

Примеры:

```bash
/usr/StorMan/arcconf setpriority 1 100 LOW
```

```bash
/usr/StorMan/arcconf setpriority 1 LOW current
```

## Остановка задачи на ребилд, если нагрузка не спадает даже при понижении приоритета таски



```bash
TASK STOP <Controller#> DEVICE <Channel#> <ID#>
```

где Controller — номер контроллера, DEVICE — устройство(logicaldrive, к примеру), Channel — канал, ID — Device ID.

Пример

```bash
/usr/StorMan/arcconf task stop 1 logicaldrive 0 0
```




<https://wiki.colobridge.net/%D0%BF%D0%BE%D0%BB%D0%B5%D0%B7%D0%BD%D0%BE%D0%B5/%D1%81%D0%BE%D0%B2%D0%B5%D1%82%D1%8B/%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_raid_adaptec_%D1%81_%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E_arcconf>
<https://wiki.hetzner.de/index.php/Adaptec_RAID_Controller/ru>
<https://www.cyberciti.biz/faq/linux-checking-sas-sata-disks-behind-adaptec-raid-controllers/>

