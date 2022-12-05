---
title: Узнаём версию Joomla из командной строки
authors: 
 - glowingsword
tags:
 - CMS
 - Joomla
date: 2020-04-04
---
# Узнаём версию Joomla из командной строки

## Joomla 3.x

Для Joomla 3.x используем команду
``` bash
grep -e '$RELEASE' -e '$DEV\_LEVEL' libraries/cms/version/version.php
```

## Joomla 2.x

Для Joomla 2.x используем команду
``` bash
grep '$RELEASE' libraries/joomla/version/version.php
```
## Joomla 1.5.x
``` bash
grep '<version>' language/en-GB/en-GB.xml|awk -F'>\|<' '{print $3}'
```

## Общая информация  о поиске версии Joomla

Информацию ищем в файлах

Joomla! 1.0.x /includes/version.php

Joomla! 1.5.x /libraries/joomla/version.php

Joomla! 1.6.x /libraries/joomla/version.php

Joomla! 2.5.x /libraries/cms/version.php

Joomla! 3.1.x & Joomla! 3.2.x /libraries/cms/version/version.php or top
of /joomla.xml (see the <version /> element)

в зависимости от версии.

## Программный способ определения версии Joomla в скриптах сайта

Также вывести информацию о версии Joomla можно с помощью кода:
var\_dump(JVERSION);