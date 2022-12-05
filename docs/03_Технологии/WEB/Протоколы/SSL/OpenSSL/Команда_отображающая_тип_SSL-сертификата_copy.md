---
title: 'Команда отображающая тип SSL-сертификата'
authors: 
 - glowingsword
tags:
 - OpenSSL
 - полезные команды
date: 2020-04-04
---
# Команда отобращающая цепочку ssl-сертификатов

``` bash
openssl s_client -host $DOMAIN -port 443 -prexit -showcerts
```