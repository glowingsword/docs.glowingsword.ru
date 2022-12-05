---
title: Узнаём версию CMF Drupal
authors: 
 - glowingsword
tags:
 - CMS
 - Drupal
date: 2020-04-04
---
# Узнаём версию CMF

Переходим в хомяк сайта на Drupal и выполняем

``` bash
cat modules/system/system.info|grep version
```