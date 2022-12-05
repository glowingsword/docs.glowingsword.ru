---
title: 'Ошибка вида "Error: Could not load database file mysql!" на сайтах с OpenCart после переноса'
authors: 
 - glowingsword
tags:
 - CMS
 - 'OpenCart'
date: 2020-06-14
---

# Ошибка вида "Error: Could not load database file mysql!" на сайтах с OpenCart после переноса

Проверяем значение DIR_DATABASE. Если в config.php и admin/config.php данное значение отличается от корректного, исправляем путь к соответствующему каталогу. 
 
Если оно не указано, добавляем соответствующую строку вида

define('DIR_DATABASE', '/some/path/public_html/system/database/');

где путь /some/path/public_html/system/database/ состонит из пути к домашнему каталогу сайта(www-root) вида /some/path/public_html/ и относительно пути вида system/database/ к каталогу database вашего сайта на движке OpenCart.