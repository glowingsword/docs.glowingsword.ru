---
title: 'Получаем информацию о дисках и разделах из sys и procю'
authors: 
 - glowingsword
tags:
 - 'Disk'
 - 'Partitions'
date: 2021-06-02
---

Информацию о разделах можно получить с помощью

root@scp84 [~]# cat /proc/partitions
major minor  #blocks  name

   8        0 1874329600 sda
   8        1     262144 sda1
   8        2    8388608 sda2
   8        3  928513024 sda3



С какого сектора начинается раздел можно глянуть с помощью

# cat /sys/block/sda/sda1/start     
2048
# cat /sys/block/sda/sda2/start
526336
# cat /sys/block/sda/sda3/start
17303552

Каким разделом является нужный вам раздел в таблице разделов можно глянуть с помощью

root@scp84 [~]# cat /sys/block/sda/sda2/partition 
2

Размер раздела можно посмотреть с помощью 

cat /sys/block/sda/sda2/size
16777216
cat /sys/block/sda/sda3/size
1857026048


   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048      526335      262144   83  Linux
/dev/sda2          526336    17303551     8388608   82  Linux swap / Solaris
/dev/sda3        17303552  3748655294  1865675871+  83  Linux


