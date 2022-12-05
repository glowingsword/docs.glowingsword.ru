---
title: 'Ошибка вида "spam, Array, in core/model/modx/rest/modrestsockclient.class.php on line 43" на сайтах с modx после переноса'
authors: 
 - glowingsword
tags:
 - ModX
date: 2020-04-18
---

# Ошибка вида "'spam', Array, in core/model/modx/rest/modrestsockclient.class.php on line 43" на сайтах с modx после переноса

Выглядит примерно так

```bash
[Wed Feb 22 16:25:46.675102 2017] [:error] [pid 6456] [client 123.123.123.123:46796] PHP Fatal error:  Uncaught Error: Call to a member function getClientIp() on null in /some/path/core/model/modx/rest/modrestsockclient.class.php:43\nStack trace:\n#0 /some/path/core/model/modx/rest/modrestclient.class.php(135): modRestSockClient->request('www.stopforumsp...', 'api?', 'GET', Array, Array)\n#1 /some/path/core/components/formit/model/stopforumspam/stopforumspam.class.php(84): modRestClient->request('http://www.stop...', 'api', 'GET', Array)\n#2 /some/path/core/components/formit/model/stopforumspam/stopforumspam.class.php(58): StopForumSpam->request(Array)\n#3 /some/path/core/components/formit/model/formit/fihooks.class.php(595): StopForumSpam->check('', NULL)\n#4 /some/path/core/components/formit/model/formit/fihooks.class.php(140): fiHooks->spam(Array)\n#5 /some/path/core/components/formit/model/formit/fihooks.class.php(116): fiHooks->load('spam', Array, in /some/path/core/model/modx/rest/modrestsockclient.class.php on line 43, referer: http://www.some.domain/unavailable.htm
```

Для исправления необходимо установить php-модуль curl(php-curl), перезапустить apache/php-fpm и убедиться что расширение curl активно. После чего проблема перестаёт проявляться.