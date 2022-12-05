---
title: '(104)Connection reset by peer: [client IP:POPRT] mod_fcgid: error reading data from FastCGI server'
authors: 
 - glowingsword
tags:
 - Apache
 - Ошибки Apache
date: 2020-05-02
---

# Ошибка (104)Connection reset by peer: [client IP:POPRT] mod_fcgid: error reading data from FastCGI server

Выглядит ошибка так

``` log
[Sat May 02 12:04:32.720176 2020] [fcgid:warn] [pid 12831] (104)Connection reset by peer: [client IP:PORT] mod_fcgid: error reading data from FastCGI server
[Sat May 02 12:04:32.720232 2020] [core:error] [pid 12831] [client IP:PORT End of script output before headers: index.php
```
возникает ошибка из-за того, что процесс-обработчик php завершился неожиданно. Почему он завершился неожиданно - данная ошибка сама по себе не говорит. Нужно искать записи в messagess об OOM и об ошибках php в error.log, иногда что-то подобное удаётся найти. Иногда нет. Если процесс упал, а в логах ничего связанного с данной проблемой, кроме ошибки, процитированной выше - можно поискать core файл и попытаться понять, из-за чего упал процесс.

