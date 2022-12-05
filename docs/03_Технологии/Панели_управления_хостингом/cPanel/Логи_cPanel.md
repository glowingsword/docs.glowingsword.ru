---
title: 'Логи cPanel'
authors: 
 - glowingsword
tags:
 - cPanel
 - логи
date: 2020-04-04
---
# Логи cPanel

cPanel установочный лог:

``` bash
/var/log/cpanel-install-thread0.log
```

Apache:

``` bash
/usr/local/apache/logs/access_log
/usr/local/apache/logs/error_log
```

Apache domlogs:

``` bash
/usr/local/apache/domlogs/example.com
```

Apache SUEXEC Logs:

``` bash
/usr/local/apache/logs/suexec_log
```

MySQL

``` bash
/var/lib/mysql/hostname.err
```

BIND (named) Log:

``` bash
/var/log/messages
```

Exim

``` bash
/var/log/exim_mainlog
/var/log/exim_paniclog
/var/log/exim_rejectlog
```

Courier or Dovecot IMAP

``` bash
/var/log/maillog
```

Tomcat Logs:

``` bash
/usr/local/jakarta/tomcat/logs/catalina.err
/usr/local/jakarta/tomcat/logs/catalina.out
```

cPanel Access Log:

``` bash
/usr/local/cpanel/logs/access_log
```

cPanel Error Log:

``` bash
/usr/local/cpanel/logs/error_log
```

cPanel License Log:

``` bash
/usr/local/cpanel/logs/license_log
```

Stats Execution Logs:

``` bash
/usr/local/cpanel/logs/stats_log
```

ChkServd (cPanel Monitoring Daemon) Logs:

``` bash
/var/log/chkservd.log
```

cPHulkd

``` bash
/usr/local/cpanel/logs/cphulkd.log
```

cPanel Backup Logs:

``` bash
/usr/local/cpanel/logs/cpbackup/*.log
```

Pure-FTP

``` bash
/var/log/messages
/var/log/xferlog (symlinked to /usr/local/apache/domlogs/ftpxferlog)
```

Cron Logs:

``` bash
/var/log/cron
```

SSH Logs:

``` bash
/var/log/secure
```

ModSecurity:

``` bash
/usr/local/apache/logs/modsec_audit.log
/usr/local/apache/logs/modsec_debug_log