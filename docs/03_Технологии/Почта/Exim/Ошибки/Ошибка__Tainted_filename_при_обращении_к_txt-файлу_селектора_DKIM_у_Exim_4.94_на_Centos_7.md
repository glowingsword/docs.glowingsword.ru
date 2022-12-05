---
title: "Ошиба 'Tainted filename' или 'failed to expand dkim_selector' на серверах с Exim 4.94.1"
authors: 
 - glowingsword
tags:
 - Exim
 - Ошибки Exim
 - Centos 7
date: 2020-04-04
---
# Ошиба 'Tainted filename' или 'failed to expand dkim_selector' на серверах с Exim 4.94.1

Если после обновления до exim 4.94 на Centos 7 в лог exim стало падать что-то вроде 

```bash
2020-06-29 14:53:57 1jpsMH-0003pv-7K Tainted filename '/etc/exim/ssl/some.domain.txt'
2020-06-29 14:53:57 1jpsMH-0003pv-7K failed to expand dkim_selector: failed to open /etc/exim/ssl/some.domain.txt: Permission denied (euid=93 egid=93)
```
Обратить  внимание в тексте ошибки необходимо именно на  ключевые фразы ==Tainted filename== и ==failed to expand==, так как полный текс ошибок при открытии разных файлов будет немного отличаться, а данные ключевые фразы при этом служат надёжным маркером того, что мы имеем дело именно с данным багом в exim.

Сама проблема, и причины её возникновения, хорошо описаны в файле https://git.exim.org/exim.git/blob/HEAD:/src/README.UPDATING и на странице https://discuss.flarum.org/d/24326-smtp-451-temporary-local-problem-please-try-later

На всякий случай проверяем есть ли нужный файл, и доступен ли он от имени юзера exim

```bash
ls -lhd /etc/exim/ssl/reddogcrm.ru.txt
```
получаем 

```
-rw------- 1 exim exim 319 окт 10  2018 /etc/exim/ssl/some.domain.txt
```
```bash
sudo -u exim cat /etc/exim/ssl/reddogcrm.ru.txt|wc -c
```

получаем не нулевое значение(как правило там больше ста знаков должно быть).

Как видно, файл доступен для чтения для пользователя exim. И права у него корректные. Значит мы имеем дело данной проблемой конкретной версии exim.

Проверяем версию exim 

```bash
yum list all|grep -E '^exim\.\w[0-9]'
```
получаем что-то вроде 

```bash
exim.x86_64                               4.94-1.el7                     @epel
```


Также при проявлении данной проблемы наблюдаются проблемы с оптравкой писем через exim на серверах с панелями управления вроде Ispmanager или VestaCP, или прооблемы с подписыванием писем DKIM. 

Для решения данной проблемы необходимо откатить версию exim на старую версию exim 3.93.3, где нет этой gроблемы.

```bash
wget https://ca1.dynanode.net/exim-4.93-3.el7.x86_64.rpm
```

```
rpm -Uvh --oldpackage exim-4.93-3.el7.x86_64.rpm
```

и не забываем про 

```bash
yum versionlock exim-*
```

подробности см. в 