---
title: "Установка Archlinux на BTRFS subvolume из уже установленной Fedora"
authors: 
 - glowingsword
tags:
 - Arch
 - GRUB2
date: 2020-06-14
---

# Установка Archlinux на BTRFS subvolume из уже установленной Fedora
## Бутстрэпим базовую систему
Монтируем корневой раздел, в моём случае это ==/dev/sda9==
```bash
mount /dev/sda9 /mnt/BtrfsRoot
```
создаём ==subvolume== для нашей системы с названием ==@arch==
```bash
cd /mnt/BtrfsRoot
```
```bash
btrfs subvolume create @arch
```
Теперь качаем  ==archlinux-bootstrap== в ==/tmp==
```bash
cd tmp
```
```bash
curl -O http://mirror.metrocast.net/archlinux/iso/2017.04.01/archlinux-bootstrap-2017.04.01-x86_64.tar.gz
```
```bash
cd /tmp
```
```bash
tar xzf archlinux-bootstrap-2017.04.01-*.tar.gz
```
Редкактируем mirrorlist убирая # из начала строки с наиболее близко расположенным к вам зеркалом

```bash
vim /tmp/root.*/etc/pacman.d/mirrorlist
```
и chroot-имся в нашу новую систему
```bash
/tmp/root.*/bin/arch-chroot /tmp/root.*/
```
```bash
pacman-key --init
```
```bash
pacman-key --populate archlinux
```
Если нужно, устанавливаем необходимые пакеты, после чего выходим из данного каталога.

Затем монтируем subvolume для нашего арчика
```bash
mount -t btrfs -o subvol=@arch /dev/sda9 /mnt/arch
```
и копируем содержимое ==/tmp/root.x86_64== на нужный нам раздел
```bash
rsync -aAXv --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"} /tmp/root.x86_64/ /mnt/arch/
```
```bash
mkdir boot/efi
```
```bash
cd /tmp/root.*
```
```bash
cp /etc/resolv.conf etc
```
```bash
mount --bind /boot/efi boot/efi
mount --rbind /proc proc
mount --rbind /sys sys
mount --rbind /dev dev
mount --rbind /run run
```
```bash
chroot /mnt/arch /bin/bash
```
Затем genfstab для создания fstab
```bash
genfstab -U /mnt >> etc/fstab
```
Затем можно установить необходимо ПО, к примеру в моём случае это base(обновляем базовые пакеты до актуальной версии), base-devel и  btrfs-progs
```bash
pacman -Sy base base-devel btrfs-progs
```
а также grub
```bash
pacman -Sy grub efibootmgr
```
```bash
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=arch-grub --boot-directory=/boot/ --recheck --debug
```
В случае, если потом нужно будет обновить конфиг
```bash
grub-mkconfig > /boot/grub/grub.cfg
```
## Устанавливаем intel-ucode если у нас проц от Intel==
```bash
pacman -Sy intel-ucode
```
и не забываем пересобрать grub.cfg.

Устанавливаем обновление времени по ntp
```bash
timedatectl set-ntp true
```
```bash
echo имя_хоста > /etc/hostname
```
Включаем локали, раскомментировав их в /etc/locale.gen, после чего герерируем их:
```bash
locale-gen
```
в моём случае это en_US.UTF-8 и ru_RU.UTF-8.

и указываем нужную локаль в качестве системной
```bash
echo 'LANG=en_US.UTF-8' > /etc/locale.conf
```
```bash
echo 'KEYMAP=ruwin_ct_sh-UTF-8' > /etc/vconsole.conf
```
Ставим terminus, затем указываем шрифт для консоли с поддержкой кирилицы

и указываем нужный шрифт, добавив в /etc/vconsole.conf строку вида
```bash
FONT=ter-u16
```
где ter-u16 - выбранный нами шрифт. 

Выполнять systemctl restart systemd-vconsole-setup.service для немедленного подхвата изменений в нашем случае не нужно, изменения понадобятся только после первой перезагрузки.

Пересобираем initcpio
```bash
mkinitcpio -p linux
```

## Решаем проблему с подгрузкой шрифтов для консолей

Для решения данной проблемы необходимо создать правило UDEV, которое будет срабатывать на появление нового устройства /dev/fb* в файле /etc/udev/rules.d/96-fb-all-vcs-setup.rules, добавив в него

```bash
# Setup all vconsoles for a new framebuffer device
KERNEL=="fb*", ACTION=="add", RUN+="/bin/sh /etc/udev/all-vcs-set.sh"
```

и скрипт, который оно будет запускать:

/etc/udev/all-vcs-set.sh

```bash
#!/bin/sh
# We must load locale for $VCS util
. /etc/locale.conf
export LANG
VCS=/usr/lib/systemd/systemd-vconsole-setup
# Setup the "real" (current) console first
$VCS
# Setup all other active consoles
for VC in /dev/vcs[0-9]*
do $VCS /dev/tty${VC#/dev/vcs}
done
```

