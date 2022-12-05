---
title: 'Установка ffmpeg-php на Centos 6.x'
authors: 
 - glowingsword
tags:
 - PHP
 - 'Установка расширений PHP'
 - ffmpeg
date: 2020-04-21
---
# Установка ffmpeg-php на Centos 6.x
``` bash
git clone `[`https://github.com/tony2001/ffmpeg-php.git`](https://github.com/tony2001/ffmpeg-php.git)
```

``` bash
vim /root/ffmpeg-php/ffmpeg_frame.c
```
и заменяем все вхождения `PIX_FMT_RGBA32` или `PIX_FMT_RGB32` на `AV_PIX_FMT_RGB32`
``` bash
/opt/php/5.5/bin/phpize ./configure --enable-shared --prefix=/usr --with-php-config=/opt/php/5.5/bin/php-config
```
``` bash
make clean
```
``` bash
make
```
``` bash
make install
```
с поддержкой `GD`
``` bash
yum install -y gd-devel
```
``` bash
/opt/php/5.5/bin/phpize 
```
``` bash
./configure --enable-skip-gd-check --enable-shared --prefix=/usr --with-php-config=/opt/php/5.5/bin/php-config
```
``` bash
make clean
```
``` bash
make
```
``` bash
make install
```

``` bash
echo 'extension=ffmpeg.so' > /opt/php/5.5/etc/php.d/ffmpeg.ini 
``` 
``` bash
/opt/php54/bin/php -m |grep ffmpeg
```
``` bash
ffmpeg
```
``` bash
/opt/php54/bin/php -m|grep ffmpeg
```
``` bash
 ffmpeg
```

<http://firstwiki.ru/index.php/%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0_FFMPEG#.D0.A3.D1.81.D1.82.D0.B0.D0.BD.D0.BE.D0.B2.D0.BA.D0.B0_php-ffmpeg>
<https://community.centminmod.com/threads/unable-to-install-ffmpeg-php-extension.1519/page-2#post-16487>
<https://linux-notes.org/vklyuchit-atrpms-repozitorij-v-centos-fedora-redhat/>
<http://packages.atrpms.net/dist/el6/>

<https://felix90.ru/2016/02/%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-php-ffmpeg-%D0%BD%D0%B0-centos-6/>

<https://github.com/tony2001/ffmpeg-php/pull/20/files?diff=split>