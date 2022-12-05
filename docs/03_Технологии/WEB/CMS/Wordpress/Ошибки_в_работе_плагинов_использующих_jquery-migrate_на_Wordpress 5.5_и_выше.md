---
title: 'Ошибки в работе плагинов, использующих jquery-migrate, на Wordpress 5.5 и выше'
authors: 
 - glowingsword
tags:
 - CMS
 - Wordpress
 - JS
 - jQuery
date: 2020-11-01
---
# Ошибки в работе плагинов, использующих jquery-migrate, на Wordpress 5.5 и выше

Ошибки, возникающие в процессе, выглядят примерно так

```js
wp-auth-check.min.js?ver=5.5.3:2 Uncaught TypeError: Cannot read property 'hasClass' of undefined
    at HTMLDocument.<anonymous> (wp-auth-check.min.js?ver=5.5.3:2)
    at HTMLDocument.dispatch (jquery.js?ver=1.12.4-wp:3)
    at HTMLDocument.r.handle (jquery.js?ver=1.12.4-wp:3)
    at Object.trigger (jquery.js?ver=1.12.4-wp:3)
    at HTMLDocument.<anonymous> (jquery.js?ver=1.12.4-wp:3)
    at Function.each (jquery.js?ver=1.12.4-wp:2)
    at n.fn.init.each (jquery.js?ver=1.12.4-wp:2)
    at n.fn.init.trigger (jquery.js?ver=1.12.4-wp:3)
    at Object.<anonymous> (heartbeat.min.js?ver=5.5.3:2)
    at i (jquery.js?ver=1.12.4-wp:2)
```

Как правило, ошибки разные, но в них присутствует упоминание jquery.js и какого-либо отсутствующего свойства у элемента DOM, помеченного как не объявленный. Хотя, бывают и другие ошибки.

Возникает эта проблема после обновления до Wordpress 5.5 и вызвана разницей в версии jquery, поставляемой с CMS Wordpress и той, что требуется для корректной работы плагинов.

Фиксится данная проблема с помощью установки (Enable jQuery Migrate Helper)[https://wordpress.org/plugins/enable-jquery-migrate-helper/]