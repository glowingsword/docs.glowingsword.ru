---
title: Получение информации о версии joomla
authors: 
 - glowingsword
tags:
 - CMS
 - Joomla
date: 2020-04-04
---
# Получение информации о версии joomla

``` bash
grep -R "public.*\$RELEASE.=" /var/www/u0009378/data/www/kosmetolog-kemerovo.ru/includes/version.php -C 3
```

результатом работы данной команды будет примерно следующее

``` php
    public $PRODUCT = 'Joomla!';

    /** @var  string  Release version. */
    public $RELEASE = '1.7';

    /** @var  string  Maintenance version. */
    public $DEV_LEVEL = '3';
```
