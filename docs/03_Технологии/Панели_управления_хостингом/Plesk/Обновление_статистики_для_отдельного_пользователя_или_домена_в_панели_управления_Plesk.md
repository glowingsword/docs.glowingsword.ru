---
title: 'Обновление статистики для отдельного пользователя или домена в панели управления Plesk'
authors: 
 - glowingsword
tags:
 - Plesk
date: 2020-04-04
---
# Обновление статистики для отдельного пользователя или домена в панели управления Plesk

ВЫполнем команду

``` bash
sudo /usr/local/psa/admin/sbin/statistics --calculate-one --domain-name=u1234567.plsk.somehosting.domain
````
где `u1234567.plsk.somehosting.domain` - технологический домен, или доменное имя одного из сайтов клиента.
