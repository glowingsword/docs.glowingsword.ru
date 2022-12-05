---
title:  "Ошибка Transaction Check Error при установке perl-XML-LibXML или Munin на серверах с CentOS 6"
authors: 
 - glowingsword
tags:
 - Centos 6
date: 2020-06-04
---

# Ошибка Transaction Check Error при установке perl-XML-LibXML или Munin на серверах с CentOS 6

Возникает при установке munin, а также при установке perl-XML-LibXML, или любого другого пакета с данной зависимостью. 
Данная ошибка связана с использованием некоторых сторонних репозиториев, в частности rpmforge.

Проявлется она так:

```bash
# yum install munin-node
Transaction Check Error:
  file /usr/share/man/man3/XML::SAX::Base.3pm.gz conflicts between attempted installs of perl-XML-SAX-0.96-7.el6.noarch and perl-XML-SAX-Base-1.04-1.el6.rf.noarch
  file /usr/share/man/man3/XML::SAX::Exception.3pm.gz conflicts between attempted installs of perl-XML-SAX-0.96-7.el6.noarch and perl-XML-SAX-Base-1.04-1.el6.rf.noarch
```

Для решения проблемы выполняем:
```bash
echo 'exclude=perl-XML-SAX-Base' >>  /etc/yum.repos.d/rpmforge.repo
```
или отключением репозиторий rpmforge(указываем disable вместо enable в конфиге rpmforge.repo), если его использование не является необходимостью.

После чего делаем

```bash
yum update
```
```bash
yum install munin-node
```