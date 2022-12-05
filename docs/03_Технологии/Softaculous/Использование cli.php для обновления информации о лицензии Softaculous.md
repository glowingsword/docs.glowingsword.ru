---
title:  "Использование cli.php для обновления информации о лицензии Softaculous"
authors: 
 - glowingsword
tags:
 - Linux
 - Полезные команды
date: 2021-04-20
---

# Использование cli.php для обновления информации о лицензии Softaculous

```bash
php -d open_basedir="" -d safe_mode=0 -d disable_functions="" /usr/local/softaculous/cli.php --refresh-license
```
Проверяем что получилось

```bash
php -d open_basedir="" -d safe_mode=0 -d disable_functions="" /usr/local/softaculous/cli.php -l
```
## Полезная инфа
https://www.softaculous.com/docs/admin/how-to-refresh-license/#refresh-license-via-cli