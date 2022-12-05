---
title:  "Добавляем для определённого systemd-сервиса нужную переменную окружения на примере добавления переменной OPENSSL ia32cap='~0x200000200000000' для network-manager"
authors: 
 - glowingsword
tags:
 - Linux
 - systemd
date: 2020-06-04
---
# Добавляем для определённого systemd-сервиса нужную переменную окружения на примере добавления переменной OPENSSL ia32cap="~0x200000200000000" для network-manager

Открываем соответствующий service-файл в любимом текстовом редакторе, к примеру

```bash
vim /usr/lib/systemd/system/NetworkManager.service
```
и добавляем 

```bash
Environment=OPENSSL_ia32cap="~0x200000200000000"
```
где вместо  ==/usr/lib/systemd/system/NetworkManager.service== необходимо указать путь к соответствующему service-файлу, в который необходимо добавить изменение, а вместо OPENSSL_ia32cap="~0x200000200000000" - указываем необходимую вам переменную и её значение. 

Затем выполняем 

```bash
systemctl daemon-reload
```
и

```bash
systemctl restart NetworkManager
```

для перезапуска нужного сервис-файла и применения изменений.

Но это брутальное решение. Лучше не трогать стандартные юниты. Проще создать каталог /usr/lib/systemd/system/NetworkManager.service.d, в котором создать файл вида OPENSSL_ia32cap.conf с содержимым

```ini
[Unit]
Environment=OPENSSL_ia32cap="~0x200000200000000"
```

после чего выполнить systemd reload и перезапустить NetworkManager.
