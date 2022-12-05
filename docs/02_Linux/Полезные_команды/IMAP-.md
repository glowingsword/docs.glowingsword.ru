---
title:  "Смотрим названия IMAP-каталогов в .maildir с кириллическими символами"
authors: 
 - glowingsword
tags:
 - Linux
 - Полезные команды
date: 2020-06-14
---

# Смотрим названия IMAP-каталогов в .maildir с кириллическими символами

Название каталогов хранятся в UTF-7, что-бы глянуть каталоги необходимо войти в .maildir и выполнить

```bash
find . -maxdepth 1 -type d|cut -c4-| sed 's/\&/+/g'|iconv -f utf-7
```