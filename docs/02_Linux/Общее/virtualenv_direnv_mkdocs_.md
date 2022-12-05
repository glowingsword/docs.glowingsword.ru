---
title: 'Настраиваем связку virtualenv и direnv для автоматической активации окружения с mkdocs при заходе в каталог с документацией'
authors: 
 - glowingsword
tags:
 - Linux
 - Монтирование разделов
date: 2020-05-05
---
# Настраиваем связку virtualenv и direnv для автоматической активации окружения с mkdocs при заходе в каталог с документацией
Ставим direnv, нужный пакет для дистра ищем https://github.com/direnv/direnv/blob/master/docs/installation.md

Добавляем в конец .bashrc

``` bash
show_virtual_env() {
  if [ -n "$VIRTUAL_ENV" ]; then
    echo "($(basename $VIRTUAL_ENV))"
  fi
}
export -f show_virtual_env
PS1='$(show_virtual_env)'$PS
```

В хомяке проекта mkdocs создаём .envrc вида

```
layout virtualenv ./
unset PS1
```

выполняем 

``` bash
direnv allow
```

после чего выходим из командной оболочки. Заходим заново, видим как активируется virtualenv при входе в каталог.