---
title: 'Кодировка iso-8859-1 в заголовках ответа при обращении к служебным страницам веб-сервера Apache'
authors: 
 - glowingsword
tags:
 - Apache
date: 2020-04-05
---
# Кодировка iso-8859-1 в заголовках ответа при обращении к служебным страницам веб-сервера Apache

Cлужебные страницы веб-браузера, вроде страниц, отдаваемых при срабатывании правил перенаправления, таких как
``` bash
$ curl <http://localhost/> 
```
``` bash
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">;

<html>
<head>
<title>

301 Moved Permanently

</title>
</head>
<body>
<h1>

Moved Permanently

</h1>

The document has moved <a href="https://localhost/">here</a>.

<hr>
<address>

Apache/2.2.15 (CentOS) Server at localhost Port 80

</address>
</body>
</html>
```

или страниц о возникновении ошибок отдаются с кодировкой по умолчанию. 

В качестве которой используется кодировка iso-8859-1. Это нормальное
поведение для веб-сервера Apache. 

Подробное описание причины, по которой используется данная кодировка присутствует на странице официального руководства Apache <http://httpd.apache.org/docs/2.4/env.html> в блоке описания директивы `suppress-error-charset`.