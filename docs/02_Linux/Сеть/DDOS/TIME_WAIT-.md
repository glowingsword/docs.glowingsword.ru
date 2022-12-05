---
title: 'Много висящих соединений со статусом TIME WAIT при отсутствии большого количества запросов к какому-либо сайту'
authors: 
 - glowingsword
tags:
 - Сеть
 - DDOS
date: 2020-04-21
---
# Много висящих соединений со статусом TIME WAIT при отсутствии большого количества запросов к какому-либо сайту

Командой 
``` bash
netstat -antp | grep TIME_WAIT -c
```
смотрим общее количество запросов со статусом TIME_WAIT.

Изучаем `access.log`, если ничего подозрительного нет, смотрим `dmesg`.

Если там мелькают записи вида
``` bash
TCP: time wait bucket table overflow TCP: time wait bucket table
overflow TCP: time wait bucket table overflow TCP: time wait bucket
table overflow TCP: time wait bucket table overflow TCP: time wait
bucket table overflow TCP: time wait bucket table overflow TCP: time
wait bucket table overflow
```
смотрим значение мараметра `tcp_max_tw_buckets`
``` bash
cat /proc/sys/net/ipv4/tcp_max_tw_buckets
```
и при необходимости повышаем его
``` bash
echo 400000 > /proc/sys/net/ipv4/tcp_max_tw_buckets
```
после чего наблюдаем за состоянием сервера.
