
Выводим краткую информацию об имеющихся контроллерах

storcli64 show all

Выводим детальную информацию об имеющихся контроллерах

storcli64 show all

Получаем список виртуальных дисков для каждого контроллера

storcli64 /c0 /vall show

!!! info "Внимание"
    Именно эти вирутальные диски в ОС мы видим как блочные устройства sda, sdb, sdc и т.п. в ОС Linux. Физические же жётские диски, входящие в RAID, находятся уровнем ниже, управляются RAID-контроллером, и ОС с ними напрямую не взаимодействует.

Смотрим на физические диски

storcli64 /c0 /eall /sall show

Смотрим информацию о топологии виртуальных дисков(Drive Group) 

storcli /cx/dall show

или более подробная информация

storcli /c0/dall show all

Видим там таблицу вида 

```r
-----------------------------------------------------------------------------
DG Arr Row EID:Slot DID Type  State BT       Size PDC  PI SED DS3  FSpace TR 
-----------------------------------------------------------------------------
 0 -   -   -        -   RAID1 Dgrd  N   893.25 GB dflt N  N   none N      N  
 0 0   -   -        -   RAID1 Dgrd  N   893.25 GB dflt N  N   none N      N  
 0 0   0   252:0    4   DRIVE Onln  N  446.625 GB dflt N  N   none -      N  
 0 0   1   252:1    5   DRIVE Onln  N  446.625 GB dflt N  N   none -      N  
 0 0   2   252:2    6   DRIVE Onln  N  446.625 GB dflt N  N   none -      N  
 0 0   3   252:3    7   DRIVE Rbld  Y  446.625 GB dflt N  N   none -      N  
-----------------------------------------------------------------------------
```

где колонка DG указывает на группу дисков(DiskGroup), Arr(Array) – на дисковые массивы, Row в терминологии megacli был известен как Arm, EID(Enclosure Device ID) и Slot(Slot Number), DID(Device Id).

Отображаем все ребилды на конкретном контроллере

storcli64 /c0 /eall /sall show rebuild

Смотрим на ребилд конкретного диска

storcli64 /c0 /e8 /s4 show rebuild


Смотрим информацию о конкретном диске

/opt/MegaRAID/storcli/storcli64 /c0/e252/s3 show 

и подробную, с SN диска

/opt/MegaRAID/storcli/storcli64 /c0/e252/s3 show  all

Смотрим информацию обо всех дисках

/opt/MegaRAID/storcli/storcli64 /c0/eall/sall show all

Смотрим информацию о событиях, в том числе об SN вылетевшего диска

/opt/MegaRAID/storcli64 /c0 show events

# https://www.broadcom.com/support/knowledgebase/1211161499760/lsi-command-line-interface-cross-reference-megacli-vs-twcli-vs-s