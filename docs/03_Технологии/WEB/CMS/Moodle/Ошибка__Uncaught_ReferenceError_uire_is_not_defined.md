---
title: 'Ошибка "(index):2756 Uncaught ReferenceError: uire is not defined" в Moodle'
authors: 
 - glowingsword
tags:
 - CMS
 - 'Moodle'
 - Softaculous
date: 2020-05-14
---

# Ошибка "(index):2756 Uncaught ReferenceError: uire is not defined" в Moodle

Если меню пользователя в верхнем правом углу на портале с Moodle не работает, а в консоли отладчика браузера видим ошибки вида

``` js
polyfill.min.js:formatted:3 Uncaught SyntaxError: Invalid regular expression: missing /
(index):2756 Uncaught ReferenceError: uire is not defined
    at (index):2756
    at Object.execCb (require.min.js:5)
    at b.check (require.min.js:5)
    at b.<anonymous> (require.min.js:5)
    at require.min.js:5
    at require.min.js:5
    at each (require.min.js:5)
    at b.emit (require.min.js:5)
    at b.check (require.min.js:5)
    at b.<anonymous> (require.min.js:5)
```
стоит безотлогательно проверить настройки php, исползуемые php-обработчиком сайта. 

Сделать это можно разными путями, самый простой из которых - добавление скрипта ==phpinfo.php== с phpinfo()...

Проверяем: 

=== "Команда"
    ``` bash
    curl -s http://domain.name/phpinfo.php |grep mbstring.func_overload
    ```

===  "Результат"
    ``` bash
    # curl -s http://domain.name/phpinfo.php |grep mbstring.func_overload
    <tr><td class="e">mbstring.func_overload</td><td class="v">2</td><td class="v">2</td></tr>
    ```

Просто комментируем в соответсвующем php.ini(путь можно глянуть в результате выполнения phpinfo, по аналогии с тем, как мы смотрели mbstring.func_overload)

``` ini
;mbstring.func_overload=2
;mbstring.internal_encoding=UTF-8
```

сохраняем, если у нас php как модуль apache, перезапускаем Apache. Проверяем, что значение изменилось(командой, упомянутой выше).

Затем(это важно), чистим кэш Moodle, делаем это командой

``` bash
/opt/php/7.2/bin/php admin/cli/purge_caches.php
```

Где вместо ==/opt/php/7.2/bin/php== необходимо указать путь к используемой сайтом сборке(версии) php, а саму команду выполняем обязательно в домашнем каталоге сайта с Moodle(иначе чистка кэша завершится неудачно).