---
title:  'Ошибки last update puppet'
authors: 
 - glowingsword
tags:
 - Puppet
 - 'Ошибки Puppet'
date: 2020-04-21
---
# Ошибки last update puppet

В случае возникновения ошибок вида
``` bash
Sep 21 14:21:16 localhost puppet-agent\[19992\]: Ignoring --listen on
onetime run Sep 21 14:21:16 localhost puppet-agent\[19992\]: Run of
Puppet configuration client already in progress; skipping
```
проверяем присутствует ли puppet в списке процессов
``` bash
ps auxf |grep puppet
```
если его нет, а при
``` bash
/etc/init.d/puppet restart
```
отображается сообщение вида
``` bash
Ignoring --listen on onetime run
```
или при
``` bash
root@host \[\~\]\# puppetd --test --verbose notice: Ignoring --listen on
onetime run notice: Run of Puppet configuration client already in
progress; skipping
```
проверяем есть ли файлы `/var/lib/puppet/run/agent.pid` и `/var/lib/puppet/state/puppetdlock` и удаляем их, после чего повторно перезапускаем `puppet`

``` bash
/etc/init.d/puppet restart
```

Проверяем состояние puppet
``` bash
/etc/init.d/puppet-agent status /usr/local/mon/bin/check_puppet.sh
```
``` bash
/usr/local/mon/bin/check_puppet_last_update.sh
```
Если непонятно, что именно приводит к ошибке запуска `puppet`, выполняем
``` bash
puppetd --test --verbose
```
на серверах с не дефолтным расположением конфига `puppet` делаем так
``` bash
/usr/bin/puppet agent -tv --config /opt/puppet/puppet.conf
```

где `/opt/puppet/puppet.conf` - путь к файлу конфига.

<https://administratosphere.wordpress.com/2012/05/24/puppet-refuses-to-run-with/>
