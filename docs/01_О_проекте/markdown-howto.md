# Markdown и расширения, используемые при оформлении документации данной KB
## Метаданные

``` yaml
---
title: 'Наш заголовок'
authors: 
 - some_author
tags:
 - Tag1
 - Tag2
todo: 'Optimize this page in the next days'
date: 2020-04-18
---
```

## Ввод специальных символов с клавиатуры в Linux
1. Вводим символ с помощью Compose Key. Настраиваем Compose в Gnome Tweaks. И пользуемся.
Для получения длинного тире вида — зажимаем Compose, затем дваждны вводим минус, получаем ==—==.
Compose + oc даст ==©==, Compose + or — ==®==.
2. Вводим нужный символ через Ctrl + Shift + U, 4-х символьный код символа Unicode, затем Enter или пробел.

Ctrl + Shift + U → 2014 → Space — даст нам символ ==—==.

Ctrl + Shift + U → 221E → Space — даст нам символ ==∞==.

Ctrl + Shift + U → 2603 → Space — даст нам символ ==☃==.

Ctrl + Shift + U → 1f4b0 → Space — даст нам символ ==💰==.

Чем хорош вариант №2? Тем, что он позволяет вставлять Emoji, и расширенные символы Unicode, которые не релаьно ввести с помощью Compose.

3. Вариант #3 - часть смециальных символов можно отображать, используя Python Markdown SmartyPants и PyMdown Extensions SmartSymbols и Emoji. Последний вариант хорош для отображения emoji.


## Markdown
### Заголовки

=== "Результат"
    <h1 id="h1">H1<a class="headerlink" href="#h1" title="Permanent link">¶</a></h1>
    <h2 id="h2">H2<a class="headerlink" href="#h2" title="Permanent link">¶</a></h2>
    <h3 id="h3">H3<a class="headerlink" href="#h3" title="Permanent link">¶</a></h3>
    <h4 id="h4">H4<a class="headerlink" href="#h4" title="Permanent link">¶</a></h4>
    <h5 id="h5">H5<a class="headerlink" href="#h5" title="Permanent link">¶</a></h5>
    <h6 id="h6">H6<a class="headerlink" href="#h6" title="Permanent link">¶</a></h6>
    <h1 id="alt-h1">Alt-H1<a class="headerlink" href="#alt-h1" title="Permanent link">¶</a></h1>
    <h2 id="alt-h2">Alt-H2<a class="headerlink" href="#alt-h2" title="Permanent link">¶</a></h2>

=== "Markdown"
    ~~~ markdown
    # H1
    ## H2
    ### H3
    #### H4
    ##### H5
    ###### H6

    Alt-H1
    ======

    Alt-H2
    ------
    ~~~

___

### Акцентирование

=== "Результат"
    Выделение(italic) с помощью *звёздочки* и _подчёркивания_

    Строгое выделение(bold) с помощью **двух звёздочек** или __символов подчёркивания__

    Комбинирование выделение с помощью **звёздочек и _символов подчёркивания_**
    
    ~~Зачёркнутый текст~~

=== "Markdown"
    ``` markdown
    Выделение(italic) с помощью *звёздочки* и _подчёркивания_
    Строгое выделение(bold) с помощью **двух звёздочек** или __символов подчёркивания__
    Комбинирование выделение с помощью **звёздочек и _символов подчёркивания_**
    ~~Зачёркнутый текст~~
    ```

### Подсветка кода

=== "Результат"

    ``` bash
    #!/bin/bash

    echo "Hello world!"
    ```

=== "Markdown"
    ~~~ markdown
    ``` bash
    #!/bin/bash

    echo "Hello world!"
    ```
    ~~~


## Расширения Markdown

### Admonition 
Admonition предоставляет возвожность добавить блок с примечанием или предупреждением.
Синтаксис
``` markdown
!!! note "Заголовок"
```

Где 
1. Заголовок - наш заголовок, если указать "" - будет блок без заголовка.
2. note - класс из списка
    *note
    *seealso
    *abstract
    *summary
    *tldr
    *info
    *todo
    *tip
    *hint
    *important
    *success
    *check
    *done
    *question
    *help
    *faq
    *warning
    *caution
    *attention
    *failure
    *fail
    *missing
    *danger
    *error
    *bug
    *example
    *quote
    *cite

Эти же классы можно использовать для коллапсирующих блоков Details.

=== "Результат"
    !!! note "Phasellus posuere in sem ut cursus"
        Lorem 

=== "Markdown"
    ``` markdown
    !!! note "Заметка №1"
    Текст заметки...
    ```
## Расшиерения из pymdown-extensions

### Mark

