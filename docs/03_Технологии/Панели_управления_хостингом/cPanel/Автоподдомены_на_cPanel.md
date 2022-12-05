---
title: Автоподдомены на cPanel
authors: 
 - glowingsword
tags:
 - cPanel
 - phpMyAdmin
date: 2020-04-04
---
# Автоподдомены на cPanel

Функция автоподдоменов в cPanel реализована автоматически и ее нельзя
отключить. Для создания автоподдомена достаточно добавить в ресурсные
записи основного домена запись:

``` bash
 *      ip-address 
```

или

``` bash
subdomain.domain.ru     ip-address.
```

После этого достаточно создать папку subdomain в public\_html и
поместить в нее файлы сайта.