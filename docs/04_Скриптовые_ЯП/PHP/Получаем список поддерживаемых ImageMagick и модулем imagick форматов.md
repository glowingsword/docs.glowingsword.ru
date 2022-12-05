---
title: 'Получаем список поддерживаемых ImageMagick и модулем imagick форматов'
authors: 
 - glowingsword
tags:
 - PHP
date: 2021-06-07
---

Выполняем

```bash
php -r "print_r(Imagick::queryFormats());"
```

и видим форматы, что поддерживает ImageMagick с соответствующим модулем на вашем сервере.