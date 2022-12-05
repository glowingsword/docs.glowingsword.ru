---
title: 'Ошибка "xc_dom_probe_bzimage_kernel__unknown compression format" при загрузке VPS с Ubuntu 20.04 на XEN'
authors: 
 - glowingsword
tags:
 - XEN
date: 2022-11-07
---


# Ошибка "xc_dom_probe_bzimage_kernel__unknown compression format" при загрузке VPS с Ubuntu 20.04 на XEN

## Определяем, точно ли у клиента траблы с xc_dom_bzimageloader и его ядром

Если VPS на XEN не стартует, и в выхлопе 

```bash
xm create /etc/xen/conf/OUR_ID.conf -c 
```

мы при этом наблюдаем ошибку

```bash
xc: error: panic: xc_dom_bzimageloader.c:775: xc_dom_probe_bzimage_kernel: unknown compression format: Invalid kernel
```

то это — точно проблема, описанная в этой статье.

## Как завести VPS, чтобы она загрузилась

### Подкидываем на VPS заведомо рабочее ядро, не пожатое bzip2

Нужно остановить VPS, подмонтировать её раздел куда-то, и скопировать туда ядро из шаблона с чистым дистром, аналогичным тому, что юзает VPS.

```bash
xm destroy VPS_ID
```
```bash
mount /dev/OUR_VG/VPS_ID-disk /tmp/VPS_ID/boot/
```

Делаетя это примерно так

```bash
cd /xen/templates/
```
```bash
mkdir ubuntu-20.04-x86_64
```
```bash
tar zxf ubuntu-20.04-x86_64.tar.gz -C ./ubuntu-20.04-x86_64/
```
```bash
cd ubuntu-20.04-x86_64/boot
```
```bash
cp config-5.4.0-65-generic /tmp/VPS_ID/boot/
```
```bash
cp initrd.img-5.4.0-65-generic /tmp/VPS_ID/boot/
```
```bash
cp vmlinuz-5.4.0-65-generic /tmp/VPS_ID/boot/
```
```bash
cd /xen/templates/
```
```bash
rm -rI ./ubuntu-20.04-x86_64
```

После чего, если ранее эта версия ядра у клиента в /boot отсутствовала, необходимо поправить grub.cfg, прописав верхней запись со скопированной нами версией ядра. Просто копируем первую ```menuentry {что-то тут}``` в нашем grub.cfg, и заменяем путь к vmlinuz на путь к vmlinuz-5.4.0-65-generic, а к initrd — на путь к initrd.img-5.4.0-65-generic(где вместо 5.4.0-65 вам необходимо подставить соответствующую вашей версию скопированного рабочего ядра). 

Загружаемся, выбрав в меню загрузчика ядро, не пожатое с помощью bzip.

### Загрузились? Самое время сравнить рабочее, и не рабочее, ядра

Логинимся от рута на VPS по SSH, или из консоли XEN.

Смотрим, чем отличается ядро, которое может загрузить pygrub(загрузчик XEN) от того, что он не может "прожевать".

"Хорошее" ядро выглядит так

```bash
# file vmlinuz-5.4.0-65-generic
vmlinuz-5.4.0-65-generic: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, BuildID[sha1]=9600f316a53a0f54278885e8d9710538ec5f6a08, stripped
```

А "Плохое" немного иначе, у него есть вхождение bzImage в строке:

```bash
# file vmlinuz-5.15.0-52-generic
vmlinuz-5.15.0-52-generic: Linux kernel x86 boot executable bzImage, version 5.15.0-52-generic (buildd@lcy02-amd64-032) #58-Ubuntu SMP Thu Oct 13 08:03:55 UTC 2022, RO-rootFS, swap_dev 0XA, Normal VGA
```

### Устанавливаем зависимости, и  создаём скрипт, что будет автоматически распаковывать ядро, пожатое bzip2 после его установки

Скачиваем скрипт

```bash
wget -q -O /usr/local/bin/extract-vmlinux  https://raw.githubusercontent.com/torvalds/linux/master/scripts/extract-vmlinux
```
Выдаём руту права на его исполнение

```bash
chmod ug+x /usr/local/bin/extract-vmlinux
```

Устаналиваем зависимости

