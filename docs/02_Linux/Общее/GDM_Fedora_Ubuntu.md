---
title: 'Убираем пользователя из списка пользователей в GDM в Fedora и Ubuntu'
authors: 
 - glowingsword
tags:
 - Linux
 - GDM
date: 2020-04-30
---

# Убираем пользователя из списка пользователей в GDM в Fedora и Ubuntu

Для этого необходимо открыть файл ==/var/lib/AccountsService/users/<username>== , где ==<username>== - имя соответствюущего пользователя, и заменить

```ini
SystemAccount=false
```
на

```ini
SystemAccount=true
```
после чего перезапустить ПК. 

Если соответствующего файла ранее не было,
нужно просто добавить в созданный файл

```ini
[User] 
SystemAccount=true
```
