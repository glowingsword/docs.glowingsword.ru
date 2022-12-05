

# Ошибка IP TEMP BANNED при IMAP-авторизации с определённого IP на серверах с cPanel
## Характерный признак проблемы с блокировкой IP со стороны cphulkd
Видим в трафике с конкретного IP к серверу, на котором расположен соответсвующий ящик с не работающей авторизацией текст вроде 

```bash
2 NO [ALERT] LOGIN DENIED -- EXCESSIVE FAILURES -- IP TEMP BANNED
```

## Изучение логов
Смотрим лог  /usr/local/cpanel/logs/cphulkd.log, ищем наш IP.

## Cнятие блокировки
Убедившись, что он залочен, делаем 
```bash
/usr/local/cpanel/scripts/cphulkdwhitelist OUR_IP
```
где ==OUR_IP== - наш IP, при подключении с которого не работает авторизация. 

После чего проверяем работает ли авторизация с проблемного хоста, видим что работает, а значит мы - молодцы. И идём пить кофе с печенькой...

## Если блокировку снять не удоалось

Если ==cphulkdwhitelist== пишет

```bash
cphulkd is not enabled
```
Проверяем состояние сервиса
```bash
systemctl status cphulkd.service
```
и наличие процессов


== "Команда"
    ```bash
    ps auxf|grep cPhulkd
    ```

== "Результат"
    ```bash
    root      24718  0.0  0.0  51336 12952 ?        S    Jul30   0:13 cPhulkd - processor
    root      24719  0.3  0.0  65416 28264 ?        S    Jul30  29:12  \_ cPhulkd - dbprocessor
    root       9530  1.1  0.0  64192 24904 ?        S    17:48   0:03  \_ cPhulkd - processor - http socket
    root      55852  0.2  0.0  51600 12428 ?        S    17:53   0:00  \_ cPhulkd - processor - http socket
    ```

Если процессы запущены, служба в active, несмотря на то, что сервис находится в состоянии disabled

```bash
Loaded: loaded (/etc/systemd/system/cphulkd.service; disabled; vendor preset: disabled)
```
логинимся в WHM, и проверяем, а не отключена ли на сервере данная служба. 

В теории, если сервис cphulkd.service находится в состоянии disabled - значит он отключен в WHM. 
В таком случае и cphulkd.service должен быть остановлен.

Если в WHM cphulk в OFF, останаливаем его:

```bash
systemctl stop cphulkd.service
```
Проверяем, что процессы cPhulkd на сервере больше не выполняются. 
Проверяем, актуальна ли проблема. Убеждаемся, что не актуальна, а значит мы таки молодцы, заслужили свою печеньку.

## Полезная информация 
https://docs.cpanel.net/knowledge-base/security/cphulk-management-on-the-command-line/