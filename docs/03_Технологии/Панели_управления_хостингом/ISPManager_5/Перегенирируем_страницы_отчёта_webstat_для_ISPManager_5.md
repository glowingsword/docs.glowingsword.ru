---
title: 'Перегенирируем страницы отчёта webstat для ISPManager 5'
authors: 
 - glowingsword
tags:
 - ISPManager 5
date: 2020-04-05
---

# Перегенирируем страницы отчёта webstat для ISPManager 5

```bash
/usr/share/awstats/tools/awstats_buildstaticpages.pl \
-update \
-config=[site.com] \
-dir=/var/www/[user]/data/www/[site.com]/webstat \
-awstatsprog=/usr/share/awstats/wwwroot/cgi-bin/awstats.pl
```



