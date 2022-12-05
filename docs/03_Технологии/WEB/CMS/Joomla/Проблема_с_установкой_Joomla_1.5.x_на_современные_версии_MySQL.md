---
title: Проблема с установкой Joomla 1.5.x на современные версии MySQL
authors: 
 - glowingsword
tags:
 - CMS
 - Joomla
date: 2020-04-04
---
# Проблема с установкой Joomla 1.5.x на современные версии MySQL

Необходимо заменить все вхождения "TYPE=MyISAM" на "ENGINE=MyISAM" в
файлах с расширением sql в каталоге \\installation\\sql\\mysql\\, так
как директива TYPE помечена как устаревшая с MySQL версии 4.0.18., и её
поддержка была удалена в актуальных версиях MySQL.