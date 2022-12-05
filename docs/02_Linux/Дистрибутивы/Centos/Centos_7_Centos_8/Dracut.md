---
title:  "После обновления ядра при загрузке система вываливается в Dracut"
authors: 
 - glowingsword
tags:
 - Linux
 - 'Centos 7'
 - dracut

date: 2020-10-24
---
# После обновления ядра при загрузке система вываливается в Dracut

Как правило, проблема возникает из-за криво собранного mkinitrd. 

Фиксится на Centos 7 и Centos 8 проблема так

```bash
version=$(rpm -qv kernel | cut -d- -f2- | tail -n 1)
/etc/kernel/postinst.d/51-dracut-rescue-postinst.sh $version /boot/vmlinuz-$version
new-kernel-pkg --mkinitrd --dracut --depmod --update $version
```

Где вторая строка – создаёт rescue-образ, а третья – обычный, для регулярного использования.

После чего, как правило, загрузка с последнего установленного ядра идёт нормально.