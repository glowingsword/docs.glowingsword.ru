---
title:  "Переменные окружения для сборки пакетов с помощью Clang"
authors: 
 - glowingsword
tags:
 - "Linux"
 - "Переменные окружения"
date: 2020-06-14
---

# Переменные окружения для сборки пакетов с помощью Clang

Выставляем переменные 

export CC='ccache clang -fcolor-diagnostics -Qunused-arguments -fcatch-undefined-behavior -ftrapv'
export CXX='ccache clang++ -fcolor-diagnostics -Qunused-arguments -fcatch-undefined-behavior -ftrapv'

после чего поддерживающие сборку с помощью Clang проекты будут использовать Clang вместо дефолтного иструментария от GCC для сборки.