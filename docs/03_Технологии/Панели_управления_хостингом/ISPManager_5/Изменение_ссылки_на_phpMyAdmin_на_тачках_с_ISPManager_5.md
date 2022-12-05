---
title: Изменение ссылки на phpMyAdmin на тачках с ISPManager 5
authors: 
 - glowingsword
tags:
 - ISPManager
 - ISPManager 5
 - phpMyAdmin
date: 2020-04-04
---
# Изменение ссылки на phpMyAdmin на тачках с ISPManager 5
Редактируем

``` bash
vim /usr/local/mgr5/etc/ispmgr.conf 
```
и

``` bash
vim /usr/local/mgr5/etc/conf.d/myadmin.conf
```

в зависимости от того, где указана строка

``` yaml
extaction phpmyadmin <https://$site/newadmin>
```

Заменяем в ней `phpmyadmin` на нужное нам значение.

В 

``` bash
vim /etc/nginx/vhosts-includes/phpmyadmin.conf
```

заменяем `phpmyadmin` на нужное нам значение в локейшенах

``` nginx
location /phpmyadmin location \~\*
^/phpmyadmin/(.+\\.(jpg\|jpeg\|gif\|css\|png\|js\|ico\|html\|xml\|txtt
))$ 
location \~ ^/phpmyadmin/(.+\\.php)$ 
location ^\~ /phpmyadmin/setup
```

В файле

``` bash
vim /etc/httpd/conf.d/phpmyadmin.conf
```
правим phpmyadmin на нужное нам значение в
``` apacheconf
Alias /phpmyadmin /usr/share/phpMyAdmin
```

Перезапускаем ISPManager 5

``` bash
/usr/local/mgr5/sbin/mgrctl -m ispmgr exit
```
и веб-серверы

``` bash
service nginx configtest && service nginx restart 
```
``` bash
service httpd configtest && service httpd restart
```
<http://forum.sys-admin.kz/index.php?topic=4692.0>