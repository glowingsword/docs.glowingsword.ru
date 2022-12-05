---
title: 'Добавляем ACL не пускающие письма с исполняемыми файлами, в том числе и вложенными в архив'
authors: 
 - glowingsword
tags:
 - Exim
 - Настройка Exim
 - DKIM
date: 2021-04-10
---

# Добавляем ACL не пускающие письма с исполняемыми файлами, в том числе и вложенными в архивы

Настройка будет показана на примере Ubuntu 16.04, но с учётом специфических для дистров моментов, этот метод применим и для других случаевл

Открываем в редакторе файл /etc/exim4/exim4.conf.localmacros и добавлем в него

```ini
# макросы
EXE_PATTERNS = apk|cgi|js|jse|jsp|wsf|exe|com|vb|vba|vbs|vbe|bat|pif|ps1|scr|hta|cmd|chm|cpl|reg|lnk|dll|sys|jar|ocx|msi|msu|mst
ARCH_PATTERNS = bz2|zip|rar|7z|cab|ace|7za|lah|lzo|lzx|gz|arj|bin|msi|cbr|deb|rpm|gzip|jar|pak|pkg|tar-gz|tgz|xar|zipx|wim|tb2|tar|paq|xz|iso|jar|lzh|lzma|pak|pk3|pk4|smzip|u3p|xpi|zipx|cpio|xar|lz|rk|zoo|img|ha
```

Открываем в редакторе файл /etc/exim4/exim4.conf.template и прокручиваем его до блока объявления acl-ов, который выглядит примерно так

```bash
acl_smtp_rcpt = acl_check_rcpt
acl_smtp_data = acl_check_data
acl_not_smtp = acl_check_not_smtp
```

и указан обычно немного выше начала основного блока с набором ACL-ей, что начинается с 

```ini
begin acl
```

Затем переходим к блоку begin acl и в нём добавляем ближе к началу ещё один блок

```ini
    acl_check_mime:
        # Проверка на присутствие отправителя в белых списках host_local_deny_exceptions, sender_local_deny_exceptions, local_host_whitelist, local_sender_whitelist и whitelist.
        accept
              hosts = ${if exists{CONFDIR/host_local_deny_exceptions}\
                    {CONFDIR/host_local_deny_exceptions}\
                    {}}

        accept
                senders = ${if exists{CONFDIR/sender_local_deny_exceptions}\
                    {CONFDIR/sender_local_deny_exceptions}\
                    {}}
        accept
                hosts = ${if exists{CONFDIR/local_host_whitelist}\
                    {CONFDIR/local_host_whitelist}\
                    {}}
        accept
                senders = ${if exists{CONFDIR/local_sender_whitelist}\
                  {CONFDIR/local_sender_whitelist}\
                  {}}
        accept
                hosts = net-lsearch;/etc/exim4/whitelist
        # Проверка вложений на их присутствие в списке исполняемых файлов или на соответствие типа файла исполняемому файлу
        deny    message     = We do not accept attachments like: $mime_filename
                condition   = ${if or{{match{$mime_content_type}{(?i)executable}}{match{$mime_filename}{\N(?i)\.(EXE_PATTERNS)$\N}}}}
                log_message = Rejected mail with executable attachement: filename=$mime_filename, content-type=$mime_content_type, recipients=$recipients
        # Проверка вложений c рашсширениями как у архивов на присутствие файлов, в которых присутствуют вложенные исполняемые файлы, обнаруженые спомощью deepfind
        deny    message   = We do not accept attachments/deepfind like: $mime_filename
            condition       = ${if match{$mime_filename}{\N(?i)\.(ARCH_PATTERNS)$\N}}
            decode          = default
            condition       = ${if match{${run{/usr/local/bin/deepfind $mime_decoded_filename}}}{\N(?i)\.(EXE_PATTERNS)\n\N}}
            log_message     = Rejected mail with executable/deepfind attachement: filename=$mime_filename, content-type=$mime_content_type, recipients=$recipients
        # Проверка сложений с расширениями zip, rar, tgz, tar, gz и 7z на присутствие исполняемых файлов с помощью архиватора(ахиватор выводит список файлов, exim по нему проходится правилом с EXE_PATTERNS, если находит совпадение, выводит сообщение о том, что сообщение заблокировано).
        deny    message   = A arhive attachment contains a Windows-executable file - blocked because we are afraid of new viruses not recognized [yet] by antiviruses.
            condition       = ${if match{$mime_filename}{\N(?i)\.(zip|rar|tgz|tar|gz|7z)$\N}}
            condition       = ${if def:sender_host_address}
            decode          = default
            condition       = ${if or{\
                                {match{${run{/usr/bin/unzip -l $mime_decoded_filename}}}{\N(?i)\.(EXE_PATTERNS)\n\N}}\
                                {match{${run{/usr/bin/unrar l $mime_decoded_filename}}}{\N(?i)\.(EXE_PATTERNS)\n\N}}\
                                {match{${run{/usr/bin/tar -tf $mime_decoded_filename}}}{\N(?i)\.(EXE_PATTERNS)\n\N}}\
                                {match{${run{/usr/bin/7z l $mime_decoded_filename}}}{\N(?i)\.(EXE_PATTERNS)\n\N}}}}
            log_message             = forbidden arhive attachment: filename=$mime_filename, content-type=$mime_content_type, recipients=$recipients

            accept
```

Устаналиваем на сервер необходимое ПО

```bash
apt install unrar
```
```bash
apt install unzip
```
```bash
apt install p7zip-full
```
```bash
apt install strigi-utils
```

## Полезные ссылки

https://forum.lissyara.su/mta-mail-transfer-agent-f20/problemy-s-fil-traciej-pisem-s-ispolnyaemymi-vloje-t43823.html
https://kostikov.co/ispolzovanie-analiza-mime-sredstvami-exim-488
https://www.lissyara.su/doc/exim/4.62/content_scanning_at_acl_time/
http://www.rldp.ru/exim/exim484r/glava39.htm