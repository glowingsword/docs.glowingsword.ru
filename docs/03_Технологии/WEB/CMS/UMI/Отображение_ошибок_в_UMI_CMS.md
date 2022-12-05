---
title: Отображение ошибок в UMI CMS
authors: 
 - glowingsword
tags:
 - CMS
 - Joomla
date: 2020-04-04
---
# Отображение ошибок в UMI CMS

В файле congig.ini указываем

``` ini
[debug]
enabled = "1"
show-backtrace = "1"
```

В файл .htaccess добавляем

``` php
php_value error_reporting 8191
```

если не помогло, в начало файла index.php добавляем

``` php
error_reporting(E_ALL|E_STRICT);
ini_set("error_reporting",E_ALL|E_STRICT);
ini_set("display_errors","on");
```