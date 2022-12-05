---
title:  'Missing privilege separation directory: /var/run/sshd  при запуске SSH'
authors: 
 - glowingsword
tags:
 - Ubuntu
 - Настройка Ubuntu
 - ssh
date: 2020-04-04
---
# Missing privilege separation directory: /var/run/sshd  при запуске SSH

Если в journalctl -xe после запуска ssh.service на Ubuntu 16.04 видим ошибку 

``` bash
Missing privilege separation directory: /var/run/sshd
```

открываем файл /usr/lib/tmpfiles.d/sshd.conf и смотрим чтобы в нём было

``` bash
d /var/run/sshd 0755 root root
```
выполняем 
``` bash
systemd-tmpfiles --create
```

Проверяем. Если не помогло, измняем на 

``` bash
d /run/sshd 0755 root root
``` 

и проверяем ещё раз. А можно указать оба варианта, на случай, если systemd будет искать каталог, у нас будет оба варианта, не зависимо от того, какой вариант будет искать сервис(так сказать подстелить соломки, так как buleproof - наше всё).


https://serverfault.com/questions/941855/why-am-i-missing-var-run-sshd-after-every-boot