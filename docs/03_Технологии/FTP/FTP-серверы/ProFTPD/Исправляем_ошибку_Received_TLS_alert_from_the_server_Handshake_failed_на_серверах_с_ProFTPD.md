---
title:  Обновляем информацию о часовых поясах в Ubuntu
authors: 
 - glowingsword
tags:
 - FTP
 - FTP-серверы
 - ProFTPD
 - Ошибки ProFTPD
date: 2020-04-19
---
# Исправляем ошибку Received TLS alert from the server Handshake failed на серверах с ProFTPD

При подключении к некоторым серверам по протоколу FTP с помощью FTP-клиента FileZilla иногда возникает ошибка вида
``` bash
Status: Initializing TLS... Error: Received TLS alert from the server: Handshake failed (40) Error: Could not connect to server
```
для решения данной проблемы на серверах с панелью управления ispmanager
достаточно в файле /etc/proftpd.conf заменить директиву вида
``` bash
TLSCipherSuite ALL:!ADH:!DES:!SSLv2:!SSLv3
```
на следующую
``` bash
TLSCipherSuite ALL:!ADH:!DES
```
или удалить данную строку, и добавить вместо неё
``` bash
TLSProtocol SSLv23
```
после чего перезапустить proftpd.

В остальных случаях действуем в соответствии с руководством
<http://wpguru.co.uk/2015/02/how-to-fix-proftp-handshake-trouble-in-plesk/>
