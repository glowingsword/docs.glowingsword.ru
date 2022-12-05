---
title: 'Установка dbase для альтернативной версии php'
authors: 
 - glowingsword
tags:
 - PHP
 - 'Установка расширений PHP'
todo: 'Допилить статью, как будет время'
date: 2020-05-15
---

# Установка dbase для альтернативной версии php

## Подготовка к сборке
Убеждаемся что установлены необходимые для сборки пакеты.
Обязательно должны быть установлены gcc и autoconf(для Centos, в других дистрибутивах они могут иметь другое наименование, необхоимо сверяться с информацией по конкретному дистрибутиву ). 

Если их нет - ставим:

``` bash
yum install gcc autoconf
```

## Получение исходников модуля
Обновляем информацию о пакетах для пакетного менеждера pecl

``` bash
/opt/php72/bin/pecl channel-update pecl.php.net
```

Качаем сам пакет

``` bash
 pecl download dbase
downloading dbase-7.0.1.tgz ...
Starting to download dbase-7.0.1.tgz (33,588 bytes)
.........done: 33,588 bytes
File /root/dbase-7.0.1.tgz downloaded
```


Если pecl у сборки отстствует - не беда, качаем архив с сайта https://pecl.php.net/package/dbase с помощью wget/curl и любого другого походящего для этого консольного http-клиента.

Распаковываем скачанный архив:
``` bash
tar -vzxf dbase-7.0.1.tgz
```
Переходим в каталог с исходниками модуля

``` bash
cd dbase-7.0.1
```

## Настройка параметров сборки
### phpize
Обязательный этап, задаёт версию api для расширения, чтобы оно подходило для сборки(расширение, собранное с другой версией zend api интерпретатор не сможет загрузить, поэтому перед сборкой всега задаётся нужная версия zend api для собираемого расширения).
``` bash
/opt/php72/bin/phpize
```
## php-config
На этому этапе собиарется информация о том, с какими параметрами собиралась сборка php, они необходимы для корректной сборки и установки модуля.

``` bash
./configure --with-php-config=/opt/php72/bin/php-config
```

## Сборка и установка модуля
### Сборка
``` bash
make
```

### Устанновка
Устанавливаем его в каталог для модулей


=== "Команда"
    ``` bash
    make install
    ```

=== "Результат"
    ``` bash
    # make install
    Installing shared extensions:     /opt/php72/lib/php/modules/
    ```


### Включение модуля
``` bash
echo 'extension=dbase.so' > /opt/php72/etc/php.d/dbase.ini
```
## Проверка

``` bash
# /opt/php72/bin/php -m|grep dbase
dbase
```
