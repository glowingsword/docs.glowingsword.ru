 ---
title: "Установка ionCube Loader на VPS с Centos, Debian или Ubuntu"
authors: 
 - glowingsword
tags:
 - PHP
 - 'ISPManager 4'
date: 2022-07-22
---
 # Не работает  PHP как модуль Apache на VPS с ISPManager 4  на Debian или Ubuntu
 
Для решения проблемы необходимов в текстовом редакторе открыть файл **/etc/apache2/mods-available/php5.conf**

```bash
vim /etc/apache2/mods-available/php5.conf
```
и закомментировать строки вида

```httpdconf
<FilesMatch ".+\.ph(p[345]?|t|tml)$">
    SetHandler application/x-httpd-php
</FilesMatch>
```

после через перезапустить apache2

``` bash
service apache2 restart
```