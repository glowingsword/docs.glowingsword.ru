---
title:  "Смотрим для какой ОС был собран бинарник в формате ELF"
authors: 
 - glowingsword
tags:
 - Linux
 - Полезные команды
date: 2020-06-04
---

# Смотрим для какой ОС был собран бинарник в формате ELF

Выполняем
```bash
readelf -h  <our_bin>
```

где our_bin - путь к интересующему нас бинарнику.

Подробности: <https://greek0.net/elf.html>