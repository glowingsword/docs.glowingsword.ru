---
title: 'Получаем uuid, partuuid и hints_string раздела с помощью grub_probe'
authors: 
 - glowingsword
tags:
 - Linux
 - grub2
date: 2020-04-04
---

Легенда: к примеру, у нас есть загрузчик другой ОС на втором диске, мы хотим его добавить в меню Grub, но для этого нам нужно получить информацию о разделе.

Создаём временный каталог, куда монтируем наш раздел

```bash
mkdir /tmp/sda1
```
```bash
mount /dev/sda1 /tmp/sda1/
```
Получаем UUID ФС раздела aka fs_uuid в grub2

```bash
grub-probe --target=fs_uuid /tmp/sda1/EFI/Microsoft/Boot/bootmgfw.efi
```
Получаем PARTUUID раздела aka partuuid в grub2

```bash
grub-probe --target=partuuid /tmp/sda1/EFI/Microsoft/Boot/bootmgfw.efi 
```
Получаем hints_string

```bash
grub-probe --target=hints_string /tmp/sda1/EFI/Microsoft/Boot/bootmgfw.efi
```
Первые два значения можно получить и с помощью lsblk, так

```bash
lsblk -o NAME,UUID,PARTUUID
```
сопоставив нужны NAME(device в терминологии grub2) с соответствующими ему UUID и PARTUUID. Но, если lsblk в системе нет, а grub-probe есть – можно все три значения получить с помощью последнего.

В конце не забываем 

```bash
umount /dev/sda1
```
```bash
rmdir /tmp/sda1
```
так как в приличном обществе принято убирать за собой, не оставляя мусора в системе.