# Реинициализация mysql на Centos 7

Если предварительно нужно сдампить базы и таблицы, см. "Дамп баз данных Mysql"

Стопаем мускуль и проверяем, что он стопнут

``` bash
systemctl stop mysql
```
Проверяем, что действительно стопнут

``` bash
systemctl status mysql;ps auxfS|grep mysqld|grep -v grep
```
Последняя команда должна показать что мускуль остановлен, а также отсутствие процессов mysqld и mysqld_safe.

Переименовываем каталог /var/lib/mysql

``` bash
mv /var/lib/mysql /var/lib/mysql_backup_$(LC_TIME='en_US.UTF-8' date '+%Y%m%d')
```

Создаём нужный каталог, и указываем ему верного владельца

Mysql < 5.7

``` bash
mkdir /var/lib/mysql
mkdir /var/lib/mysql/mysql
chown -R mysql:mysql /var/lib/mysql 
```

Mysql >= 5.7

``` bash
mkdir /var/lib/mysql
chown -R mysql:mysql /var/lib/mysql 
```

Инициализуем базу.

Для mysql < 5.7 делаем

``` bash
mysql_install_db
```

Для mysql >= 5.7 выполняем

``` bash
mysqld --initialize --user=mysql
```
В процессе будет сформирован пароль root, в выхлопе ищем

[Note] A temporary password is generated for root@localhost: наш_пароль

изпользуем его для одноразового подключения, и меняем пароль root

``` bash
systemctl start mysql
```
``` bash
mysql -uroot -p'наш_пароль'
```
``` mysql
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('NEW_PASS');
FLUSH PRIVILEGES;
```

где NEW_PASS - какой-то пароль.

Делаем на всякий случай

``` bash
mysql_upgrade -u root -pNEW_PASS
```

Если нужно после реиницализации восстановить базы из полученного ранее дампа
``` bash
mysql -uroot -ppNEW_PASS < /root/all-databases_$(LC_TIME='en_US.UTF-8' date '+%Y%m%d').sql
```