Ставим virtualenv

``` bash
pip install virtualenv
```

``` bash
virtualenv /opt/venvs/mkdocs
```
``` bash
source /opt/venvs/mkdocs/bin/activate
```

cd  /opt/venvs/mkdocs

Создаём файл /opt/venvs/mkdocs/requirements.txt вида 

``` bash
Markdown
MarkupSafe
mkdocs
mkdocs-material
mkdocs-material-extensions
Pygments
pymdown-extensions
tags-macros-plugin
lightgallery
```

``` bash
pip install -r /opt/venvs/mkdocs/requirements.txt
```
Запуск строенного сервера mkdocs в каталоге, в котором расположен данный файл(README.MD)

``` bash
mkdocs serve
```
Запуск сборки статических страниц в site
``` bash
mkdocs serve build
```
По завершении работы с проектом не забываем делать
``` bash
deactivate
```