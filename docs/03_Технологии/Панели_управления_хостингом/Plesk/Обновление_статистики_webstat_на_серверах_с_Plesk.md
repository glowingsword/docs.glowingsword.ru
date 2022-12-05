---
title: 'Обновление статистики webstat на серверах с Plesk'
authors: 
 - glowingsword
tags:
 - Plesk
date: 2020-04-04
---
# Обновление статистики webstat на серверах с Plesk

Обновляем статистику для одного домена
``` bash
/usr/local/psa/admin/sbin/web_statistic_executor --calculate-domain mydomain.ru
```

Также стоит учитывать, что если сайт доступен только по протоколу https, то статистику нужно проверять по адресу

<https://mydomain/plesk-stat/webstat-ssl/>

а не

<https://mydomain/plesk-stat/webstat/>


Полезные материалы
<https://kb.plesk.com/en/115166> 
<https://kb.plesk.com/en/125318>
<https://kb.plesk.com/en/116256>
