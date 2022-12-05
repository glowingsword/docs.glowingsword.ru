---
title: Установка кэшера APC
authors: 
 - glowingsword
tags:
 - PHP
 - Настройка PHP
date: 2020-04-04
---
# Настройка PHP

## mail.log для PHP 5.2 и более старых версий

1. Создаём файл server_vars.php со следующим содержимым:

``` php
<?php
    putenv("HTTP_HOST=".@$_SERVER["HTTP_HOST"]);
    putenv("SCRIPT_NAME=".@$_SERVER["SCRIPT_NAME"]);
    putenv("SCRIPT_FILENAME=".@$_SERVER["SCRIPT_FILENAME"]);
?>
```

2. Создаём файл sendmail.sh со следующим содержимым:

``` bash
#!/bin/bash
echo "$(date) ${SCRIPT_NAME} ${SCRIPT_FILENAME} ${HTTP_HOST}" >> /path/to/mail.log
```

3. Выставляем для php следующие параметры (к примеру, в локальном
php.ini):

``` ini
auto_prepend_file = /path/to/server_vars.php
sendmail_path = /path/to/sendmail.sh
```
