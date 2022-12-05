---
title: 'Меняем тему оформления Wordpress при помощи запросов к базе данных'
authors: 
 - glowingsword
tags:
 - CMS
 - Wordpress
date: 2020-04-04
---
# Меняем тему оформления Wordpress при помощи запросов к базе данных

``` sql
SELECT *
FROM wp_options
WHERE option_name = 'template'
OR option_name = 'stylesheet'
OR option_name = 'current_theme';
```

Ссылка на оригинальную статью
<http://docs.appthemes.com/tutorials/how-to-change-wordpress-themes-directly-from-the-database/>