---
title: 'Вход в панель управления ISPManager, если нет пароля root, но есть root-доступ к серверу(метод с созданием пользователя toor)'
authors: 
 - glowingsword
tags:
 - 'ISPManager 4'
 - Авторизация без пароля
date: 2020-04-04
---
## Вход в панель управления ISPManager, если нет пароля root, но есть root-доступ к серверу(метод с созданием пользователя toor)

Создаём пользователя(для Debian вместо wheel указываем sudo)

``` bash
  useradd toor -u 0 -g 0 -o -d /root/ -G bin,daemon,sys,adm,disk,wheel
  passwd toor (меняем на рутовый пароль из Sd)
```

По завершению работ, удаляем:

``` bash
  userdel -f toor
```