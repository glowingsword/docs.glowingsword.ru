---
title: 'Ошибка Error at offset X при unserialize данных из cookie'
authors: 
 - glowingsword
tags:
 - PHP
date: 2020-12-30
---

При возникновении ошибки 

```php
PHP Notice:  unserialize(): Error at offset 5 of 43 bytes in /var/www/test.php on line 7

```
которая проявляется в процессе десериализации сериализованнорго представления php в коде, использующем $_COOKIE, $_GET или $_POST для получения от клиента сериализованного предствления, вроде следующего кода

```php
$serialized=$_COOKIE['whoiam'];
$_GET += unserialize($serialized);
```

что десериализует представление вида(в таком виде оно хранится на стороне клиента)

```json
a:1:{s:6:"mynick";s:12:"glowingsword";}
```

стоит проверить, что за строка поступает на вход функции unserialize().

Как видно, в примере выше, мы получаем сериализованное представление из $_COOKIE. По идее десериализая должна работать корректно. Но, она не работает.

Пытаемся вывести значение $serialized в скрипте до того, как отдаём его функции unserialize()

```php
$serialized=$_COOKIE['whoiam'];
print_r($serialized);
$_GET += unserialize($serialized);
```

в моём случае я получил

```bash
a:1:{s:6:\"mynick\";s:12:\"glowingsword\";}
```

что странно, ведь мы не экранировали кавычки функцией вроде addslashes().

Вспоминаем, что у старых версий PHP(до PHP 5.4) был такой интересный параметр, как ==magic_quotes_gpc==, который автоматически экранировал кавычки у данных, полученных в GET, POST и COOKIE. 

Если данный параметр выставлен в On в настройках используемой вашими скриптами сборке php – его необходимо выставить в Off.

Проверить его значение можно с помощью простого скрипта phpinfo.php вида 

```bash
<?php 
phpinfo();
?>
```
добавленного в корень сайта. 

Ищем в выхлопе phpinfo() нужный нам параметр ==magic_quotes_gpc==, и если он в ==On==, добавляем в ==php.ini== себе 

```ini
magic_quotes_gpc = Off
```
перезапускаем httpd/apache2/php-fpm/киляем php-cgi нужного юзера (в зависимости от того, какие обработчики вы используете: модуль apache, php-fpm или php-fcgid соответственно), и проверяем что у нас получилось. В результате работы ==phpinfo()== значение параметра ==magic_quotes_gpc== должно быть выставлено в Off, а описанная выше проблема должна перестать проявляться.

Полезные ссылки:
* https://www.php.net/manual/ru/security.magicquotes.what.php
* https://www.php.net/manual/ru/info.configuration.php#ini.magic-quotes-gpc
* https://www.php.net/manual/ru/security.magicquotes.disabling.php


