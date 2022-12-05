---
title: 'Исправляем ошибку 404 при обращении к Softaculous на серверах с панелью управления cPanel'
authors: 
 - glowingsword
tags:
 - cPanel
 - softaculous
date: 2020-04-21
---
# Исправляем ошибку 404 при обращении к Softaculous на серверах с панелью управления cPanel

В случае, если при обращении к `Softaculous` возникает ошибка `404`, стоит проверить присутствует ли на сервере соответствующий симлинк

``` bash
ls -ln /usr/local/cpanel/base/frontend/paper_lantern/softaculous
```
В случае отсутствия симлинка создаём новый

``` bash
ln -s /usr/local/cpanel/whostmgr/docroot/cgi/softaculous/enduser /usr/local/cpanel/base/frontend/paper_lantern/softaculous
```

Если симлинк корректный, но на сервере отсутствует `softaculous` - выполняем
``` bash
/usr/local/cpanel/scripts/install_plugin
```
``` bash
/usr/local/cpanel/whostmgr/docroot/cgi/softaculous/softaculous_plugin.tar.bz2
```
для установки softaculous.

<http://www.softaculous.com/board/index.php?tid=7750&title=Softaculous_does_not_show_up_after_cpanel_update_11.50>
