---
title: 'Ошибка "Allowed memory size of SOME_NUMBER bytes exhausted (tried to allocate 64 bytes)" на сайтах с Jooomla c $cache_handler не равным files'
authors: 
 - glowingsword
tags:
 - CMS
 - Joomla
date: 2020-05-14
---
# Ошибка "Allowed memory size of SOME_NUMBER bytes exhausted (tried to allocate 64 bytes)" на сайтах с Jooomla c $cache_handler не равным files

Видим ошибку вида

``` s
PHP Fatal error:  Allowed memory size of 549453824 bytes exhausted (tried to allocate 64 bytes) in /var/www/some_user/data/www/site.domain/libraries/joomla/error/exception.php on line 117
```

ошибка возникает при вызове

``` php
$this->backtrace = debug_backtrace();
```

в configuration.php при этом видим что-то вроде 

``` php
var $cache_handler = 'memcache';
var $memcache_settings = array("persistent" => "0", "compression" => "0", "servers" => array("0" => array("host" => "127.0.0.1", "port" => "11211")));
```

или

``` php
var $caching = '2';
var $cache_handler = 'memcache';
var $memcached_server_host = '127.0.0.1';
var $memcached_server_port = '11211';
```

Проверяем, есть ли на тачке memcache

``` bash
ss -lnpt 'src :11211'
State      Recv-Q Send-Q                                                Local Address:Port                                                               Peer Address:Port              
Cannot open netlink socket: Protocol not supported
LISTEN     0      0                                                         127.0.0.1:11211                                                                         *:*                   users:(("memcached",pid=30642,fd=26))
```

Если есть, значит нужно установить php-модуль memcache, и включить его в настройках. 
Если такого сервиса на сервере нет, делаем 

``` php
public $caching = '0';
public $cache_handler = 'file';
```

вместо значений, указанных выше. Проблема перестаёт проявляться.

Также важно обратить внимание на знаения 

``` php
var $list_limit = '20';
var $session_handler = 'database';
```

при возникновении данной ошибки, не верное значение ==$list_limit== и ==$session_handler== тоже могу тприводить к возникновению подобной проблемы.  Есть сомнения, лучше сбросить значения на дефолтные, что указаны выше.

