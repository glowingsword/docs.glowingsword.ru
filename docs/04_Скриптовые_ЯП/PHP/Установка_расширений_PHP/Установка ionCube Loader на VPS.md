---
title: "Установка ionCube Loader на VPS с Centos, Debian или Ubuntu"
authors: 
 - glowingsword
tags:
 - PHP
 - 'Установка расширений PHP'
 - 'ionCube PHP Loader'
date: 2022-07-22
---

# Установка ionCube Loader на VPS с Centos, Debian или Ubuntu

## Подготовительные работы

Переходим в каталог, в который принято качать сорцы устанавливаемых руками приложений и модулей

```bash
cd /usr/local/src/
```

убеждаемся, что в каталоге отсутствуют других файлы с именами вида ioncube_loaders_lin*, оставшиеся от предыдущих попыток установки ionCube

```bash
ls ioncube*
```

если команда нашла какие-то файлы, удаляем их

```bash
rm ioncube*
```

## Загрузка и распаковка дистрибутива с версиями модуля

Качаем необходимый дистрибутив

выбираем нужный вариант исходя из архитектуры используемого дистрибутива

=== "x86_64(amd64)"
    ```bash
    wget https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
    ```

=== "x86 (32 bit distro)"
    ``` markdown
    wget https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86.tar.gz
    ```

Распаковка полученного тарбола

```bash
tar -xvzf ioncube_loaders_lin*.tar.gz
```

### Распаковка и копирование в нужный каталог каталога с модулями ionCube

Перемещаем каталог с модулями в каталог, в котором они должны находиться.
Выбираем вариант с учётом используемого на VPS дистрибутива и его архитектуры(важно для Centos, на Debian-based модуль всегда перемещается в один и тот же каталог назначения).

=== "Centos x86-64"
    ```bash
    mv ioncube /usr/lib64/php/ioncube
    ```

=== "Debian / Ubuntu"
    ```bash
    mv ioncube /usr/local/
    ```

=== "Centos x86(32 bit)"
    ```bash
    mv ioncube /usr/lib/php/ioncube
    ```



## Указываем путь к модулю в конфигурационном файле php.ini

Здесь также выбираем команду в зависимости от дистрибутива

=== "Centos x86-64"
    ```bash
    echo "zend_extension=/usr/lib64/php/ioncube/ioncube_loader_lin_7.1.so" >> /etc/php.d/ioncube.ini
    ```

=== "для Debian/Ubuntu"
    ```bash
    echo "zend_extension=/usr/local/ioncube/ioncube_loader_lin_7.1.so" >> /etc/php7/mods-available/ioncube.ini
    ln -s /etc/php7/mods-available/ioncube.ini /etc/php7/cli/conf.d/01_ioncube.ini
    ln -s /etc/php7/mods-available/ioncube.ini /etc/php7/apache2/conf.d/01_ioncube.ini
    ```

=== "Centos x86(32 bit)"
    ```bash
    echo "zend_extension=/usr/lib/php/ioncube/ioncube_loader_lin_7.1.so" >> /etc/php.d/ioncube.ini
    ```


Где вместо ioncube_loader_lin_7.1.so необходимо указать файл для необходимой вам версии php, для которой вы подключаете модуль.

Посмотреть версии модуля для каких версий PHP доступны можно просто выполнив команду

```bash
ls -lha /usr/lib{,64}/php/ioncube/ /usr/lib/php/ioncube/
```

где вместо ioncube_loader_lin_7.1.so указываем нужную вам версию модуля.

!!! info "Как выбрать модуль правильно"
    Номер, идущий после ioncube_loader_lin_ в имени файлов соответствует версии PHP, для которой они были собраны. Если в имени файла в конце присутствует _ts — это версия модуля c thread safe. Если модуль подключается для PHP как модуль Apache(mod_php), подключаем версию с ts, если для PHP как CGI/FastCGI, без него.

## Проверяем результат

Выполняем

```bash
php -v
```

в выводе команды должна появиться строка вида

```bash
    with the ionCube PHP Loader v6.1.0 (), Copyright (c) 2002-2017, by ionCube Ltd.
```

также должен появиться модуль

```
php -m | grep ionCube
```
