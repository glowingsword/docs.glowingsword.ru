---
title: 'Создание RAID-1 или RAID-10 массива на  LSI 9271-4 с помощью megacli'
authors: 
 - glowingsword
tags:
 - RAID
 - LSI
date: 2021-01-05
---

# Создание RAID-1 или RAID-10 массива на  LSI 9271-4 с помощью megacli

Так как контроллеры LSI 9271-4 юзают GUI(вместо TUI как у хороших контроллеров вроде  LSI 9361-4i), для которого не работает мышь в IPMI Supermicro(нет нужного драйвера в прошивке RAID-контроллера?), создать массив RAID-1/RAID-10(в зависимости от ситуации) на серверах Supermicro с таким контроллером можно только с помощью аппаратного KVM, или с помощью IPMI и загрузочного диска с утилитой megacli.

Убеждаемся, что массива нет, так

```bash
megacli  -LDInfo -L0 -a0
```

видим что-то вроде

```bash

Adapter 0 -- Virtual Drive Information:
Adapter 0: No Virtual Drive Configured.

Exit Code: 0x00
```

значит его нет, и всё Ok.

Так как нас интересует вариант без использования KVM, загружаемся с диска/флешки, выполняем

```bash
megacli -CfgSpanAdd -r10 -Array0[252:0,252:1] -Array1[252:2,252:3] WT RA Direct NoCachedBadBBU -a0
```
и получаем массив RAID-10 из 4 дисков.

Создаём RAID-1 из двух дисков

```bash
megacli -CfgLdAdd -r1 [252:0,252:1] WT RA Direct NoCachedBadBBU -a0  
```

Даём имя виртуальному диску в соответствии с именем хоста, для которого готовим сервер

```bash
megacli -LDSetProp -Name OurName -L0 -a0
```

Где:
* OurName - имя нашего виртуального хоста(я использую первую часть имени хоста)
* 0 в ==-L0== - номер нашего VD(VDnum)
* 0 в ==-a0== - номер нашего адаптера RAID(AdapterNum), в сложных конфигурациях с большим количеством дисков их может быть несколько в одном сервере.

## Полезная информация
https://www.broadcom.com/support/knowledgebase/1211161499760/lsi-command-line-interface-cross-reference-megacli-vs-twcli-vs-s
https://www.broadcom.com/support/knowledgebase/1211161498596/megacli-cheat-sheet--live-examples