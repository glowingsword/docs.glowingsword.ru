---
title: 'Устраняем ошибку (104)Connection reset by peer: mod_fcgid: ap_pass_brigade failed in handle_request_ipc function'
authors: 
 - glowingsword
tags:
 - Apache
 - 'Ошибки Apache'
date: 2020-04-18
---
# Устраняем ошибку "(104)Connection reset by peer: mod_fcgid: ap_pass_brigade failed in handle_request_ipc function"

В случае возникновения ошибок

!!! error ""
    (104)Connection reset by peer: mod_fcgid: error reading data from FastCGI server (104)Connection reset by peer: mod_fcgid: ap_pass_brigade failed in handle_request_ipc function

увеличиваем значение

``` apacheconf
FcgidMaxRequestsPerProcess
```
в ==fcgid.conf== или выставляем его в ==0==, после чего перезапускаем апачик.

Если имеем дело с php 5.5 или выше с акселератором Opcache, стоит также понизить значение ==apc.shm_size== до 32M или отключить apc директивой ==apc.enabled=0==.

* <http://qaru.site/questions/384996/php-and-modfcgid-appassbrigade-failed-in-handlerequestipc-function>
* <https://www.tablix.org/~avian/blog/archives/2016/05/on_ap_pass_brigade_failed/>