```bash
apt update
```
```bash
apt install elfutils lz4 lzop bzip2 binutils
```

Создаём файл ```/etc/kernel/postinst.d/extract-vmlinux``` с содержимым 

```bash
#!/usr/bin/env bash

KERNEL_VERSION="$1"
KERNEL_PATH="$2"

# extract-vmlinux is in /usr/local/bin
PATH="${PATH}:/usr/local/bin"

# Ensure we have the extract-linux tool
if ! command -v extract-vmlinux > /dev/null; then
        echo >&2 "Command 'extract-vmlinux' is not available (https://raw.githubusercontent.com/torvalds/linux/master/scripts/extract-vmlinux),  Aborting"
        exit 1
fi

# The KERNEL_PATH must be valid
if [ ! -f "${KERNEL_PATH}" ]; then
        echo >&2 "Kernel file '${KERNEL_PATH}' not found. Aborting"
        exit 1
fi

# Create a temp file
TEMP_FILE=$(mktemp /tmp/decompress-kernel-XXXXX)
trap "rm -f ${TEMP_FILE}" 0

# If the given kernel file is still a bzimage see if its needs decompression
if echo "$(file -b "${KERNEL_PATH}")" | grep -q "^Linux kernel x86 boot executable bzImage"; then
        if ! grep -qoa BZh ${KERNEL_PATH}; then
                echo "No bzip2 compression headers found, skipping..."
                exit 0
        fi

        echo "Decompressing '${KERNEL_PATH}'..."
        # Extract the kernel and replace existing if successful
        if extract-vmlinux ${KERNEL_PATH} > ${TEMP_FILE}; then
                # Double check the kernel is a valid ELF image
                if ! readelf -h ${TEMP_FILE} > /dev/null; then
                        echo >&2 "Decompression of kernel file '${KERNEL_PATH}' failed!, not a valid ELF image"
                        exit 1
                fi

                echo "Decompression of kernel file '${KERNEL_PATH}' successful"
                cp -v ${TEMP_FILE} ${KERNEL_PATH}

        else
                echo >&2 "Decompression of kernel file '${KERNEL_PATH}' failed!"
                exit 1
        fi

# Perhaps its already been decompressed
elif echo "$(file -b "${KERNEL_PATH}")" | grep -q "^ELF 64-bit LSB executable"; then
        echo "Kernel file '${KERNEL_PATH}' appears to be decompressed already. skipping"

else
        echo >&2 "Unable to determine the state of kernel file '${KERNEL_PATH}'"
        exit 1
fi
```

Поправляем права на скрипт

```bash
chmod ug+x /etc/kernel/postinst.d/extract-vmlinux
```

### Восстанавливаем работоспособность  ядра, не загружающегося на XEN

И пробуем, как он отработает на одном из ядре, к примеру на заведомо "проблемном" для XEN linux-image-5.15.0-52-generic:

```bash
apt install -y --reinstall linux-image-5.15.0-52-generic linux-headers-5.15.0-52-generic
```

Переходим в /boot VPS-ки. Проверяем, как отработал наш хук

```bash
# file vmlinuz-5.15.0-52-generic
vmlinuz-5.15.0-52-generic: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, BuildID[sha1]=28a29b8480e5f760cc6ca2f7d53398fa4d3836d7, stripped
```

## Проверяем, загружается ли VPS с "исправленным" ядром

Ребутаем VPS, проверяем что она грузится с этого ядра корректно.

## Подчищаем за собой

Если мы копировали вручную отсутствовавшую у клиента версию ядра, как было в моём случае(копировал 5.4.0-65, у клиента такой версии ядра ранее не было, в пакетом менеджере она не значится как установленная), то:
1. в grub.cfg удаляем menuentry для этой версии ядра.
2. не забываем в таком случае подчистить сами файлы ядра командой ```rm vmlinuz-5.4.0-65-generic initrd.img-5.4.0-65-generic config-5.4.0-65-generic``` в /boot/ VPS клиента.

## Библиография
1. https://unix.stackexchange.com/questions/553185/how-do-i-demonstrate-the-type-of-kernel-compression-in-practice
2. https://unix.stackexchange.com/questions/583714/xen-pvgrub-with-lz4-compressed-kernels/584843#584843