---
title: 'phpmyadmin  открывается по HTTP вместо HTTPS'
authors: 
 - glowingsword
tags:
 - ISPManager
 - ISPManager 5
 - phpMyAdmin
date: 2021-09-11
---

В файле /usr/local/mgr5/etc/conf.d/myadmin.conf вместо текущей строки с extaction phpmyadmin  указываем строку вида

```bash
extaction phpmyadmin https://$site/phpmyadmin/
```
после неё сразу добавляем 

```bash
path phpmyadmin-redirect https://$site/phpmyadmin/
```
так как бывают случаи, что после релоада панелька всё равно пытается открывать phpmyadmin по HTTPS.

В  /etc/phpMyAdmin/config.inc.php добавляем

```bash
$cfg['PmaAbsoluteUri'] = 'https://'.$_SERVER['SERVER_NAME'].'/phpmyadmin/';
```

Перезапускаем ISPManager 5

``` bash
/usr/local/mgr5/sbin/mgrctl -m ispmgr exit
```
и веб-серверы

``` bash
nginx -t  && service nginx restart 
```
``` bash
service httpd configtest && service httpd restart
```