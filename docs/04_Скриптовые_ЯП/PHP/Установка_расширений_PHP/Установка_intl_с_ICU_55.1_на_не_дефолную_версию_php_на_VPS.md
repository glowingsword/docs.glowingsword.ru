---
title: 'Установка intl с ICU 55.1 на не дефолную версию php на VPS'
authors: 
 - glowingsword
tags:
 - PHP
 - 'Установка расширений PHP'
 - Memcache
date: 2020-04-21
---
# Установка intl с ICU 55.1 на не дефолную версию php на VPS

Качаем ICU 58.2(последнюю версию, с которой корректно собирается php intl на Centos 6.x в настоящий момент, 59.1 не собирается из-за ошибок вида 

``` bash
/opt/icu5c/include/unicode/umachine.h:347:13: error: 'char16_t' does not name a type)`
```

``` bash
wget https://github.com/unicode-org/icu/releases/download/release-58-2/icu4c-58_2-src.tgz
```
``` bash
tar zxvf icu4c-58_2-src.tgz
```

``` bash
cd icu/source ./configure --prefix=/opt/icu5c && make && make install
```

``` bash
wget https://pecl.php.net/get/intl-3.0.0.tgz
```
``` bash
tar -xvzf intl-3.0.0.tgz
```
``` bash
cd intl-3.0.0 /opt/php56/bin/phpize
```
``` bash
./configure --with-php-config=/opt/php56/bin/php-config --with-icu-dir=/opt/icu5c
```
``` bash
make
```
``` bash
make install 
```
``` bash
ls -la /opt/php56/lib/php/extensions/no-debug-non-zts-20131226/
```
``` bash
echo "extension=intl.so" > /opt/php56/etc/php.d/intl.ini
```
``` bash
/opt/php56/bin/php -m | grep intl 
```
``` bash
intl 
``` bash
/opt/php56/bin/php -i | grep
```
``` bash
ICU
```

Для php `7.x` делаем по другому. Скачиваем архив с исходниками php той же
версии, что и версия для которой собирается модуль
``` bash
wget http://md1.php.net/distributions/php-7.1.7.tar.xz
```
распаковываем
``` bash
tar -xvf php-7.1.7.tar.xz заходим в распакованный каталог
```
``` bash
cd php-7.1.7
```
заходим в каталог нужного нам расширения 
``` bash
cd ext/intl
```
собираем его
``` bash
/opt/php71/bin/phpize 
```
``` bash
./configure --with-php-config=/opt/php71/bin/php-config --with-icu-dir=/opt/icu5c
``` 
``` bash
make 
```
``` bash
make install 
```
``` bash
ls -la /opt/php71/lib/php/extensions/no-debug-non-zts-20131226/
```
``` bash
echo "extension=intl.so" > /opt/php71/etc/php.d/intl.ini
```
``` bash
/opt/php71/bin/php -m | grep intl
```
``` bash
intl 
```
``` bash
 /opt/php71/bin/php -i | grep
 ```
 ``` bash
ICU
```

Если в процессе сборки при make выдаются ошибки для `ICU` версии `> =59.1`, делаем так
``` bash
make CXXFLAGS="-g -std=c++11"
```
вместо простого
``` bash
make
```
Дополнительная информация
<https://nix-tips.ru/obnovlenie-icu-na-centosred-hatfedora.html>
<https://ru.stackoverflow.com/questions/524666/%D0%9E%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-icu-%D0%BD%D0%B0-php7>
