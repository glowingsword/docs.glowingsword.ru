---
title: Ошибка ERR CONTENT DECODING FAILED на сайте с CMS Joomla
authors: 
 - glowingsword
tags:
 - CMS
 - Joomla
date: 2020-04-04
---
# Ошибка ERR CONTENT DECODING FAILED на сайте с CMS Joomla

Ошибка ERR CONTENT DECODING FAILED на сайте с CMS Joomla возникает из-за включенного в настройках сайта сжатия Gzip. 
Для решения данной проблемы в файле configuration.php сайта необходимо строку

``` php
        public $gzip = '1';
```

заменить на

``` php
        public $gzip = '0';
```
