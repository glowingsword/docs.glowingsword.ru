---
title: 'Полезное ПО на node.js'
authors: 
 - glowingsword
tags:
 - Node.js
date: 2020-04-22
---
# Ошибка Your distribution, identified as "wheezy", is not currently supported при установке node.js 6.x

Проведённый мной анализ текста установочного срипта nodejs6.x говорит о том, что wheeze входит в список поддерживаемых дистрибутивов.
Однако проверка того, поддерживается ли данный дистрибутив, в установщике производится с помощью кода вида

``` bash
print_status "Confirming \"${DISTRO}\" is supported..."

if [ -x /usr/bin/curl ]; then

`   exec_cmd_nobail "curl -k -sLf -o /dev/null '`[`https://deb.nodesource.com/${NODEREPO}/dists/${DISTRO}/Release`](https://deb.nodesource.com/$%7BNODEREPO%7D/dists/$%7BDISTRO%7D/Release)`'"`  
`   RC=$?`

else

`   exec_cmd_nobail "wget -qO /dev/null -o /dev/null '`[`https://deb.nodesource.com/${NODEREPO}/dists/${DISTRO}/Release`](https://deb.nodesource.com/$%7BNODEREPO%7D/dists/$%7BDISTRO%7D/Release)`'"`  
`   RC=$?`

fi

if [$RC != 0]($RC_!=_0 "wikilink"); then

`   print_status "Your distribution, identified as \"${DISTRO}\", is not currently supported, please contact NodeSource at `[`https://github.com/nodesource/distributions/issues`](https://github.com/nodesource/distributions/issues)` if you think this is incorrect or would like your distribution to be considered for support"`  
`   exit 1`

fi

```

который автоматически считает дистрибутив не поддерживаемым, если не может скачать соответствующий файл Release для нужной версии дистрибутива.

При этом на wheeze при обращении к deb.nodesource.com возникает ошибка, связанная с отсутствием в списке доверенных корневого сертификата, используемого для верификации сертификата Amazon Root CA 1

!!! failure
    ``` bash
    Err <https://deb.nodesource.com> wheezy/main amd64 Packages
    ` server certificate verification failed. CAfile: /etc/ssl/certs/ca-certificates.crt CRLfile: none`
    Err <https://deb.nodesource.com> wheezy/main i386 Packages
    ` server certificate verification failed. CAfile: /etc/ssl/certs/ca-certificates.crt CRLfile: none`
    Ign <https://deb.nodesource.com> wheezy/main Translation-en
    ```

Что, в свою очередь, и приводит к возникновению подобной проблемы.

Для решения данной проблемы достаточно создать файл
``` bash
vim /usr/local/share/ca-certificates/amazon.com.crt
```
скопировать в него нужный корневой сертификат, после чего выполнить
``` bash
sudo update-ca-certificates
```

После чего необходимо скачать установочный скрипт для nodejs, добавить опцию -k для curl в
скрипт установки node6x, после чего использовать изменённый скрипт для установки node.js.

<https://github.com/nodesource/distributions/issues/46>
<https://github.com/nodesource/distributions/issues/232>
