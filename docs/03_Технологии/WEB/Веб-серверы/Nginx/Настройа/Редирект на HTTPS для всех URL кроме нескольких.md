# Редирект на HTTPS для всех URL кроме нескольких

Затем над блоками server добавляем

```nginx
map $uri $redirect_https {
    /urls/page_1         0;
    /urls/page_2         0;
    /urls/page_3         0;
    default              1;
}
```

где /urls/page_{1,3} — это адреса, при обращении к которым не должен производиться редирект на HTTPS.


В блок вида 

```nginx
server {
    listen 80;
    # что-то ещё
}
```

где-то после listen(к примеру, в конец блока) добавляем

```nginx
    if ($redirect_https = 1) {
       return 301 https://$server_name$request_uri;
    }
```

Естественно, это решение можно использовать и в обратную сторону(для организации редиректов с HTTPS на HTTP для таких URL).

## полезные ссылки

[Примеры использования map c regex и без](https://johnhpatton.medium.com/nginx-map-comparison-regular-express-229120debe46)
[Ещё немного примеров с map](https://dzone.com/articles/about-using-regexp-in-nginx-map)
[Официальная документация по map](http://nginx.org/ru/docs/http/ngx_http_map_module.html)
[Раскрытие возможностей map в nginx](https://habr.com/ru/post/231277/)