---
title: "Ошибка вида \"WARNING DKIM disabled in exim config. Module disabled.\" при включении OpenDKIM в пане"
authors: 
 - glowingsword
tags:
 - 'ISPManager 4'
date: 2023-03-02
---

# Ошибка вида "WARNING DKIM disabled in exim config. Module disabled." при включении OpenDKIM в панели

Если при включении OpenDKIM в панели ISPManager4:
* OpenDKIM не включается;
* явных ошибок при этом не видно;
* нужный пакет установлен;
* в логах панельки мелькает предупреждение
    ```
    Jun  7 16:06:45 [18820:1] WARNING DKIM disabled in exim config. Module disabled.
    ```
необходимо в разделе "Возможности" не отключая, включить ещё раз exim, после чего opendkim успешно активируется.