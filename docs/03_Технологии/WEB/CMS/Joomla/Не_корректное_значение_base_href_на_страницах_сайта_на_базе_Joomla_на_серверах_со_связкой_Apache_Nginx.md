---
title: 'Не корректное значение base href на страницах сайта на базе Joomla на серверах со связкой Nginx + Apache'
authors: 
 - glowingsword
tags:
 - Joomla
date: 2020-04-18
---

# Не корректное значение base href на страницах сайта на базе Joomla на серверах со связкой Nginx + Apache

На серверах со связкой Nginx + Apache бывает, что возникает проблема с ошибкой загрузки смешанного контента. Сама страница сайта отдаётся при этом по безопасному протоколу HTTPS, а подключаемые ресурсы пытаются грузиться по не безопасному HTTP, так же и ссылки на другие разделы сайта могут вести на небезопасный протокол HTTP. Возникает это из-за того, что на старых версиях Joomla значение 'base href' формируется не корректно на серверах со связкой Nginx + Apache + mod_fcgid(вероятно, и другими обработчиками - тоже).

Проблема воникает из-за не корректного значения ==base href==

``` html
curl -s -k <https://some.url> | grep '<base href'
    <base href="http://some.url/" />
```

которое формируется на основе значений переменных 

``` php
$_SERVER['HTTPS'];
$_SERVER['HTTP'];
```

Выдержка из исходного кода Joomla

``` php
// Determine if the request was over SSL (HTTPS). if
(isset($_SERVER['HTTPS']) && !empty($_SERVER['HTTPS']) &&
(strtolower($_SERVER['HTTPS']) != 'off')) {
       $https = 's://';
} else {
      $https = '://';
}
```

Для решения проблемы необходимо установить и настроить корректно настроить mod_rpaf для Apache 2.2.x, или remoteip_module для Apache 2.4. 
Если rpaf старый, его стоит обновить из Git.

---
Полезные материалы по теме:

<http://www.inmotionhosting.com/support/edu/joomla-3/remove-base-tag>
<http://stackoverflow.com/questions/19733229/joomla-base-href-uses-http-instead-of-https>
