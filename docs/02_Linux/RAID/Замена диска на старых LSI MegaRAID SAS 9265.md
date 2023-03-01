---
title: 'Замена диска на старых LSI MegaRAID SAS 9265'
authors: 
 - glowingsword
tags:
 - RAID
 - LSI
date: 2023-03-01
---

# Замена диска на старых LSI MegaRAID SAS 9265

Замена дисков на LSI MegaRAID SAS 9265 имеет одну неприятную особенность, этот контроллер не запускает авто-ребилд при замене диска.
Ребилд на нём нужно запускать вручную, после замены диска.

## Убеждаемся, что заменённый диск виден

К примеру, мы заменили диск 

```
Device at Enclosure 21, Slot 3
```
После замены диска видим
```
Firmware state: Unconfigured(good), Spun Up
```

## Ищем Slot Number и Physical Disk нашего заменённого диска

Cмотрим на результат выполнения команды
```bash
megacli -CfgDsply -a0|grep -e 'Slot Number:' -e 'Physical Disk:'
```
видим что-то вроде

```r
Physical Disk: 0
Slot Number: 0
Physical Disk: 1
Slot Number: 1
Physical Disk: 2
Slot Number: 2
Physical Disk: 3
Physical Disk: 4
Slot Number: 4
Physical Disk: 5
Slot Number: 5
Physical Disk: 0
Slot Number: 6
Physical Disk: 1
Slot Number: 7
Physical Disk: 2
Slot Number: 8
Physical Disk: 3
Slot Number: 9
Physical Disk: 4
Slot Number: 10
Physical Disk: 5
Slot Number: 11
```

Cопоставляем все диски с одним Physical Disk, группируя по слотам

```r
Physical Disk: 0
Slot Number: 0
Slot Number: 6

Physical Disk: 1
Slot Number: 1
Slot Number: 7

Physical Disk: 2
Slot Number: 2
Slot Number: 8

Physical Disk: 3
Slot Number: 9

Physical Disk: 4
Slot Number: 4
Slot Number: 10

Physical Disk: 5
Slot Number: 5
Slot Number: 11
```

Как видно, у нас 1 диск в Physical Disk: 3, у остальных подключен по два диска(смотрим по слотам).

Делаем
```bash
megacli -CfgDsply -a0|grep -e 'Slot Number' -e 'Drive.* postion: DiskGroup:'
```
Видим что-то вроде
```yaml
Slot Number: 0
Drive's postion: DiskGroup: 0, Span: 0, Arm: 0
Slot Number: 1
Drive's postion: DiskGroup: 0, Span: 0, Arm: 1
Slot Number: 2
Drive's postion: DiskGroup: 0, Span: 0, Arm: 2
Slot Number: 4
Drive's postion: DiskGroup: 0, Span: 0, Arm: 4
Slot Number: 5
Drive's postion: DiskGroup: 0, Span: 0, Arm: 5
Slot Number: 6
Drive's postion: DiskGroup: 0, Span: 1, Arm: 0
Slot Number: 7
Drive's postion: DiskGroup: 0, Span: 1, Arm: 1
Slot Number: 8
Drive's postion: DiskGroup: 0, Span: 1, Arm: 2
Slot Number: 9
Drive's postion: DiskGroup: 0, Span: 1, Arm: 3
Slot Number: 10
Drive's postion: DiskGroup: 0, Span: 1, Arm: 4
Slot Number: 11
Drive's postion: DiskGroup: 0, Span: 1, Arm: 5
```

Наш отсутствующий диск имел бы запись
```yaml
Slot Number: 3
Drive's postion: DiskGroup: 0, Span: 0, Arm: 3
```
так как парный ему диск из Span: 1 имеет запись
```yaml
Drive's postion: DiskGroup: 0, Span: 1, Arm: 3
```
где DiskGroup и Arm у дисков совпадают, отличается только Span.

## Возвращаем диск в Unconfigured(good) на место изъятого диска в настройках контроллера

Выполняем

```bash
megacli -PdReplaceMissing -PhysDrv[21:3] -array0 -row3 -a0
```

Если сторонних масивов нет, и новый диск в состоянии Unconfigured(good), вместо PdReplaceMissing, технически, можно выполнить

```bash
/opt/MegaRAID/storcli/storcli64 /c0/e21/s3 insert dg=0 array=0 row=3
```
Эта команда добавляет диск ```/c0/e21/s3``` в ```DiskGroup: 0, Span: 1, Arm: 3```.

Где у нас получается такое соответствие параметров:
```r
dg - DiskGroup
array – Span
row – Arm
```

## Запуск ребилда после возвращения диска на место изъятого ранее

Запускаем ребилд для диска, подключенного к третьему слоту

```bash
megacli -pdrbld -start -physdrv [21:3] -a0
```
## Следим за окончанием ребилда

Наблюдаем за прогрессом с помощью

```bash
watch -n 3 'megacli -pdrbld -showprog -physdrv [21:3] -a0'
```

## Дополнительная полезная информация
https://skeletor.org.ua/?p=4093
http://erikimh.com/megacli-cheatsheet/
http://linux-bash.ru/menudisk/113-megacli.html
https://serveradmin.ru/zamena-diska-v-reyde-s-pomoshhyu-magacli-na-kontrollere-perc-h700/
https://wikitech.wikimedia.org/wiki/MegaCli#Manually_array_rebuild_with_an_used_disk
