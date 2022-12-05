---
title: 'Установка модуля для стандартной версии php на VPS с cPanel'
authors: 
 - glowingsword
tags:
 - cPanel
date: 2020-04-21
---
# Установка модуля для стандартной версии php на VPS с cPanel

Для начала отмечаем 1 пункт, отвечающий за включение нужного нам модуля в файл `/var/cpanel/easy/apache/profile/makecpphp.profile.yaml`.

К примеру:
``` perl
perl -i -pe 's/Cpanel::Easy::PHP(\\d\*)::Curl(\\S\*): 0/Cpanel::Easy::PHP$1::Curl$2: 1/g' /var/cpanel/easy/apache/profile/makecpphp.profile.yaml
```
После чего выполняем команду
``` bash
/scripts/makecpphp
```
для запуска процесса пересборки `php`.
