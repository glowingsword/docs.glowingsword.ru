---
title: Добавление подписи DKIM
authors: 
 - glowingsword
tags:
 - Exim
 - Настройка Exim
 - DKIM
date: 2020-04-04
---
# Настройка заголовков, указываемых в DKIM-Signature h-заголовке

Ищем в конфигурционном файле  /etc/exim/exim.conf упоминание dkim_domain или блок .ifdef DKIM_ENABLE, в него закиываем 

```ini
      dkim_sign_headers =  subject:to:from
```

где заголовки subject:to:from — те заголовки, что необходимо подписать и указать в DKIM-Signature h.

В итоге, отправив тестовое сообщение, мы получим что-то вроде

```yaml
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/relaxed; d=some.domain;
	s=mailru; h=Subject:To:From; bh=p5AkL0xY2vWmmHPBPzIdMI5IZtPu+d2sJLiP8EqZScM=;
	 b=uq8jhkDBPk+Sh0x7HA6GzrShlSahkAfKQE2aPkc+NfMh790WIySH/ipcwcjNetw9Z4anurkEK9
	7b9ZhFPZ7wr6xXhdp9Ng8gQOmOq3N+mGtchhiCmaZdalVkdaRMfHhFyzsdxTLiJozjYLjQWg7YpdH
	9AtbD1vycwwdcLr7pMGU=;
```

Видим, что у нас подписаны h=Subject:To:From, а значит всё у нас получилось так, как мы настраивали.

