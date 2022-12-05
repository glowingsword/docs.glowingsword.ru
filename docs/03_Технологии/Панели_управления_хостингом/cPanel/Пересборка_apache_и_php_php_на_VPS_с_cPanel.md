---
title: 'Пересборка apache и php php на VPS с cPanel'
authors: 
 - glowingsword
tags:
 - cPanel
 - PHP
date: 2020-04-21
---
# Пересборка apache и php php на VPS с cPanel

Залогинившись на сервере, создаём сессию screen, к примеру
``` bash
screen -S rebuildapache
```
после чего запускаем скрипт
``` bash
/scripts/easyapache
```
отмечаем в диалоговых окнах нужные нам пункты, в том числе модули, и запускаем перезапуск apache и php.

<https://forum.likg.org.ua/server-side-actions/recompile-cpanel-internal-php-with-curl-curlssl-support-t452.html>
