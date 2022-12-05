---
title: 'Получаем UUID раздела'
authors: 
 - glowingsword
tags:
 - Linux
date: 2020-04-19
---
# Получаем UUID раздела

Используем команду
``` bash
sudo blkid /dev/sda2
```
где `/dev/sda2` - раздел, `UUID` которого нам необходим.