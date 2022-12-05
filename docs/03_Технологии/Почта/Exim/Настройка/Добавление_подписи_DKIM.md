---
title: Добавление подписи DKIM
authors: 
 - glowingsword
tags:
 - Exim
 - Настройка Exim
 - DKIM
date: 2020-04-04
---
# Добавление подписи DKIM

Для начала устанавливаем пакет opendkim

``` bash
yum install opendkim
```

Создаём директорию для хранения публичного и секретного ключей

``` bash
mkdir -p /etc/exim/dkim
```

Создаём ключ

``` bash
opendkim-genkey -D /etc/exim/dkim -d domain.ru -s mail
```

Переименовываем его

``` bash
mv mail.private domain.ru.key
```

Меняем владельца файлов, и назначаем им нужные права

``` bash
chown -R exim:exim /etc/exim/dkim/
chmod 640 /etc/exim/dkim/*
```

Редактируем конфигурационный файл EXIM

``` bash
vim /etc/exim/exim.conf
```

В начало файла необходимо добавить

``` ini
##DKIM
DKIM_DOMAIN = ${lc:${domain:$h_from:}}
DKIM_FILE = /etc/exim/dkim/${lc:${domain:$h_from:}}.key
DKIM_PRIVATE_KEY = ${if exists{DKIM_FILE}{DKIM_FILE}{0}}
```

В секцию remote\_smtp добавляем следующее

``` ini
#DMIM settings for SMTP
dkim_domain           = DKIM_DOMAIN
dkim_selector         = mail
dkim_private_key      = DKIM_PRIVATE_KEY
```

Сохраняем изменения, и перезапускаем EXIM

``` bash
/etc/init.d/exim restart
```

Смотрим пример DNS-записей в файле /etc/exim/dkim/mail.txt(используется
синтаксис конфигурационного файла DNS-сервера BIND), и по их образцу
добавляем необходимые записи в настройки DNS вашего домена.

Нужно добавить две записи, примерно следующего вида:

``` ini
mail._domainkey.domain.ru.  TXT  v=DKIM1\; k=rsa\; p=ocheni_dlinnii_cliuch
_adsp._domainkey.domain.ru. TXT  dkim=unknown
```
