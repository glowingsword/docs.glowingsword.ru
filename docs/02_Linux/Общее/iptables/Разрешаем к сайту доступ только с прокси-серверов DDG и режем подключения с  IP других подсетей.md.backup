---
title:  "Разрешаем к сайту доступ только с прокси-серверов DDoS Guard(DDG) и режем подключения с  IP других подсетей"
authors: 
 - glowingsword
tags:
 - Linux
 - iptables
 - ipset
 - DDG
date: 2021-01-31
---

# Разрешаем к сайту доступ только с прокси-серверов DDoS Guard(DDG) и режем подключения с  IP других подсетей

Указываем переменную с именем нашего домена

```bash
domain=domain.example
```

Выполняем

```bash
iptables -I INPUT 1 -s 77.220.207.192/27 -p tcp -m tcp -m multiport --dports 80,443 -m string --string "${domain}" --algo kmp --to 65535 -j ACCEPT 
```
```bash
iptables -I INPUT 2 -s 186.2.160.0/24 -p tcp -m tcp -m multiport --dports 80,443 -m string --string "${domain}" --algo kmp --to 65535 -j ACCEPT 
```
```bash
iptables -I INPUT 3 -s 186.2.164.0/24 -p tcp -m tcp -m multiport --dports 80,443 -m string --string "${domain}" --algo kmp --to 65535 -j ACCEPT 
```
```bash
iptables -I INPUT 4 -s 77.220.207.224/27 -p tcp -m tcp -m multiport --dports 80,443 -m string --string "${domain}" --algo kmp --to 65535 -j ACCEPT 
```
```bash
iptables -I INPUT 5 -s 89.108.67.0/24 -p tcp -m tcp -m multiport --dports 80,443 -m string --string "${domain}" --algo kmp --to 65535 -j ACCEPT 
```
```bash
iptables -I INPUT 6 -p tcp -m tcp -m multiport --dports 80,443 -m string --string "${domain}" --algo kmp --to 65535 -j DROP
```