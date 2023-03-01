---
title: 'Очистка почтовой очереди Exim'
authors: 
 - glowingsword
tags:
 - Exim
 - Настройка Exim
 - Почтовый сервер
date: 2023-03-01
---
# Очистка почтовой очереди Exim

## Ищем почтовый ящик, с которого отправляется больше всего сообщений

Выполняем
```bash
exim -bp | grep -o '<.*>' | sort | uniq -c | sort -n
```

## Ищем домен, с которого отправляется больше всего сообщений

```bash
exim -bp | grep -o '<.*>' |awk -F'@' '{print $2}'|awk -F '>' '{print $1}'| sort | uniq -c | sort -n
```

## Удаляем сообщения, отправленные с почтового ящика или домена

Запускаем

```bash
exiqgrep -i -f target | xargs exim -Mrm
```

где вместо target указываем нужный нам ящик, или домен.

## Удаляем замороженные сообщения из очереди

Используем

```bash
exiqgrep -z -i | xargs exim -Mrm
```
или

```bash
exim -bpu | grep frozen | awk {'print $3'} | xargs exim -Mrm
```

## Удаляем из очереди письма, для которых не указан адрес отправителя

```bash
exim -bp | grep '<>'|awk '{print $3}'|xargs exim -Mrm
```

## Дополнительная информация по теме

[how-to-clear-exim-mail-queue](https://linux-tips.com/t/how-to-clear-exim-mail-queue/137)
[exim-remove-all-messages-from-the-mail-queue](https://www.cyberciti.biz/faq/exim-remove-all-messages-from-the-mail-queue/)