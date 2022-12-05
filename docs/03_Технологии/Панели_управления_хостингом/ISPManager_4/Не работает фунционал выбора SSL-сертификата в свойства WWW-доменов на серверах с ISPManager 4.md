---
title: "Не работает фунционал выбора SSL-сертификата в свойства WWW-доменов на серверах с ISPManager 4"
authors: 
 - glowingsword
tags:
 - "ISPManager 4"
 - SSL
date: 2022-07-22
---

# Не работает фунционал выбора SSL-сертификата в свойства WWW-доменов на серверах с ISPManager 4

Как правило, проблема возникает из-за того, что HTTPS-запросы обрабатывает httpd.

=== "Проверка"
    ```bash
    netstat -lnp|grep :443
    ```

=== "Результат"
    ```bash
    # netstat -lnp|grep :443
    tcp        0      0 some_ip:443          0.0.0.0:*                   LISTEN      3592/httpd  
    ```

где some_ip - это основной IP-адрес сервера, на котором производятся работы.

Для переключения работы с https на nginx **включаем**(это очень важно, включаем, предварительно **не отключая**, т.е. уже включенный) nginx на странице раздела "Возможности" панели управления ISPManager.

Если после этого переключение не произошло, смотрим нет ли в конфиге панельки опции WebNginxNoSSL

=== "Проверка"
    ```bash
    grep WebNginxNoSSL / /usr/local/ispmgr/etc/ispmgr.conf
    ```

=== "Результат"
    ```bash
    -bash-4.1# grep WebNginxNoSSL / /usr/local/ispmgr/etc/ispmgr.conf
    /usr/local/ispmgr/etc/ispmgr.conf:Option WebNginxNoSSL
    ```

На всякий случай создаём резервную копию конфигурационного файла панели 

```bash
cp /usr/local/ispmgr/etc/ispmgr.conf /usr/local/ispmgr/etc/ispmgr.conf_backup_$(date +%Y-%m-%d)
```

после чего удаляем из **/usr/local/ispmgr/etc/ispmgr.conf** строку с ```Option WebNginxNoSSL```.

после чего убиваем процессы панели

=== "Поиск pid процессов"
    ```bash
    ps auxf|grep ispmgr|grep -v exim
    ```

=== "Что примерно видим в ответ на команду"
    ```bash
    -bash-4.1# ps auxf|grep ispmgr|grep -v exim
    root      3447  0.0  0.1  39152  2196 ?        Ss   13:02   0:00 /usr/local/ispmgr/sbin/ihttpd some_ip 1500
    root      3449  0.0  0.6 468664 13976 ?        Sl   13:02   0:00 /usr/local/ispmgr/bin/ispmgr
    ```

После чего

```bash
kill -15 3449 3447
```
где 3449 и 3447 – PID интересующий нас процессов.

Проверяем, что эти процессы остановились с помощью команды, которой мы их искали.
Если они ещё висят, завершаем их принудительно

```bash
kill -9 3449 3447
```

затем запускаем панель 

```bash
/usr/local/ispmgr/sbin/ihttpd some_ip 1500
```

и включаем ssl-сертификат для нужного домена. 

Должно получится примерно так 

```
-bash-4.1# netstat -lnp|grep :443
tcp        0      0 IPv4:443          0.0.0.0:*                   LISTEN      4634/nginx  
```

В свойствах WWW-домена в ISPManager 4 должно появиться поле "SSL сертификат" с выпадающим списком для выбора нужного сертификата из списка.