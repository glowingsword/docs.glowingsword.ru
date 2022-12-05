---
title: "Ошибка \"(22)Invalid argument: mod fcgid: cant lock process table in pid\""
authors:
 - glowingsword
tags:
 - Apache
 - Ошибки Apache
date: 2020-04-28
---
# Ошибка "(22)Invalid argument: mod fcgid: can't lock process table in pid"

 Как правило, возникает из-за превышения ограничения на процессы-обработчики, на процессы(с помощью ulimits), или в случаях, когда запуск новых процессов упирается в ограничения, указанные в качестве значения параметров ==FcgidSpawnScoreUpLimit== или ==FcgidSpawnScore==. 
 
 Если превышения по процессам не было, стоит включить ==LogLevel debug== в глобальном конфиге и понаблюдать за работой проблемного сайта.