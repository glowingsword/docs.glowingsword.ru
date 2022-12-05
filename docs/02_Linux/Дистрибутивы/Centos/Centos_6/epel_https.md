---
title:  Устраняем ошибку с недоступностью epel по https
authors: 
 - glowingsword
tags:
 - Centos 6
 - настройка Centos 6
date: 2020-04-04
---
# Устраняем ошибку с недоступностью epel по https

Ошибка вида
``` ini
Error: Cannot retrieve metalink for repository: epel. Please verify its path and try again
```

возникает из-за устаревшей версии пакета nss(ниже версии nss-3.14.3-4.el6\_4).

Ошибка исправляется апдейтом пакета nss.

``` bash
sudo yum --disablerepo="epel" update nss
```