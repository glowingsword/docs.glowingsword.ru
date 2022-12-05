---
title:  "Ищем планку с битой оперативой на серверах SuperMicro на Centos 7"
authors: 
 - glowingsword
tags:
 - SuperMicro
date: 2021-02-03
---

# Ищем планку с битой оперативой на серверах SuperMicro на Centos 7

Для начала определяемся с моделью сервера

dmidecode -t 2|grep 'Product Name\|Version:'
	Product Name: X9DRW
	Version: 0123456789

и ищем для неё мануал вида https://www.supermicro.com/QuickRefs/motherboard/C606_602/QRG-1278.pdf на сайте производителя сервера(компании Supermicro).

Это важно, так как поиск сбойной планки зависит от топологии материнской платы(расположения и наименования слотов на схеме из документа, упомянутого выше).

Теперь, когда у нас есть нужная схема, переходим в каталог /sys/devices/system/edac/mc/, и изучаем каталоги mc0 и mc1 в данном каталоге.

Интересующие нас элементы структуры каталогов

mc0  mc1

где

mc0 - CPU1
mc2 - CPU2

Также у каждого CPU, в свою очередь, есть структура каталогов

mc1/csrow0
mc1/csrow1

где csrow0 и csrow1 - это левая и правая площадки с разъёмами для RAM.

Также у каждой из них есть файл ce_count, позволяющий определить, где искать битую планку

cat mc1/csrow0/ce_count
0

cat mc1/csrow1/ce_count
1701975067

Зная нужную площадку, также можно найти канал, на котором возникают ce errors

for i in ch0_ce_count ch1_ce_count ch2_ce_count ch3_ce_count;do echo $i; cat /sys/devices/system/edac/mc/mc1/csrow1/$i;done
ch0_ce_count
1613090594
ch1_ce_count
0
ch2_ce_count
0
ch3_ce_count
0

Также в каталоге  /sys/devices/system/edac/mc/mc1/ можно найти файлы с наименованием вида dim[\d], где вместо [\d] - какое-то число.

К примеру, в моём случае было так

```bash
dimm0  dimm1  dimm10  dimm3  dimm4  dimm6  dimm7  dimm9
```

каждый из каталогов описывает один один слот для одной планки ОЗУ.

Как видим, у нас 8 планок, что соответствует топологии нашего сервера.

Ищем нужную нам битую планку так:

```bash
for i in dimm0  dimm1  dimm10  dimm3  dimm4  dimm6  dimm7  dimm9;do echo $i;cat /sys/devices/system/edac/mc/mc1/$i/dimm_ce_count;done
dimm0
0
dimm1
1577305852
dimm10
0
dimm3
0
dimm4
0
dimm6
0
dimm7
0
dimm9
0
```


К примеру, у нас выше сбоит dimm1, значит нам нужно узнать его местоположение.

cat /sys/devices/system/edac/mc/mc1/dimm1/dimm_label

Получаем

CPU_SrcID#1_Ha#0_Chan#0_DIMM#1

в принципе, мы и так уже видим по label, где конкретно у нас возникает проблема(Chan#0⇾DIMM#1), что трактуется как 0-й канал и DIMM#1, что, как мы подозревем, память из 1-го слота(счёт от 0). Но, на всякий случай, удостоверяемся, что мы на верном пути.

Узнаём его канал и слот

cat /sys/devices/system/edac/mc/mc1/dimm1/dimm_location

получаем

channel 0 slot 1


Итак, мы видим, что у нас сбоит планка из 0-го(первый если отсчёт от 1) канала у второго CPU.

У первого CPU 4 канала
 
P1-DIMMA - 0-й канал
P1-DIMMB - 1-й канал
P1-DIMMC - 2-й канал
P1-DIMMD - 3-й канал

У второго CPU 4 канала:

P2-DIMME - 0-й канал
P2-DIMMF - 1-й канал
P2-DIMMG - 2-й канал
P2-DIMMH - 3-й канал

Нумерация каналов завязана на буквы латинского алфавита, где чем дальше канал справа по алфавиту, тем больше его порядковый номер(E - 0, а G - уже 3).

2 канала находятся в блоке csrow0, ещё 2 - в csrow1.

В каждом канале у нас по два слота, а соответственно, если нас интересует канал P2-DIMME, нам необхоимо определиться также, какой слот нас интересует.

P2-DIMME1 - 0-й слот
P2-DIMME2 - 1-й слот


Нулевой канал и первый слот - это P2-DIMME2.

Серийник битой памяти можно глянуть так

dmidecode -t memory 

и в выхлопе ищем Memory Device c Locator: P2-DIMME2, к примеру

Memory Device
	Array Handle: 0x004D
	Error Information Handle: Not Provided
	Total Width: 72 bits
	Data Width: 64 bits
	Size: 8192 MB
	Form Factor: DIMM
	Set: None
	Locator: P2-DIMME2
	Bank Locator: P1_Node1_Channel0_Dimm1
	Type: DDR3
	Type Detail: Registered (Buffered)
	Speed: 1333 MT/s
	Manufacturer: Kingston                      
	Serial Number: ED0CCXXY    
	Asset Tag: Dimm1_AssetTag
	Part Number: 9965516-099.A00LF 

При этом сопоставляем Bank Locator: P1_Node1_Channel0_Dimm1 со строкой CPU_SrcID#1_Ha#0_Chan#0_DIMM#1 полученной ранее, видим что CPU_SrcID и P1_Node1 те же, Channel и DIMM - тоже. Теперь мы знаем и серийник проблемной памяти.


https://support.siliconmechanics.com/portal/en/kb/articles/how-to-diagnose-memory-errors-on-amd-x64-using-edac