## Выбираем временную зону
```bash
rm /etc/localtime
ln -s /usr/share/zoneinfo/Зона/Субзона /etc/localtime
```
в моём случае это 
```bash
ln -s /usr/share/zoneinfo/Europe/Chisinau  /etc/localtime
```
Включаем синхронизацию времени по NTP
```bash
timedatectl set-ntp true
```
системное время устаналиваем в UTC
```bash
hwclock --systohc --utc
```

==Устаналиваем gpm для поддержки мыши в консоли==
```bash
pacman -Su gpm
systemctl start gpm.service
systemctl enable gpm.service
```
добавляем в /etc/hosts строку
```bash
127.0.1.1	arch.localdomain	arch
```

==Указываем пароль==
```bash
passwd
```
Теперь можно перезагрузиться и проверить что у нас получилось

## Установка Gnome
```bash
pacman -Sy gnome  gnome-boxes gnome-initial-setup gnome-multi-writer gnome-packagekit  gnome-software cheese file-roller gedit gedit-code-assistance gnome-calendar gnome-clocks gnome-color-manager gnome-documents gnome-getting-started-docs gnome-logs gnome-maps gnome-nettool gnome-photos gnome-sound-recorder gnome-todo gnome-tweak-tool gnome-weather seahorse gnome-dictionary gnome-user-share gnome-themes-extra gnome-keyring gnome-characters gnome-backgrounds chrome-gnome-shell
```
```bash
systemctl enable gdm.service
```
## Устанавливаем плагины NetworkManager для VPN
```bash
pacman -Sy  modemmanager networkmanager networkmanager-pptp networkmanager-openvpn networkmanager-openconnect
```
```bash
systemctl enable NetworkManager.service
systemctl enable NetworkManager-dispatcher.service 
systemctl enable ModemManager.service
```
## Устанавливаем bluez для работы с bluetooth-гарнитурами

```bash
pacman -Sy pulseaudio pulseaudio-alsa pulseaudio-bluetooth bluez bluez-libs bluez-utils bluez-firmware
systemctl enable bluetooth.service
```
## Создание пользователя admin для логина в Gnome

```bash
sudo useradd -m -g users -G wheel admin
passwd admin
```
Не забываем разрешить членам wheel юзать sudo, для чего необходимо выполнить
```bash
EDITOR=vim visudo
```
и расскоментировать строку вида
```bash
%wheel ALL=(ALL) ALL
```
после чего сохранить данное изменние.

## Установка yaourt

Добавляем 
```bash
[archlinuxfr]
Server = http://repo.archlinux.fr/x86_64
SigLevel = Optional TrustAll
```
в ==/etc/pacman.conf==, после чего выполняем

```bash
pacman -Sy yaourt
```

## Установка необходимого ПО
```bash
sudo -iu admin
sudo pacman -Sy mpv chromium firefox thunderbird filezilla keepassx2 bridge-utils net-tools iproute2 namcap calibre keepassxc pwgen 
yaourt -Sy google-chrome copyq copyq-plugin-itemweb nagstamon tilix skypeforlinux telegram bindfs apache-tools(если уже есть httpd, то не надо) httpstat-go the_silver_searcher
```
## Установка необходимых шрифтов
```bash
yaourt -S ttf-croscore ttf-dejavu ttf-liberation ttf-carlito ttf-caladea ttf-droid ttf-dejavu ttf-vista-fonts ttf-dejavu ttf-liberation noto-fonts fake-ms-fonts ttf-ubuntu-font-family-ib ttf-dejavu-ib
```

https://tehnojam.pro/category/software/delaem-krasivye-shrifty-s-novym-freetype2-v-linux.html

## Установка pkgfile для поиска пакетов, предоставляющих файл по маске

### pacman -Sy
```bash
systemctl enable pkgfile-update.timer
```

## Установка command-not-found
Устанавливаем command-not-found для того, что-бы система предлагала установить пакет, в случае если приложение не установлено в системе
```bash
yaourt -Sy command-not-found
```

## Устаналиваем retroarch
```bash
sudo pacman -Sy libretro-beetle-psx libretro-beetle-psx-hw  libretro-blastem libretro-bsnes libretro-desmume libretro-genesis-plus-gx  libretro-mupen64plus libretro-nestopia libretro-nestopia libretro-overlays libretro-reicast libretro-scummvm libretro-shaders libretro-shaders-glsl libretro-snes9x libretro-yabause
```

## Устаналиваем plymouth
```bash
yaourt -Sy plymouth
```
```bash
vim /etc/mkinitcpio.conf
```
в 

```ini
HOOKS="base udev plymouth autodetect modconf block btrfs filesystems keyboard fsck"
```
после ==udev== или ==systemd== добавляем plymouth.

в /boot/efi/efi/arch-grub/grub.cfg добавляем quiet splash
```bash
vim /boot/efi/efi/arch-grub/grub.cfg
```
```ini
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
```

```bash
systemctl disable gdm.service
systemctl enable gdm-plymouth.service
```
==Ссылки на полезные материалы==

* http://alv.me/antergos-Dovodka-konsoli/
* http://archlinux.org.ru/forum/topic/1090/
* http://eax.me/archlinux-install/
* http://www.akitaonrails.com/2017/01/10/arch-linux-best-distro-ever