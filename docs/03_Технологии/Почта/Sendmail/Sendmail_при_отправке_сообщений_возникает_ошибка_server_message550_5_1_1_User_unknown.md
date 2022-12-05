---
title: 'Sendmail при отправке сообщений возникает ошибка server message: 550 5.1.1 User unknown'
authors: 
 - glowingsword
tags:
 - semdmail
 - ошибки semdmail
date: 2020-04-21
---
# Sendmail при отправке сообщений возникает ошибка server message: 550 5.1.1 User unknown

Для решения данной проблемы необходимо добавить в `/etc/mail/sendmail.mc` записи вида

``` s
define(\`MAIL_HUB',\`mydomain.ru.')dnl 
define(\`LOCAL_RELAY',\`mydomain.ru.')dnl
```
после чего выполниить команды
``` bash
make -C /etc/mail 
```
``` bash
service sendmail restart
```
для сборки конфигурацинного файла sendmail и перезапуска службы `sendmail`.

<http://sc0rp1us.blogspot.md/2012/05/sendmail-centos-localhost.html>
<http://forum.lissyara.su/viewtopic.php?t=21720>
