---
title: Получить информацию о глобальных значениях, влияющих на используемую mysql кодировку
authors: 
 - glowingsword
tags:
 - MySQL
 - Полезные запросы MySQL
date: 2020-04-04
---
# Получить информацию о глобальных значениях, влияющих на используемую mysql кодировку
Глобальное значение

``` mysql
SHOW GLOBAL VARIABLES LIKE  "char%";
```

``` mysql
SHOW  VARIABLES LIKE  "char%";
```