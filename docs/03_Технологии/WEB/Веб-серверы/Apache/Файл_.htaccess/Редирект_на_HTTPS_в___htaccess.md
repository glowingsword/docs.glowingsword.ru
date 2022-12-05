---
title:  "Редирект на HTTPS в .htaccess"
authors: 
 - glowingsword
tags:
 - Apache
 - .htaccess
 - Правила перенаправления
 - Редиректы
date: 2020-04-04
---
# Редирект на HTTPS в .htaccess

Данные варианты правил следует пробовать начиная с 1-го(вариант для ISPManager и серверов без панелей), и вплоть до 5-го(если сервак с cPanel, или другие варианты корректно не работают и нам не подошли).

=== "Вариант 1 (для ISPManager)"
    ``` apacheconf
    RewriteEngine On
    RewriteCond %{SERVER_PORT} !^443$
    RewriteRule .* https://%{SERVER_NAME}%{REQUEST_URI} [R=301,L]
    ```

=== "Вариант 2"
    ``` apacheconf
    RewriteEngine On
    RewriteCond %{HTTPS} =on 
    RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI} [QSA,L]
    ```

=== "Вариант 3"
    ``` apacheconf
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteCond %{HTTP:X-Forwarded-Proto} !https
    RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
    ```

=== "Вариант 4(cPanel)"
    ``` apacheconf
    RewriteEngine On
    RewriteCond %{ENV:HTTPS} !on
    RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
    ```

=== "Вариант №5(cPanel)"
    ``` apacheconf
    RewriteCond %{HTTP:X-HTTPS} !On
    RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
    ```