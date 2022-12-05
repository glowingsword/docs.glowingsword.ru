---
title: 'Как остановить контейнер на базе системы виртуализации OpenVZ, который не реагирует на команду vzctl stop'
authors: 
 - glowingsword
tags:
 - 'OpenVZ'
date: 2020-05-09
---
Если выполняем 
```bash
vzctl stop 24110231 --fast
```

и команда завершается не удачно, так

```bash
# vzctl stop CTID --fast
Killing container ...
Child CTID exited with status 7
Unable to stop container
```

выполняем команду

```bash
vzctl set 24110231 --disabled yes --save
```

после чего контейнер стопается.