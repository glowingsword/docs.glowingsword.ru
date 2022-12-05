---
title: 'Ошибка FATAL Library libmgr linked to lib/libmgr.so conflicting with already loaded one на серверах с ISPManager 5'
authors:
 - glowingsword
tags:
 - ISPManager
 - ISPManager 5
date: 2020-07-15
---
# Ошибка FATAL Library libmgr linked to lib/libmgr.so conflicting with already loaded one на серверах с ISPManager 5

!!! info 'К сведению...'
    Ошибка "Library libmgr linked to lib/libmgr.so. conflicting with already loaded one" говорит о том, что на сервере присутствуют два пакета COREmanager.

## Проверяем нет ли у нас дубля пакета coremanager

### Мой любимый способ поиска дублей coremanager

Выполняем команду

=== "Команда"
    ```bash
    rpm -qa | grep coremanager-5
    ```

=== "Результат"
    ```bash
    [root@mgr5]# rpm -qa | grep coremanager-5
    coremanager-5.66.2-2.el6.x86_64
    coremanager-5.66.1-1.el6.x86_64
    ```

### Тоже неплохой способ поиска дубля coremanager

```bash
package-cleanup --dupes |grep coremanager-5
```
Если в результате будет видны две разных версии одного и того же пакета, значит у нас проблема с задублированным пакетом.

Для решения данной проблемы необходимо удалить без зависимостей более старый пакет:

```bash
rpm --nodeps -e coremanager-5.66.1-1.el6.x86_64
```

## Обновление кэша пакетов, и повторное обновлнеие обновление:

```bash
cd /usr/local/mgr5 && sbin/pkgupgrade.sh coremanager 
```

Обновление следует производить очень аккуратно, внимательно читая, что происходит.

## Возможные подводные камни и способы их обхода

Бывает, что в процессе возникает предупреждение

```bash
Warning: RPMDB altered outside of yum
```
и обновление не идёт. 

ВЫполняем 

```bash
yum clean all
```
затем 

```bash
yum history new
```

Если в процессе возникнет предупреждение

```bash
There are unfinished transactions remaining. You might consider running yum-complete-transaction, or "yum-complete-transaction --cleanup-only" and "yum history redo last", first to finish them. If those don't work you'll have to try removing/installing packages by hand (maybe package-cleanup can help).
```

выполняем 

```bash
yum install yum-utils
```

```bash
yum-complete-transaction --cleanup-only
```

```bash
yum clean all
```

После фикса повторно возвращаемся к выполнению пункта "Обновление кэша пакетов, и повторное обновлнеие обновление".

http://forum.ispsystem.ru/showthread.php?31018-%D0%9D%D0%B5-%D0%BF%D0%BE%D0%B4%D0%BD%D0%B8%D0%BC%D0%B0%D0%B5%D1%82%D1%81%D1%8F-ISPManager-%D0%BF%D0%BE%D1%81%D0%BB%D0%B5-%D0%BE%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F/page2