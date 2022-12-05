---
title:  "Печатаем файл в консоль с помощью vim и сразу выходим"
authors: 
 - glowingsword
tags:
 - vim
date: 2021-02-18
---

# Печатаем файл в консоль с помощью vim и сразу выходим

```bash
vim --cmd 'set t_ti= t_te=' +redraw +q
```