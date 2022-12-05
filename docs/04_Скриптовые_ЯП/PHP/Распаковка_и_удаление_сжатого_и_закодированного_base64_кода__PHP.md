---
title: Распаковка и удаление сжатого и закодированного base64 кода PHP
authors: 
 - glowingsword
tags:
 - PHP
 - Деобфусцирование PHP
date: 2020-04-04
---

# Распаковка и удаление сжатого и закодированного base64 кода PHP
## Распаковываем код, сжатый при помощи gzinflate и base64

``` php
<?php
echo gzinflate( base64_decode( /* insert code */ ));
?>
```
## Распаковываем код, сжатый при помощи gzuncompress и base64

``` php
<?php
echo gzuncompress( base64_decode( /* insert code */ ));
?>
```
## Удаляем код, сжатый при помощи gzinflate и base64 из файлов

``` bash
find -name "*.php" -exec sed -i '/<?.*eval(gzinflate(base64.*?>/ d' '{}' \; -print
```
