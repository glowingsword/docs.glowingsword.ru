---
title: 'Тормозит phpMyAdmin на серверах c cPanel'
authors: 
 - glowingsword
tags:
 - cPanel
 - phpMyAdmin
date: 2021-01-26
---

Если у нас на сервере с cPanel сильно тормозит phpMyAdmin, при том, что в консоли mysql запросы к БД выполняются нормально, нам необходимо отключить параметр =="Enable phpMyAdmin information schema searches"== в настройках WHM.

Переходим в ==WHM ⇾ Home ⇾ Server Configuration ⇾ Tweak Settings==, находим вкладку Software и переключаем ==Enable phpMyAdmin information schema searches [?]== с дефолтного значения On на значение Off, и у нас должно получиться, как на скриншоте,

 ![!Description](/assets/img/cpanel_how_to_disable_phpmyadmin_schema_searches.png)

 после чего нажимаем на кнопку ==Save==. Панель применит изменение, и проблема перестанет проявляться.



