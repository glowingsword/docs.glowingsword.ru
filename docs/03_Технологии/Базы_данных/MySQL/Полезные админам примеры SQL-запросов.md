# Полезные админам примеры SQL-запросов

Выводим только нужное количество символов из соответствующего поля таблицы.

```sql
SELECT id,LEFT(title,12) title FROM categories ORDER BY num DESC; 
```
Такой приём бывает полезным, когда изучается проблема с записями в не корректной кодировке.

Выводим нужное количество символов из строки, конвертированное в HEX

```sql
SELECT id,HEX(LEFT(title,12)) title FROM categories ORDER BY num DESC;
```

Выводим строку в HEX-представлении из соответствующего поля таблицы

```sql
SELECT id,HEX(title) title FROM categories ORDER BY num DESC
```

Полученную строку можно затем скопировать, и натравить на неё python, примерно так

```bash
echo -n 'HEX_STRING' | python -c "import sys;strin=sys.stdin.read(); out = [(strin[i:i+2]) for i in range(0, len(strin), 2)];print(' '.join(out))"
```

для получения красивой строки вида

```bash
D0 9F D1 80 D0 BE D0 B3 D1 80 D0 B0 D0 BC D0 BC D0 B8 CC 81 D1 80 D0 BE
```


