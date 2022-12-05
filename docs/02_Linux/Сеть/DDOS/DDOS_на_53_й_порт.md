Бывает такое, что LA на сервере большая, при этом веб-сервер и сервер баз данных не нагружены, а трафик валит на 53-й порт(tcpdump и добавленные в iptables счётчики для наиболее используемых протоколов и портов помогут определить куда валит трафик).

Смотрим в лог, видим 

```bash
Nov 23 03:07:34 somehost named[6408]: client @0x7fb51044beb0 47.226.60.144#58948 (.): view external: query (cache) './ANY/IN' denied
Nov 23 03:07:34 somehost named[6408]: client @0x7fb513738990 47.226.60.144#58948 (.): view external: query (cache) './ANY/IN' denied
Nov 23 03:07:34 somehost named[6408]: client @0x7fb511b0a1e0 47.226.60.144#58948 (.): view external: query (cache) './ANY/IN' denied
Nov 23 03:07:34 somehost named[6408]: client @0x7fb511688dd0 47.226.60.144#58948 (.): view external: query (cache) './ANY/IN' denied
Nov 23 03:07:37 somehost named[6408]: client @0x7fb511b0a1e0 223.227.61.155#9287 (.): view external: query (cache) './ANY/IN' denied
Nov 23 03:07:37 somehost named[6408]: client @0x7fb513738990 223.227.61.155#9287 (.): view external: query (cache) './ANY/IN' denied
Nov 23 03:07:37 somehost named[6408]: client @0x7fb511688dd0 223.227.61.155#9287 (.): view external: query (cache) './ANY/IN' denied
Nov 23 03:07:37 somehost named[6408]: client @0x7fb5117a06c0 223.227.61.155#9287 (.): view external: query (cache) './ANY/IN' denied
```

как правило, это говорит о том, что кто-то пытается использовать уязвимость http://www.h-online.com/open/news/item/BIND-DNS-server-updates-close-critical-hole-1727232.html


Закрывается уязвимость старых версий Bind с помощью закрытия OPEN DNS.

К примеру, типичный вариант директив для закрытия уязвимости

```json
acl "trusted" { {IP сервера};127.0.0.1; };
options { allow-recursion { trusted; };
allow-notify { trusted; };
allow-transfer { trusted; };
```

Но, даже когда уязвимость закрыта, нередко атакующие продолжают слать тонну запросов с разных IP на 53-й порт вашего сервера. В таком случае стоит заблокировать их в iptables, натравить на данные записи fail2ban, или поставить сервер на защиту от DDOS в зависимости от количества IP, с которых валит подобный тарфик, и ваших возможностей(способности настроить fail2ban и наличия средств для подключения защиты от DDOS при большом объёме подобного трафика).