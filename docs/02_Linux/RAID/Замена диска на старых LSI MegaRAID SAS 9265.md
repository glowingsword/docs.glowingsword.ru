
К примеру, мы заменили диск 

Device at Enclosure 21, Slot 3

После замены диска видим

 Firmware state: Unconfigured(good), Spun Up

 смотрим на выхлоп вида

 megacli -CfgDsply -a0|grep -e 'Slot Number:' -e 'Physical Disk:'

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

сопоставляем все диски с одним Physical Disk, группируя по слотам

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

Как видно, у нас 1 диск в Physical Disk: 3, у остальных подключен по два диска(смотрим по слотам).

Делаем

  megacli -CfgDsply -a0|grep -e 'Slot Number' -e 'Drive.* postion: DiskGroup:'

Видим что-то вроде

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

Наш отсутствующий диск имел бы запись

Slot Number: 3
Drive's postion: DiskGroup: 0, Span: 0, Arm: 3

так как парный ему диск из Span: 1 имеет запись

Drive's postion: DiskGroup: 0, Span: 1, Arm: 3

где DiskGroup и Arm у дисков совпадают, отличается только Span.

Выполняем 

megacli -PdReplaceMissing -PhysDrv[21:3] -array0 -row3 -a0

Если сторонних масивов нет, и новый диск в состоянии Unconfigured(good), вместо PdReplaceMissing, технически, можно выполнить

/opt/MegaRAID/storcli/storcli64 /c0/e21/s3 insert dg=0 array=0 row=3

Эта команда добавляет диск /c0/e21/s3 в DiskGroup: 0, Span: 1, Arm: 3.

Там такое соответствие параметров получается:

dg - DiskGroup
array – Span
row – Arm

Запускаем ребилд для диска, полключенного к третьему слоту

megacli -pdrbld -start -physdrv [21:3] -a0

Наблюдаем за прогрессом с помощью

megacli -pdrbld -showprog -physdrv [21:3] -a0

https://skeletor.org.ua/?p=4093
http://erikimh.com/megacli-cheatsheet/
http://linux-bash.ru/menudisk/113-megacli.html
https://serveradmin.ru/zamena-diska-v-reyde-s-pomoshhyu-magacli-na-kontrollere-perc-h700/
https://wikitech.wikimedia.org/wiki/MegaCli#Manually_array_rebuild_with_an_used_disk
