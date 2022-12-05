---
title: 'Ошибка "host lookup did not complete"'
authors: 
 - glowingsword
tags:
 - Exim
 - Ошибки Exim
date: 2021-06-03
---

# Ошибка "host lookup did not complete"

К примеру, у нас ошибка

```bash
2021-06-02 12:08:38 H=our.super_mailer.com [127.0.0.88] sender verify defer for <ourmail@domain.example>: host lookup did not complete
```

Проверяем, как резолвится домен

```bash
exim -bt 'ourmail@domain.example'
```

Заодно делаем 


```bash
exim -bv 'ourmail@domain.example'
```

для проверки адреса в режиме address verification mode.

Если видим 

```bash
ourmail@domain.example cannot be resolved at this time: host lookup did not complete
```

значит e-mail не резолвился, должно быть что-то вроде

```bash
ourmail@domain.example
  router = hosting, transport = remote_smtp
  host super_mailer.com [127.0.0.87]
```
Бывает, что эта проблема носит временный характер и через время перестаёт проявляться, бывает что перманентный. В зависимости от того, вы админите почтовик с не резолвящимся адресом, или это адрес ваших партнёров/контрагентов, решаем проблему на своей стороне, или связываемся с партнёрами что админят почтовый сервис, адрес которого не резолвится, и просим их пофиксить проблему.
