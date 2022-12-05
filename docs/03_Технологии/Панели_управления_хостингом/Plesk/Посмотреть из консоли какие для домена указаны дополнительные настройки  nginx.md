---
title: 'Посмотреть из консоли какие для домена указаны дополнительные настройки  nginx'
authors: 
 - glowingsword
tags:
 - Plesk
date: 2022-07-22
---

# Посмотреть из консоли какие для домена указаны дополнительные настройки  nginx

```bash
plesk bin domain --show-web-server-settings example.com | grep 'additional nginx directives'
```