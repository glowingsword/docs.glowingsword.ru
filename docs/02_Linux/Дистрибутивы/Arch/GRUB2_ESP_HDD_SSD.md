---
title: Установка GRUB2 на второй ESP на запасном HDD или SSD
authors: 
 - glowingsword
tags:
 - Arch
 - GRUB2
date: 2020-04-04
---

# Установка GRUB2 на второй ESP на запасном HDD или SSD

``` bash
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=arch-ssd-encrypted --boot-directory=/boot/ --debug --recheck /dev/sdb
```