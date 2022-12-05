# Установка свежей версии timezonedb на не дефолную версию php на VPS

!!! warn "Если у вас несколько версий php" 
    Важно указать путь к phpize той сборки php, для которой будет установлено расширение. Дефолтный phpize и phpize других версий php изменят настройки расширения под свою версию php api, поэтому очень важно не перепутать версию phpize при сборке.

    Также важно в параметрах configure верно указать путь к php-config нужной версии php. 

!!! example "К примеру"
    К примеру, мы устанавливаем расширение для сборки php 5.5 из каталога /opt/php55. Следовательно, у нас путь к данным файлам будет иметь вид:
    * phpize - ==/opt/php55/bin/phpize==
    * phpconfig - ==/opt/php55/bin/php-config==
    
    И именно путь к этим версиям ==phpize== и ==php-config== мы будем использовать при конфигурации собираемого расширения перед сборкой.

## Скачиваем архив с расширением
``` bash
wget https://pecl.php.net/get/timezonedb-2018.9.tgz
```

## Распаковываем
``` bash
tar -xvf timezonedb-2018.9.tgz 
```
после чего переходим в каталог с исходниками расширения

``` bash
cd timezonedb-2018.9
```

## Конфигурирем перед сборкой
### phpize

``` bash
/opt/php/5.5/bin/phpize 
```

### configure
``` bash
./configure --with-php-config=/opt/php55/bin/php-config
```

## Сборка
``` bash
make 
```

## Установка расширения

``` bash
make install 
```
не забываем сделать

``` bash
echo "extension=timezonedb.so" > /opt/php55/etc/php.d/timezonedb.ini
``` 

что-бы собранное расширение подхватилось php.

## Проверка

### Проверяем в консоли

Выполняем

``` bash
/opt/php55/bin/php -i|grep timezone
```

### Проверяем на сайте

Перезапускаем Apache, в моём случае командой

``` bash
service httpd restart
```

в вашей возможно понадобится 

``` bash
systemctl restart httpd
```

После чего создаём в хомяке сайта, использующего данную сборку php, файл phpinfo.php

``` php
<?php phpinfo(); ?>
```

Переходим по url вида https://имя.сайта/phpinfo.php, где вместо "имя.сайта" - доменное имя вашего сайта. Видим что информация о Timezone DB изменилась, теперь сборка юзает свежую timezonedb из собранного вами расширения, а не базу timezonedb, с которой данная сборка php была собрана изначально.

