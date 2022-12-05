---
title:  "Обновление curl и libcurl на VPS серверах с Centos 6"
authors: 
 - glowingsword
tags:
 - Centos 6
date: 2020-06-04
---
# Обновление curl и libcurl на VPS серверах с Centos 6

Создаём файл /etc/yum.repos.d/city-fan.repo содержащий

```ini
[CityFan]
name=City Fan Repo
baseurl=http://nervion.us.es/city-fan/yum-repo/rhel$releasever/$basearch/
enabled=1
gpgcheck=0
```
после чего выполняем
```bash
yum clean all
```
```bash
yum install libcurl 
```

Подробности:
<https://www.digitalocean.com/community/questions/how-to-upgrade-curl-in-centos6>