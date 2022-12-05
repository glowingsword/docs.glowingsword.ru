# Установка atop на Centos

Ставим atop 

``` bash
yum install atop
```
Если нужен другой интервал обновления информации в логах(600 секунд, это 10 минут, что многовато для многих случаев)
``` bash
sed -i 's/INTERVAL=600/INTERVAL=10/g'  /etc/sysconfig/atop
```
Включаем сервис в автохагрузку
``` bash
systemctl enable atop
```

Запускаем atop

```
systemctl start atop
```

## Однострочник делающий то же

``` bash
yum -y install atop;sed -i 's/INTERVAL=600/INTERVAL=10/g'  /etc/sysconfig/atop; chkconfig --level 12345 atop on; service atop start
```