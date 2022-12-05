---
title: 'Изменяем настройки Memcache в конфигах Bitrix'
authors: 
 - glowingsword
tags:
 - CMS
 - Bitrix
date: 2020-10-16
---

Открываем в текстовом редакторе файл 
```bash
vim ./bitrix/.settings_extra.php
```
и редактируем блок

```php
'memcache' => array(
    'host' => '127.0.0.1',
    'port' => '11212',
),
```

где host – адрес хоста, где расположен наш Memcache, а port – порт, на котором висит наш Memcache.

Затем открываем

```bash
 vim ./bitrix/php_interface/dbconn.php
```

и редактируем 

```php
define("BX_MEMCACHE_HOST", "127.0.0.1");
define("BX_MEMCACHE_PORT", "11212");
```
где BX_MEMCACHE_HOST – адрес хоста с Memcache, а BX_MEMCACHE_PORT – номер порта.