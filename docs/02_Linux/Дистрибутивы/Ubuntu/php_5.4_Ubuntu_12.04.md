---
title:  'Установка php 5.4 на Ubuntu 12.04'
authors: 
 - glowingsword
tags:
 - Ubuntu
 - Настройка Ubuntu
 - php
date: 2020-04-21
---
# Установка php 5.4 на Ubuntu 12.04
``` bash
sudo apt-get update
```
``` bash
sudo apt-get install python-software-properties
```
``` bash
sudo apt-add-repository ppa:ondrej/php5-oldstable
```
``` bash
sudo apt-get update
```
``` bash
apt-cache policy php5
```
``` bash
sudo apt-get install php5
```
``` bash
php5 -v
```
<http://www.pixelite.co.nz/article/upgrading-php-54-ubuntu-1204-lts-support-drupal-8/>
<https://www.dev-metal.com/how-to-install-latest-php-5-4-x-on-ubuntu-12-04-lts-precise-pangolin/>
