---
title: 'Даунгрейд exim до 3.92.3 на Centos 7'
authors: 
 - glowingsword
tags:
 - Exim
 - Настройка Exim
 - Почтовый сервер
date: 2020-05-24
---
 # Даунгрейд exim до 3.92.3 на Centos 7
 
Почтовый сервер exim-4.93 вышел с косяком реализации новых фич SPF, в итоге после обновления на Centos 7 exim до 3.93 наблюдаютя проблемы с отправкой сообщений.

Понижаем версию пакета

```bash
yum downgrade exim-4.92.3 -y
```

Если получаем ошибку

```bash
 No package exim-4.92.3 available.
```
из-за того, что в кэше старого пакета нет — то понижаем версию так
 
yum downgrade ftp://ftp.pbone.net/mirror/archive.fedoraproject.org/epel/7.2020-04-20/x86_64/Packages/e/exim-4.92.3-1.el7.x86_64.rpm -y

Эта команда загрузит пакет из среза репы epel с зеркала ftp.pbone.net за 2020-04-20, где нужный пакет ещё был, и понизит версию, используя загруженный пакет.

```bash 
yum install yum-plugin-versionlock
```

лочим его


== "Команда"
    ```bash
    yum versionlock exim-*
    ```
== "Результат"
    ```bash
    yum versionlock exim-*
    Loaded plugins: fastestmirror, versionlock
    Adding versionlock on: 0:exim-4.92.3-1.el7
    versionlock added: 1
    ```

проверяем, что он залочен


== "Команда"
    ```bash
    yum versionlock list
    ```

== "Результат"
    ```bash  
    yum versionlock list
    Loaded plugins: fastestmirror, versionlock
    0:exim-4.92.3-1.el7.*
    versionlock list done
    ```

перезапускаем 

```bash
systemctl restart exim
```
проверяем, что сервис запущен

```bash
systemctl status exim
```

После чего проверяем корректность работы отправки писем — сообщения должны отправляться после понижения версии exim корректно.
