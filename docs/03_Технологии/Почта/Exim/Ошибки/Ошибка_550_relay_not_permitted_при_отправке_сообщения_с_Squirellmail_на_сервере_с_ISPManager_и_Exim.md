# Ошибка 550 relay not permitted при отправке сообщения с Squirellmail на сервере с ISPManager и Exim

Видим в логе exim

```log
2020-09-30 15:39:01 H=localhost ([192.168.103.193]) [::1] F=<if@somedomain.com> rejected RCPT <someuser@anotherdomain.com>: relay not permitted
2020-09-30 15:39:01 unexpected disconnection while reading SMTP command from localhost ([192.168.103.193]) [::1]
```

Если сделать трейс обработчика php, что выполняет скрипты Squirellmail, видим

```C
accept(3, {sa_family=AF_INET6, sin6_port=htons(53158), inet_pton(AF_INET6, "::1", &sin6_addr), sin6_flowinfo=0, sin6_scope_id=0}, [28]) = 9
fcntl(9, F_GETFL)                       = 0x2 (flags O_RDWR)
fstat(9, {st_mode=S_IFSOCK|0777, st_size=0, ...}) = 0
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7feae013d000
lseek(9, 0, SEEK_CUR)                   = -1 ESPIPE (Illegal seek)
dup(9)                                  = 10
fcntl(10, F_GETFL)                      = 0x2 (flags O_RDWR)
fstat(10, {st_mode=S_IFSOCK|0777, st_size=0, ...}) = 0
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7feae013c000
lseek(10, 0, SEEK_CUR)                  = -1 ESPIPE (Illegal seek)
getsockname(9, {sa_family=AF_INET6, sin6_port=htons(25), inet_pton(AF_INET6, "::1", &sin6_addr), sin6_flowinfo=0, sin6_scope_id=0}, [28]) = 0
clone(child_stack=0, flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLD, child_tidptr=0x7feae0124a90) = 2018
```
Как видно, почтовый клиент(веб-интерфейс Squirellmail) отправляет сообщения с IPv6.

Смотрим, что за IP указаны для разрешённых релеев в конфигурационном файле Exim

Открываем /etc/exim/exim.conf и ищем что-то вроде

```ini
hostlist relay_from_hosts = 127.0.0.1 : 192.168.103.193
```

Как видно, разрешены только IPv4(локалхост и внешний IP тачки). 

Переделываем на 

```ini
hostlist relay_from_hosts = <; 127.0.0.1 ; 192.168.103.193 ; fe80::200:5aee:feaa:20a2 ; ::1
```

где:
* <; – переопределение разделителя, так как : не годится в разделители в случаях, когда используем IPv6(в IPv6 разделитель – тоже :)
* 127.0.0.1 и 192.168.103.193 – адреса что были раньше(IPv4)
* fe80::200:5aee:feaa:20a2 – внешний адрес IPv6 сервера 
* ::1 – IPv6 локалхост.

Естественно, вместо 192.168.103.193  и fe80::200:5aee:feaa:20a2 необходимо будет указать реальный IPv4-адресс вашего сервера, а также IPv6-адресс, соответственно.

Перезапускаем Exim

```bash
service exim restart
```

Проверяем. Если всё сделали верно – проблема перестанет проявляться.

!!! info "На заметку"
    Адреса 192.168.103.193 и fe80::200:5aee:feaa:20a2 выглядят как адреса локальной сети не случайно. Реальные адреса пришлось изменить на эти, взятые с потолка, во избежание с любым пересечением с существующими уникальными белыми IP.






