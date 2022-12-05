---
title: "Обновление mysql до mysql 8.0 на Centos 7"
authors: 
 - glowingsword
tags:
 - MySQL
 - "Полезные ссылки на информацию о MySQL"
date: 2020-04-04
---

# Обновление mysql до mysql 8.0 на Centos 7

## Подготовительне действия

### Подключаем репозиторий mysql-community

```bash
wget https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm 
```
```bash                                                                       
yum install mysql80-community-release-el7-3.noarch.rpm 
```
### Смотрим тчо за версия mariadb/mysql у нас установлена

Проверяем что за версия mariadb установлена на сервере(по умолчанию 5.5 идёт с Centos 7)

```bash
rpm -qa | grep -i -P '^mariadb-' 
```

если команда не возвращает результат, значит кто-то уже сменил mariadb на mysql на этом сервере, делаем 


```bash
rpm -qa | grep -i -P '^mysql-' 
```

### Создаём резервные копии конфигурацнного файла и баз данных
Бэкапим старый конфиг mysql

```bash
cp /etc/my.cnf /etc/my.cnf_backup_$(LC_TIME='en_US.UTF-8' date '+%Y%m%d')   
```

Дампим на всякий случай все базы в общий файл дампа

```bash
mysqldump --events --routines --triggers --all-databases > /root/alldb.sql 
```

Останаливаем mariadb

```bash                                                                                                                          
systemctl stop mariadb
```

копируем на всякий случай содержмиое ==/var/lib/mysql== в каталог вида ==/var/lib/mysql_backup_SOME_DATE==

```bash
cp -R /var/lib/mysql /var/lib/mysql_backup_$(LC_TIME='en_US.UTF-8' date '+%Y%m%d')                                                                      
```

### Удаление пакетов старой версии MySQL(в нашем случае mariadb)

Удаляем без зависимостей старые пакеты Mariadb
```bash
rpm -qa | grep -i -P '^mariadb-'|xargs rpm -e --nodeps 
```

## Установка обновлённой версии MySQL

!!! warn "Нежданчик :)"
    Сразу 8-ка после mariadb 5.5 не заведётся, до 8-ки можно обновится только с MySQL 5.7.9 или совместимой с ней(по версии схемы InnoDB) версии Mariadb, поэтому обновляетмся до 5.7, а с 5.7 до 8.0.


### Смотрим, не включена ли у нас уже какая-либо версия репозитория mysql-community
```bash
yum repolist enabled|grep -P 'mysql[0-9]{1,2}-community' 
```
если включена, и это не mysql57-community, отключаем
```bash
yum-config-manager --disable mysql80-community 
```


### Включаем нужную нам версию репозитория mysql-community

Выполняем

```bash
yum-config-manager --enable mysql57-community 
```
Проверяем, что у нас за версия данного репозитория включена после наших манипуляций

```bash
yum repolist enabled|grep -P 'mysql[0-9]{1,2}-community'    
```

Если этот репозиторий ранее на этом сервере уже подключался когда-то, чистим кэш yum
```bash
yum clean all
```

### Установка промежуточной версии MySQL 5.7

Ставим mysql 5.7
```bash
yum install mysql-community-server mysql-community-libs-compat mysql-community-libs mysql-community-common   
```
Запускаем
```bash
systemctl start mysqld
```
делаем агрейд схемы таблиц mysql
```bash
mysql_upgrade 
```
Осталавливаем Mysql 5.7                                                                                      
```bash                                                                                                                                     
systemctl stop mysqld  
```
и отключаем репозиторий mysql57-community
```bash
yum-config-manager --disable mysql57-community  
```

### Установка нужной нам версии MySQL 8.0

Включаем репозиторий mysql80
```bash
yum-config-manager --enable mysql80-community
```
Включаем и запускаем mysql 8.0
```bash
systemctl enable mysqld
```
```bash
systemctl start mysqld 
```
Проверяем
```bash
mysql -V                                                                                                                               
```
видим что-то вроде 
```bash
mysql  Ver 8.0.21 for Linux on x86_64 (MySQL Community Server - GPL)
```

!!! info "На заметку"
    Как видите, после обновления до MySQL 8.0 мы не запускали mysql_upgrade, хотя при обновлении до любой более старой версии, после обновления необходимо было запускать данную утилиту для обновления схемы таблиц. Но, так было раньше. Для MySQL 8.0 запуск данной утилиты после обновления не имеет смысла, так как использование данной утилиты в этом случае не требуется — при первом запуске MySQL 8.0 на сервере, где уже присутствует MySQL Data Directory(как правило это /var/lib/mysql) восьмая версия MySQL самостоятельно апгрейдит схему таблиц до актуальной версии.

## Включение старого способа авторизации в MySQL

Если ваше приложение не поддерживает новый способ аутентификации MySQL, и ему требуется mysql_native_password для корректной работы с БД mysql(в частности это требуется пока для phpMyAdmin), делаем 

```bash
ALTER USER root IDENTIFIED WITH mysql_native_password BY 'PASSWORD';
```
где вместо PASSWORD указываем наш пароль  пользователя root баз данных mysql.

Если этот механизм аутетификации требуется сделать из коробки доступным всем пользователям mysql, в секцию

```bash
[mysqld]
```
файла ==/etc/my.cnf== добавляем

```bash
default-authentication-plugin=mysql_native_password
```

## Правки для корректнйо работы mysql 8 в конфиге ISPManager 5

Если у нас на сервере стоит ISPManager 5, также потребуется поправить /usr/local/mgr5/etc/ispmgr.conf.d/mysql.conf

Смотрим, что было там

```bash
cat /usr/local/mgr5/etc/ispmgr.conf.d/mysql.conf  
```
Видим 

```bash
path mysql_restart service mariadb restart                                                                                                                     
path mysqld.ini /etc/my.cnf                                                                                                                                    
path mysqld /usr/libexec/mysqld 
```

заменяем на 

```bash
path mysql_restart systemctl restart mysqld                                                                                                                     
path mysqld.ini /etc/my.cnf                                                                                                                                    
path mysqld /sbin/mysqld
```

сохраняем.

## Заключение

Если на сервере ранее стояла не самая актуальная версия phpMyAdmin, нужно обновить и phpMyAdmin. Если нет. обновление MySQL до 8-й версии можно считать оконченным.




