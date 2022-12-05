
# Установка APCu на не дефолную версию php на VPS
Переходим в каталог, куда будем качать исходники расширения
```bash
cd /root
```
Качаем исходники
```bash
wget -O APCu.tar.gz https://pecl.php.net/get/APCu
```
Распаковываем

```bash
tar -xvzv APCu.tar.gz
```

Переходим в каталог с исходным кодом расширения
```bash 
cd apcu-*
```
Выполняем phpize
```bash
/opt/php/7.0/bin/phpize
```

Настраиваем собираемое расширение
```bash
./configure --with-php-config=/opt/php/7.0/bin/php-config
```
Собираем
```bash
make
```
Устанавливаем
```bash
make install
```
Включаем собранное рашсирение
```bash
echo extension=apcu.so > /opt/php/7.0/etc/php.d/apcu.ini
```

Проверяем, что модуль установился корректно


=== "Команда"
    ```bash
    /opt/php/7.0/bin/php -m|grep -i apc
    ```
=== "Результат"
    ```bash
    -bash-4.1# /opt/php/7.0/bin/php -m|grep -i apc
    apcu
```
