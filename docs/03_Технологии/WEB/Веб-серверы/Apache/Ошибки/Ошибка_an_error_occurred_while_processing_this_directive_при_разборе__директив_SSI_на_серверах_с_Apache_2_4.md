---
title: "Ошибка \"[an error occurred while processing this directive]\" при разборе  директив SSI на серверах с Apache 2_4.md"
authors:
 - glowingsword
tags:
 - Apache
 - Ошибки Apache
date: 2020-08-10
---
# Ошибка "[an error occurred while processing this directive]" при разборе  директив SSI на серверах с Apache 2_4.md

Если после агрейда c Apache 2.2.x до Apache 2.4.x на сайте перестала работать часть директив SSI, и на их месте на страницах сайта отображается ошибка 

```
[an error occurred while processing this directive] 
```

значит вам "повезло" столкнуться с отсутствием совместимости некоторых использованных на сайте директив SSI с новым парсером SSI.

В частности, проблема может затрагивать директивы:

```apacheconf
#if
#include
#include virtual
```
В моём случае падало всё на 

```html
<!--#include virtual = "/comments/comments.html" -->
```

Для решения проблемы можно включить страый парсер SSI в файле .htaccess сайта, добавив в него директиву

```apacheconf
SSILegacyExprParser on
```

Больше информации по данной проблеме и отличиях старого парсера от новогом можно узнать тут:

* <http://httpd.apache.org/docs/2.4/upgrading.html>
* <http://httpd.apache.org/docs/2.4/mod/mod_include.html#ssilegacyexprparser>