Mark - способ пометить часть строки в тексте с помощью выделения цветом(так в бумажной газете отмечали ключевые фразы маркером).
Отмечаем нужный фрагмент с помощью двух символов = до и после нужной фразы.

Пример

=== "Результат"
    ==заметь меня==

    ==умная==заметка==

=== "Markdown"
    ``` markdown
    ==заметь меня==
    ==умная==заметка==
    ```

### Keys

!!! example "Пример использования Keys"
    === "Результат"
        ++ctrl+alt+delete++
    === "Markdown"
        ``` markdown
        ++ctrl+alt+delete++
        ```
### Delete

!!! example "Пример использования Delete"

    === "Результат"
        ~~Delete me~~

    === "Markdown"
        ``` markdown
        ~~Delete me~~
        ```

### Tabs

Tabs - это расширение, позволяющее создавать групы вкладок с неким содержимым.
Пример использования данного расширения

=== "Результат"
    === "Tab 1"
        Markdown **content**.

        Multiple paragraphs.

    === "Tab 2"
        More Markdown **content**.

        - list item a
        - list item b

=== "Markdown"
    ``` markdown
    === "Tab 1"
        Markdown **content**.

        Multiple paragraphs.

    === "Tab 2"
        More Markdown **content**.

        - list item a
        - list item b
    ```
### Details

Details создаёт коллапсирующие блоки скрывающие дополнительную информацию под кат.

Перед Details  необходимо добавить хотябы одну пустую строку. 
Обявляется Details с помощью ??? для начала объявления блока Details, или с ???+ если нам нужен изначально раскрытый блок.
Синтаксис элемента Details
``` markdown
??? multiple optional-class 'Заголовок'
```
Возвожные варианты классов:

??? settings "settings"
    settings - желтый цвет и символ карандаша

??? danger "danger"
    danger   - красный и символ молнии в круге

??? success "success"
    success зелёный и галочка звершения задачи в круге

??? note "note"
    note - символ карандаша

??? warning "warning"
    warning  -  оранжевый и треугольник с восклицательным знаком

??? cite "cite"
    warning  -  оранжевый и треугольник с восклицательным знаком

Подробный пример с содержимым, включающим блок с кодом с подсветкой

=== "Результат"
    ??? settings "Basic Polyfill Setup"
        Часть css полифила для details
        ```css
        details {
        display: block;
        }
        ```

=== "Markdown"
    ~~~ markdown
    ??? settings "Basic Polyfill Setup"
    Часть css полифила для details
    ```css
    details {
    display: block;
    }
    ```    
    ~~~

### Icons

=== "Результат"
    * :material-account-circle: – we can use Material Design icons
    * :fontawesome-regular-laugh-wink: – we can also use FontAwesome icons
    * :octicons-octoface: – that's not all, we can also use GitHub's Octicons

=== "Markdown"
    ``` mardown
    * :material-account-circle: – we can use Material Design icons
    * :fontawesome-regular-laugh-wink: – we can also use FontAwesome icons
    * :octicons-octoface: – that's not all, we can also use GitHub's Octicons
    ```

### Mermaid


=== "Результат"
    <div class="mermaid">
    graph TD;
        A--&gt;B;
        A--&gt;C;
        B--&gt;D;
        C--&gt;D;
    </div>

=== "Код"
    ```markdown
    graph TD;
        A-->B;
        A-->C;
        B-->D;
        C-->D;
    ```

### Изображения отображаемые плагином lightgallery

Одиночное изображение

=== "Код"
    ```markdown
    ![!Description](/assets/img/Test.png)
    ```

=== "Результат"
    ![!Description](/assets/img/Test.png)

Галерея

=== "Код"
    ```html
    <div class="lightgallery">
        <a href="/assets/img/Test.png">
            <img src="/assets/img/Test.png">
        </a>
        <a href="/assets/img/Test.png">
            <img src="/assets/img/Test.png">
        </a>
    </div>
    ```

=== "Результат"
    <div class="lightgallery">
        <a href="/assets/img/Test.png">
            <img src="/assets/img/Test.png">
        </a>
        <a href="/assets/img/Test.png">
            <img src="/assets/img/Test.png">
        </a>
    </div>

 
### Вставка содержимого файла с исходником

=== "Результат"
    ```python title="browserslistrc.py"
    --8<-- "browserslistrc.py"
    ```

=== "Markdown"
    ~~~ markdown
    ```python title="browserslistrc.py"
    --8<-- "browserslistrc.py" 
    ```
    ~~~

!!! info "Внимание!"
    Если после имени файла, указанного в кавычках, добавляем пробел — вставка сниппета из файла производиться не будет.

#### Подробности
[embedding-external-files](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#embedding-external-files) 
[pymdown-extensions/extensions/snippets](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/)