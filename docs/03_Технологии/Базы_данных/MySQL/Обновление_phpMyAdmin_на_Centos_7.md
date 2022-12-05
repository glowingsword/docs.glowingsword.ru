---
title: "Обновление phpMyAdmin на Centos 7"
authors: 
 - glowingsword
tags:
 - MySQL
 - "Полезные ссылки на информацию о MySQL"
date: 2020-09-06
---

# Обновление phpMyAdmin на Centos 7 из репозитория remi

Проверяем какой у нас php, для свежего phpMyAdmin нужен php 7.1.3 и выше
```bash
php -v 
```
у нас не нужная нам версия, нужно обновлять

```
PHP 5.4.16 (cli) (built: Apr  1 2020 04:07:17)                                                                                                                 
Copyright (c) 1997-2013 The PHP Group                                                                                                                          
Zend Engine v2.4.0, Copyright (c) 1998-2013 Zend Technologies                                                                                                  
    with the ionCube PHP Loader (enabled) + Intrusion Protection from ioncube24.com (unconfigured) v10.2.4, Copyright (c) 2002-2018, by ionCube Ltd.
```

Поключаем репы remi и epel

```bash
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
```
```bash
yum install https://rpms.remirepo.net/enterprise/remi-release-7.rpm
```

Ставим yum-utils

```bash
yum install yum-utils
```
и включаем с помощью yum-config-manager из состава yum-utils нужную нам версию репы с php
```bash
yum-config-manager --enable remi-php71
```
```bash
yum install php-common
```

как обновление дефолтной версии php на сервере завершится, не забываем сделать
```bash
httpd -t
```
и если всё будет Ok, то
```bash
systemctl restart httpd.service
```
Если вознкинут ошибки конфигурации апачика, исправляем их(в частности может потребоваться скопировать /etc/httpd/conf.d/php.conf.rpmnew в /etc/httpd/conf.d/php.conf.rpm, забэкапив старую версию файла перед этим куда-то), после чего выполняем рестарт httpd.

PHP успешно обновили? Отлично, теперь самое время обновить сам phpMyAdmin
```bash
yum --enablerepo=remi,remi-test  install phpMyAdmin
```
После успешного завершения процесса на сервере будет установлен phpMyAdmin, что корректно работает с Mysql версии 8.0.
