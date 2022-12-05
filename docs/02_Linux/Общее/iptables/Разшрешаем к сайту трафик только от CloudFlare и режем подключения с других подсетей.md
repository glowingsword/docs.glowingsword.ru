---
title:  "Разшрешаем к сайту трафик только от CloudFlare и режем подключения с других подсетей"
authors: 
 - glowingsword
tags:
 - Linux
 - iptables
 - ipset
 - Cloudflare
date: 2021-01-31
---

# Разшрешаем к сайту трафик только от CloudFlare и режем подключения с других подсетей

## Установка ipset
Устаналиваем ipset, если не поставили его ранее

Для Centos

```bash
yum install ipset
```

Для Ubuntu/Debian

```bash
apt install ipset
```

## Cоздаём список подсетей с наименованием cloudflare4

```bash
ipset create cloudflare4 hash:net
```

```bash
for net in  103.31.4.0/22 103.22.200.0/22 162.158.0.0/15 108.162.192.0/18 173.245.48.0/20 198.41.128.0/17 131.0.72.0/22 190.93.240.0/20 104.16.0.0/12 188.114.96.0/20 141.101.64.0/18 103.21.244.0/22 197.234.240.0/22 172.64.0.0/13; do ipset add cloudflare4 $net;done
```

Проверяем, что у нас получилось
```bash
ipset list cloudflare4
```

Должно получиться так

```yaml
Name: cloudflare4
Type: hash:net
Revision: 6
Header: family inet hashsize 1024 maxelem 65536
Size in memory: 1280
References: 0
Members:
131.0.72.0/22
198.41.128.0/17
104.16.0.0/12
173.245.48.0/20
103.21.244.0/22
162.158.0.0/15
197.234.240.0/22
190.93.240.0/20
141.101.64.0/18
103.22.200.0/22
103.31.4.0/22
172.64.0.0/13
188.114.96.0/20
108.162.192.0/18
```

Объявляем переменную ==domain==, в качестве значения указываем доменное имя сайта, доступ к которому должен быть только у IP из подсетей системы защиты CloudFlare.

```bash
domain=example.site
```

## Добавляем фильтрующие правила

Теперь нам нужно добавить правил, что разрешат подключения к сайту с серверов защиты, но заблокируют все остальные подключения.

### Правило, пропускающее трафик к сайту с защищаемого домена

```bash
iptables -I INPUT 1 -m set --match-set cloudflare4 src -p tcp -m multiport --dports 80,443 -m string --string "${domain}" --algo kmp --to 65535 -j ACCEPT
```
### Правило, режущее все обращения к домену, что прилетают с IP-адресов, что не входят в список подсетей защиты

```bash
iptables -I INPUT 2 -p tcp -m tcp -m multiport --dports 80,443 -m string --string "${domain}" --algo kmp --to 65535 -j DROP
```