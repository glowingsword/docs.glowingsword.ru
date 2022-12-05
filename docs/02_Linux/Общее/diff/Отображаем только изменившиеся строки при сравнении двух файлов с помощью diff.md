---
title: "Отображаем только изменившиеся строки при сравнении двух файлов с помощью diff"
authors: 
 - glowingsword
tags:
 - diff
date: 2022-07-22
---

# Отображаем только изменившиеся строки при сравнении двух файлов с помощью diff

Не совпадающие строки с любого из сравниваемых файлов

```bash
diff --changed-group-format='%<%>' --unchanged-group-format='' a.txt b.txt 
```

Только первого файла

```bash
diff --changed-group-format='%<' --unchanged-group-format='' a.txt b.txt 
```

Только второго файла

```bash
diff --changed-group-format='%>' --unchanged-group-format='' a.txt b.txt
```