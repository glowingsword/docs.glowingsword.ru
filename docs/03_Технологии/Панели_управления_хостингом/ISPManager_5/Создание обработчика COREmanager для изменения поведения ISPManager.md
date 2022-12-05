---
title: 'Создание обработчика COREmanager для изменения поведения ISPManager'
authors: 
 - glowingsword
tags:
 - ISPManager
 - ISPManager 5
date: 2021-09-11
---


Так выглядит лог того, что панель делает при resume https://paste.reg.ru/248ab5d97702 и так при добавлении C++ модуля, перехватывающего emai.resume.one https://paste.reg.ru/f19f764bb8ab

В плагин прилетает в это время xml 

```xml
08/11/2021:12:11:39 regtest@domain-shared.ru
08/11/2021:12:11:39 <?xml version="1.0" encoding="UTF-8"?>
<doc lang="en" func="email.resume" binary="/manager/ispmgr" host="https://server132.logincgi.hosting.reg.ru" themename="orion"><ok/></doc>
```




https://doc.ispsystem.ru/index.php/%d0%90%d1%80%d1%85%d0%b8%d1%82%d0%b5%d0%ba%d1%82%d1%83%d1%80%d0%b0_%d1%81%d0%b8%d1%81%d1%82%d0%b5%d0%bc%d1%8b#.D0.9E.D0.B1%20.D1.80.D0.B0.D0.B1.D0.BE.D1.82.D0.BA.D0.B0_.D0.B7.%20D0.B0.D0.BF.D1.80.D0.BE.D1.81.D0.BE.D0.B2



https://docs.ispsystem.ru/coremanager/razrabotchiku/obshchie-spetsifikatsii/xml/xml-opisanie-interfejsov#XML%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%BE%D0%B2-%D0%92%D0%BD%D0%B5%D1%88%D0%BD%D0%B8%D0%B5%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%D0%B8(handler/library)

https://forum.ispsystem.ru/showthread.php?25591-%D0%BF%D1%80%D0%BE-%D0%BF%D0%BB%D0%B0%D0%B3%D0%B8%D0%BD%D1%8B-%D0%B2-ISP-5


https://docs.ispsystem.ru/ispmanager-lite/razrabotchiku/primer-plagina-dobavlenie-punkta-menyu

https://docs.ispsystem.ru/ispmanager-lite/razrabotchiku/ispmanager-api

https://docs.ispsystem.ru/ispmanager-lite/razrabotchiku/vzaimodejstvie-cherez-api

https://docs.ispsystem.ru/ispmanager-lite/razrabotchiku/primer-plagina-rabota-s-shablonizatorom
https://docs.ispsystem.com/ispmanager-lite/developer-section/plug-in-example-templates-engine-management

https://forum.ispsystem.ru/archive/index.php/t-28362.html

https://linuxize.com/post/python-delete-files-and-directories/
https://stackoverflow.com/questions/6996603/how-to-delete-a-file-or-folder-in-python
https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
https://realpython.com/python-string-formatting/#4-template-strings-standard-library


email.suspend
email.edit
email.resume

/usr/local/mgr5/etc/xml/ispmgr_mod_fix_email_resume.xml

<?xml version="1.0" encoding="UTF-8"?>
<mgrdata>
  <handler name="fix_email_resume.py" type="cgi" ignore_errors="yes">
      <event name="email.resume" after="yes"/>
      <event name="email.suspend" before="yes"/>
  </handler>
</mgrdata>

/usr/local/mgr5/addon/fix_email_resume.py

chmod 750 /usr/local/mgr5/addon/fix_email_resume.py
chown 0:0 /usr/local/mgr5/addon/fix_email_resume.py

PARAM_passwd

regtest@domain-shared.ru:{CRAM-MD5}88b5b7b0f2c08b333339cf333a2c9078d000c53d351ab01b5af9d4dc9a26:508:508::/var/www/u1118498/data/email/domain-shared.ru/regtest:::maildir:~/.maildir userdb_quota_rule=*:bytes=0M


https://docs.ispsystem.ru/ispmanager-lite/razrabotchiku/primer-plagina-rabota-s-shablonizatorom

https://forum.ispsystem.ru/archive/index.php/t-28362.html

/usr/local/mgr5/sbin/mgrctl -m ispmgr email.edit elid='regtest@domain-shared.ru' out=text

/usr/local/mgr5/sbin/mgrctl -m ispmgr exit

## Создание модуля C++

yum install coremanager-devel ispmanager-devel

mkdir /usr/local/mgr5/src/email_resumer/

cd /usr/local/mgr5/src/email_resumer


gcc gcc-c++ make m4 autoconf cmake ImageMagick libtool flex bison