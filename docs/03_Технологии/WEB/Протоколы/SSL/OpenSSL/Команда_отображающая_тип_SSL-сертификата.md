---
title: 'Команда отображающая тип SSL-сертификата'
authors: 
 - glowingsword
tags:
 - OpenSSL
 - полезные команды
date: 2020-04-04
---
# Команда отображающая тип SSL-сертификата
``` bash
openssl x509 -issuer -noout -in mysite.crt
```