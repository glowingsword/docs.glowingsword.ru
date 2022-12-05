---
title: 'Не работают правила редиректа Worpdress на сервере с Ningx PHP-FPM'
authors: 
 - glowingsword
tags:
 - ISPManager 5
date: 2020-06-14
---
# Не работают правила редиректа Worpdress на сервере с Ningx PHP-FPM

Просто добавляем в конфиг

```bash
       location / { 
           try_files $uri $uri/ /index.php?$args;
               location ~ [^/]\.ph(p\d*|tml)$ {
                       try_files /does_not_exists @php;
               }
       }
```

вместо location /, что создаёт панелька по умолчанию, после чего правила начинают работать корректно.