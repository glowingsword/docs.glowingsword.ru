---
title: Добавление подписи DKIM
authors: 
 - glowingsword
tags:
 - Exim
 - Настройка Exim
 - Почтовый серер
date: 2020-04-04
---
# Отключаем IPv6 в exim

## Отключаем IPv6 для Exim в Debian

Для того, что-бы отключить поддержку IPv6 в exim необходимо в
конфигурационном файле /etc/exim4/exim4.conf.template (до начала секции
begin acl) добавить директиву

disable_ipv6 = true

после чего сохранить произведённые изменения и перезапустить exim
командой

service exim4 restart

## Отключаем IPv6 для Exim в Centos

Для того, что-бы отключить поддержку IPv6 в exim необходимо в
конфигурационном файле /etc/exim/exim.conf (до начала секции begin acl)
добавить директиву

disable_ipv6 = true

после чего сохранить произведённые изменения и перезапустить exim
командой

service exim restart