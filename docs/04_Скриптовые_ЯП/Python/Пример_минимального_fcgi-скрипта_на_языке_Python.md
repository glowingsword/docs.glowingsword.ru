---
title: 'Пример минимального fcgi-скрипта на языке Python'
authors: 
 - glowingsword
tags:
 - python
date: 2020-04-23
---

# Пример минимального fcgi-скрипта на языке Python

Создаём скрипт вида

``` bash
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from cgi import escape
import sys, os
from flup.server.fcgi import WSGIServer

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    yield '<h1>FastCGI Environment</h1>'
    yield '<table>'
    for k, v in sorted(environ.items()):
        yield '<tr><th>%s</th><td>%s</td></tr>' % (escape(k), escape(v))
    yield '</table>'

WSGIServer(app).run()
```


