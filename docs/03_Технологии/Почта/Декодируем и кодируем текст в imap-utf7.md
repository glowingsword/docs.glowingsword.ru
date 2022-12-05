---
title: 'Декодируем и кодируем текст в imap-utf7 с помощью Python 3'
authors: 
 - glowingsword
tags:
 - почта
date: 2021-12-04
---
# Декодируем и кодируем текст в imap-utf7 с помощью Python 3


```python
from imap_tools.imap_utf7 import encode, decode
# пример кодирования
print(encode('Входящие письма'))
# пример декодирования
print(decode(b'&BBIERQQ+BDQETwRJBDgENQ- &BD8EOARBBEwEPAQw-'))
# пример кодирования и декодирования с возвращением формального строгового представления результата
print(repr(decode(encode("Входящие\rписьма\n\n\n\r\r"))))
```

