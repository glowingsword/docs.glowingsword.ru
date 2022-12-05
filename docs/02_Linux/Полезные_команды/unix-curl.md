---
title:  "Смотрим что передаётся в unix-сокете  какой-либо службы с помощью curl"
authors: 
 - glowingsword
tags:
 - Linux
 - Полезные команды
date: 2020-06-11
---
Выполняем команду

```bash
curl --unix-socket /run/gunicorn.sock localhost
```

где вместо /run/gunicorn.sock указываем путь к интересующему нас соккету.