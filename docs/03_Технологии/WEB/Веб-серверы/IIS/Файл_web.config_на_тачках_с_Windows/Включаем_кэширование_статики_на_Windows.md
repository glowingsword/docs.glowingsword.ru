---
title: 'Включаем кэширование статики на Windows'
authors: 
 - glowingsword
tags:
 - IIS
 - Настройка веб-сервера IIS
date: 2020-04-05
---
# Включаем кэширование статики на Windows

Для включения кэширования статики добавляем в web.config директивы

``` xml
<staticContent>
        <clientCache cacheControlMode="UseMaxAge" cacheControlMaxAge="7.00:00:00" />
</staticContent>
```

Больше информации по данному вопросу можно найти на странице
<https://www.iis.net/configreference/system.webserver/staticcontent>