---
title: "Ошибка вида smarthost_transport defer (-53): retry time not reached for any host for 'yandex.ru' в логе exim при отправке сообщения"
authors: 
 - glowingsword
tags:
 - Exim
 - Ошибки Exim
 - Centos 7
date: 2020-08-12
---

# Ошибка вида smarthost_transport defer (-53): retry time not reached for any host for 'yandex.ru' в логе exim при отправке сообщения

## Признаки наличия проблемы
Если в логах видим 

```log
2020-08-12 15:53:56 1k5mjv-0006A0-9P == some_non_exists_addr@yandex.ru R=dnslookup T=remote_smtp defer (-53): retry time not reached for any host for 'yandex.ru'
```

## Наиболее очевидная причины проявления поблемы
Как правило, такая ошибка говорит о том, что у нас побились базы exim. 

## Удаление битых файлов базы exim db, с последующим перезапуском exim
Делаем 

```bash
cd /var/spool/exim/db
```
```bash
systemctl stop exim
```
```bash
rm retry retry.lockfile wait-remote_smtp wait-remote_smtp.lockfile
```
```bash
systemctl start exim
```

## Что делать, если команды из предыдущего раздела не помогли

Изредка бывате так, что описанные выше действия не решают проблему.

### Проблема с доп. IP 
Если при отправке с одного из IP-адресов(основного IP-адреса сервера) сообщения отправляются нормально, а с дополнительного не отправляюся, стоит проверить а добавлен ли он на сервер.

На сервере делаем

```bash
grep some.domain /etc/exim/domainips
```
где some.domain – наш домен.

Видим в выхлопе нужный нам IP, к примеру

```bash
some.domain :192.168.333.77
```

где вместо 192.168.333.77 должен быть указан нужный нам IP.

Смотрим добавлен ли адрес на сервер

```bash
ip a|grep 192.168.333.77
```

Если не добавлен дополнительный IP, добавляем его на сервер(вручную, или с помощью панели управления сервером, тут всё зависит от вашей конфигурации)

После чего проверяем с другого хоста, доступен ли данный IP по сети

```bash
ping 192.168.333.77
```

и доступен ли по нему smtp

```bash
telnet 192.168.333.77 25
```

Если IP не доступен, проверяем на не заблокирован ли он в iptables/firewalld. И не светится ли он с другого сервера в той же сети.

После того, как smtp-сервер нужного нам хоста станет доступным по доп.IP, выполняем команды, представленные в разделе [Удаление битых файлов базы exim db, с последующим перезапуском exim](#Удаление битых файлов базы exim db, с последующим перезапуском exim).

### Проблема с SSL-сертификатом exim

Бывает такое, что проблема возникает из-за не правильно выставленных прав на ssl-сертификат.

В таком случае делаем


=== "Команда"
```bash
grep -P 'tls_certificate|tls_privatekey' /etc/exim/exim.conf
```
=== "Результат"
    ```bash
    tls_certificate = ${if exists{/etc/exim/ssl/${tls_sni}.crt}{/etc/exim/ssl/${tls_sni}.crt}{/etc/exim/ssl/exim.crt}}
    tls_privatekey = ${if exists{/etc/exim/ssl/${tls_sni}.key}{/etc/exim/ssl/${tls_sni}.key}{/etc/exim/ssl/exim.key}}
    ```
И проверяем права на файлы /etc/exim/ssl/exim.crt и /etc/exim/ssl/exim.key, а также /etc/exim/ssl/some.domain.crt /etc/exim/ssl/some.domain.key

Права должны выглядеть так на основные сертификат и ключ

```bash
-r--r--r-- 1 exim exim 4.0K Jan  9  2019 exim.crt
-r-------- 1 exim exim 3.2K Jan  9  2019 exim.key
```

И так на сертификат и ключ для домена(технически достаточно права на чтение(r) для пользователя exim, право на запись можно и не указывать, оно добавляется панелью ISPManager, если у вас сервер с панелью управления хостингом)

```bash
-rw------- 1 exim exim 5.7K Sep 16  2019 some.domain.crt
-rw------- 1 exim exim 3.3K Sep 16  2019 some.domain.key
```

Если права указаны не верно, исправляем. Затем выполняем команды из [Удаление битых файлов базы exim db, с последующим перезапуском exim](/Технологии/Почта/Exim/Ошибки/Ошибка retry time not reached for any host for в логе при отравке сообщения#Удаление битых файлов базы exim db, с последующим перезапуском exim).

## Полезные ссылки

<http://hostciti.net/support/administratoram/mail/19.html>