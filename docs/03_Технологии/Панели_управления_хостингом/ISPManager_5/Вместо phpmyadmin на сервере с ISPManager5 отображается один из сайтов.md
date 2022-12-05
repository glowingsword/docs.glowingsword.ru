---
title: 'Вместо phpmyadmin на сервере с ISPManager5 отображается один из сайтов'
authors: 
 - glowingsword
tags:
 - ISPManager
 - ISPManager 5
 - phpMyAdmin
date: 2021-09-11
---

Проблема возникает в случаях, когда на сервере не хватает файла /etc/nginx/conf.d/isp.conf

Формируем файл с помощью команд

```bash
cat <<-'EOF' > /etc/nginx/conf.d/isp.conf
server {
    listen HOST_IP:443;
    server_name HOST_IP;
    ssl on;
    ssl_certificate /usr/local/mgr5/etc/manager.crt;
    ssl_certificate_key /usr/local/mgr5/etc/manager.key;
 
    set $mgr_proxy "https://HOST_IP:1500";
 
        location ^~ /manimg/ {
        alias /usr/local/mgr5/skins/;
    }
    location / {
        proxy_pass $mgr_proxy;
        proxy_redirect $mgr_proxy /;
        proxy_set_header Host $host:$server_port;
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-Secret OUR_SECRET;
        chunked_transfer_encoding off;
    }
 
    location ^~ /mancgi/ {
            proxy_pass $mgr_proxy;
            proxy_redirect $mgr_proxy /;
            proxy_set_header Host $host:$server_port;
            proxy_set_header X-Forwarded-For $remote_addr;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-Secret OUR_SECRET;
            chunked_transfer_encoding off;
    }

    include /etc/nginx/vhosts-includes/*.conf;
}
EOF
sed -i "s|HOST_IP|$(hostname -i)|g" /etc/nginx/conf.d/isp.conf
sed -i "s|OUR_SECRET|$(pwgen 20 1)|g" /etc/nginx/conf.d/isp.conf
```

перезапускаем nginx 

```bash
nginx -t && nginx -s reload
```
Проверяем. phpMyAdmin должен запуститься.