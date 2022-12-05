---
title: 'Смотрим статистику сетевых интерфейсов'
authors: 
 - glowingsword
tags:
 - Linux
 - netstat
 - ss
date: 2020-04-30
---
# Смотрим статистику сетевых интерфейсов
Бывает такое, что нужно быстро выяснить на каком сетевом интерфейсе наблюдается повышенная активность

В таком случае нас может сдорово выручить команда 

netstat -i

Если нам хочется красивый выхлоп в json, и с сортировкой по количеству принятых/отправленных байт или пакетов, можем вместо netstat испльзовать ip и jq.

Получаем статистику по количеству отправленных байт для 5 наиболее активных интерфейсов


``` bash
ip -j -o -s lin | jq --compact-output '.[] | {ifname: .ifname, tx_bytes:.stats64?.tx.bytes}'|jq -s ''|jq 'sort_by(.tx_bytes)|.[-5:]'
```

Получаем статистику по количеству отправленных пакетов для 5 наиболее активных интерфейсов

``` bash
ip -j -o -s lin | jq --compact-output '.[] | {ifname: .ifname, tx_packets:.stats64?.tx.packets}'|jq -s ''|jq 'sort_by(.tx_packets)|.[-5:]'
```

Получаем статистику по количеству принятых байт для 5 наиболее активных интерфейсов


``` bash
ip -j -o -s lin | jq --compact-output '.[] | {ifname: .ifname, rx_bytes:.stats64?.rx.bytes}'|jq -s ''|jq 'sort_by(.rx_bytes)|.[-5:]'
```

Получаем статистику по количеству принятых пакетов для 5 наиболее активных интерфейсов

``` bash
ip -j -o -s lin | jq --compact-output '.[] | {ifname: .ifname, rx_packets:.stats64?.rx.packets}'|jq -s ''|jq 'sort_by(.rx_packets)|.[-5:]'
```
