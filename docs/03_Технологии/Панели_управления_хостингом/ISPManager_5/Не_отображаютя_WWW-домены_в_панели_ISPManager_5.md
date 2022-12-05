---
title: 'Не отображаютя WWW-домены в панели ISPManager 5'
authors: 
 - glowingsword
tags:
 - ISPManager 5
date: 2020-10-2020
---
# Не отображаютя WWW-домены в панели ISPManager 5

Видим, что WWW-домены куда-то пропали из панели, нужный раздел не отображается, а при дёргании api ISPManager 5 информация о WWW-доменах не отображается, и не изменяется – значит мы столкнулись с данной проблемой.

Возникает она, как правила, из-за выгрузки модуля webdomain, в /usr/local/mgr5/var/ispmgr.log при этом можно увидеть что-то вроде


```log
Oct  5 21:27:50 [16105:1] core WARNING Module 'webdomain' was unloaded
Oct  5 21:27:50 [16105:1] core WARNING Module 'user_add_web' was unloaded
Oct  5 21:27:50 [16105:1] core WARNING Module 'web_access' was unloaded
```

Проверяем, что nginx и httpd(или один httpd, если на сервере была конфигурация без nginx) в настоящее время установлены на сервере, и включены в разделе "Возможности" панели. Если они не установлены – устанавливаем. Если отключены, включаем.

Если веб–сервера установлены, и в разделе "Возможности" они уже включены, проверяем не побит ли конфиг веб-сервера Nginx или Apache

Nginx

```bash
nginx -t
```

Apache

```bash
httpd -t
```

на Debian/Ubuntu вторая команда будет иметь вид

```bash
apache2ctl -t
```
Если проблем тоже нет, смотрим лог /usr/local/mgr5/var/ispmgr.log на предмет записей с вхождением вида "was not loaded due errors".

В нашем случае видим 

```log
Oct  5 21:27:50 [16105:1] backtrace EXTINFO isppriv_template_nginx::__nginxModule::__nginxModule() (lib/web_nginx_template.so + 0x8d7) [*0x7f945c6ca53b]
Oct  5 21:27:50 [16105:1] backtrace EXTINFO isp_api::RegisterModule<isppriv_template_nginx::__nginxModule>::Constructor() (lib/web_nginx_template.so + 0x1b) [*0x7f9467506cd2]
Oct  5 21:27:50 [16105:1] libmgr ERROR Error: Type: 'file' Object: 'remove' Value: '/etc/nginx/vhosts-resources/.some.domain.todelete.0/custom.conf'
Oct  5 21:27:50 [16105:1] core WARNING Module 'nginx' was unloaded
Oct  5 21:27:50 [16105:1] core WARNING Module 'web_nginx_template' was not loaded due errors. Type: 'file' Object: 'remove' Value: '/etc/nginx/vhosts-resources/.some.domain.todelete.0/custom.conf'
Oct  5 21:27:50 [16105:1] core WARNING Module 'nginx_access' was unloaded
```

Из-за чего возникает эта ситуация? У панели ISPManager есть свой встроенный парсер конфигурационных файлов Nginx и Apache. При загрузке связанного с работой веб-сервера функционала панель ISPManager грузит модуль webdomain(высокоуровневый модуль, отвечающий за работу с WWW-доменами и их отображение), тот по зависимостям грузит модуль nginx(отвечает за работу с веб-сервером nginx), тот подгружает web_nginx_template(отвечает за парсинг и формирования конфигурационных файлов nginx), последний парсит(разбирает и анализирует записи) конфигурационных файлов nginx(независимо от того, как их парсит веб-сервер nginx), сравнивает обнаруженные конфиги с теми параметрами, что указаны для WWW-доменов в конфигурационном файле(база  SQLite3 в файле ispmgr.db, что лежит в /usr/local/mgr5/etc/) и если конфиг рабочий, передаёт полученные данные модулю nginx, тот модулю webdomains, который отображает WWW-домены и позволяет через web-ui и api просматривать и изменять записи о WWW-доменах и их настройках. Если конфиг WWW-домена в файле конфига веб-сервера не соответствует текущим настройкам, указанным в соответствующей таблцие конфига ispmgr.db, панель попытается привести текущую конфигурацию в состояние, консистентное с теми настройками, что указаны в ispmgr.db. Если конфиг изменялся вручную, и сделать это корректно не получится, возникнет ошибка, и WWW-домен может не отобразиться панелькой.

В нашем случае тестирование конфигов веб-серверов встроенными парсерами(nginx -t и httpd -t) проблем не выявляло, так как nginx не подгружал конфиг из скрытого каталога /etc/nginx/vhosts-resources/.some.domain.todelete.0/. Но, парсер конфигов nginx панели ISPManager не такой умный, он ищет все конфиги в каталогах /etc/nginx/vhosts и /etc/nginx/vhosts-resources/ не зависимо от того, подключены они в вышестоящих конфигах веб-сервера nginx, или нет. 

В итоге этот парсер обнаружил не рабочий конфигурационный файл /etc/nginx/vhosts-resources/.some.domain.todelete.0/custom.conf, попытался его удалить(так как домен some.domain ранее был удалён, и этот не нужный конфиг тоже должен был быть удалён для обеспечения консистентности содержимого конфигурационных файлов WWW-доменов с их настройками, указанными в конфиге ISPManager 5 ), не смог его удалить, и выдал ошибку. В результате возникновения которой был выгружен модуль nginx и связанные с ним модули, что привело к выгрузке и модуля webdomain.

Проверять каталоги конфигов веб-сервера Nginx на наличие файлов, помеченных .todelete можно так

find /etc/nginx/vhosts-resources/ -name '*.\.todelete.*'
find /etc/nginx/vhosts/ -name '*.\.todelete.*'

Для Apache 

на Centos

```bash
find /etc/httpd/conf/vhosts/ -name '*.\.todelete.*'
```

на Debian/Ubuntu

```bash
find /etc/apache2/vhosts/ -name '*.\.todelete.*'
```

Если такие файлы или каталоги, помеченные .todelete в названии присутствуют в перечисленных каталогах, а панель их удалить не может, их необходимо удалить вручную и перезапустить панель для повторной загрузки модуля webdomain, и зависимых от него, модулей.

Для решения данной проблемы необходимо было:
1. поправить атрибуты файла /etc/nginx/vhosts-resources/.some.domain.todelete.0/custom.conf (убрать ia)
2. проверить атрибуты каталога /etc/nginx/vhosts-resources/.some.domain.todelete.0
3. удалить данный каталог со всем его содержимым.
4. Выполнить 
```bash
/usr/local/mgr5/sbin/mgrctl -m ispmgr exit
```
для перезапуска панели.
5. Проверить что проблема перестала проявляться, к примеру, так(выполнять от root)

```bash
/usr/local/mgr5/sbin/mgrctl -m ispmgr webdomain su=u01234567
```

Где u01234567 – логин любой учётки с сервера, у которой есть WWW-домены. Если всё работает, в итоге мы получим список всех WWW-доменов учётки, если нет – ошибку.

