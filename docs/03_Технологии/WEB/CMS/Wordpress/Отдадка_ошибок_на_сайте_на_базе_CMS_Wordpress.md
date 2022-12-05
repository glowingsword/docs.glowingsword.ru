---
title: 'Отладка ошибок на сайте на базе CMS Wordpress'
authors: 
 - glowingsword
tags:
 - CMS
 - Wordpress
date: 2020-04-05
---
# Отладка ошибок на сайте на базе CMS Wordpress

Добавляем в wp-config.php строки вида
``` php
define('WP_DEBUG', true); 
define( 'WP_DEBUG_DISPLAY', true );
define('WP_DEBUG_LOG', true );
```
