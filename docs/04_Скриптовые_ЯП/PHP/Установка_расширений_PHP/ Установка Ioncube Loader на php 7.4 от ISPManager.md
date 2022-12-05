---
title: 'Установка Ioncube Loader на php 7.4 от ISPManager'
authors: 
 - glowingsword
tags:
 - PHP
 - 'Установка расширений PHP'
 - 'ionCube PHP Loader'
todo: 'Допилить статью, как будет время'
date: 2021-04-01
---

Качаем архив с последней версией Ioncube Loaders

```bash
wget https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
```

```bash
tar -zxf ioncube_loaders_lin_x86-64.tar.gz
```
```bash
cp ioncube/ioncube_loader_lin_7.4.so /opt/php74/lib/php/modules/
```
```bash
echo 'zend_extension=ioncube_loader_lin_7.4.so' > /opt/php74/etc/mods-available/ioncube.ini
```
```bash
ln -s /opt/php74/etc/mods-available/ioncube.ini /opt/php74/etc/php.d/ioncube.ini
```

Выполняем 

```bash
/opt/php74/bin/php -v|grep ionCube
```

и видим 

```bash
with the ionCube PHP Loader + ionCube24 v10.4.5, Copyright (c) 2002-2020, by ionCube Ltd.
```

Если похожей строки нет, чтобы мы сделали не корректно, по шагам проверяем, где и что пошло не так, исправляем.
