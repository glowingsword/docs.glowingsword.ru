---
title: 'Включаем поддеркку pptp для VPS на OpenVZ'
authors: 
 - glowingsword
tags:
 - 'OpenVZ'
 - 'pptp'
date: 2020-05-09
---
# Включаем поддеркку pptp для VPS на OpenVZ

На OpenVZ-хосте выполняем 

```bash
modprobe ppp_async
modprobe ppp_deflate
modprobe ppp_mppe
```

Делаем 

=== "Команда"
    ```bash
    lsmod | grep ppp
    ```

=== "Ожидаемый результат"
    ```bash
    # lsmod | grep ppp
    ppp_mppe                6246  0 
    ppp_deflate             4176  0 
    zlib_deflate           21661  1 ppp_deflate
    ppp_async               7866  0 
    ppp_generic            25891  3 ppp_mppe,ppp_deflate,ppp_async
    slhc                    5845  1 ppp_generic
    crc_ccitt               1725  1 ppp_async
    ```

Затем выполняем

``` bash
CTID=1234567
```

где вместо 1234567 необходимо указать CTID нужного контейнера OpvnVZ(id VPS-ки).

```bash
vzctl set $CTID --features ppp:on --save
```

``` bash
vzctl set $CTID --devices c:108:0:rw --save
```
``` bash
vzctl exec $CTID mknod /dev/ppp c 108 0
```

``` bash
vzctl set $CTID --save --iptables "ip_conntrack iptable_filter iptable_mangle ipt_state iptable_nat ip_nat_ftp ip_conntrack_ftp"
```

``` bash
vzctl restart $CTID
```

Полезная информация https://anikin.pw/all/ustanovka-pptp-vpn-servera-na-openvz-konteyner/