---
title: 'Исправляем ошибку вида "Received TLS alert from the server: Handshake failed (40)" на серверах с ProFTPD и ISPManager'
authors: 
 - glowingsword
tags:
 - ISPManager 5
 - ProFTPD
date: 2020-04-05
---
# Исправляем ошибку вида "Received TLS alert from the server: Handshake failed (40)" на серверах с ProFTPD и ISPManager

Для решения данной проблемы в файле /etc/proftpd.conf необходимо закомментировать параметр вида

1.  TLSCipherSuite ALL:!ADH:!DES:!SSLv2:!SSLv3

и добавить следующие параметры

TLSProtocol SSLv23 TLSRenegotiate required off

после чего перезапустить proftpd.

Полезная информация:
<http://wpguru.co.uk/2015/02/how-to-fix-proftp-handshake-trouble-in-plesk/>