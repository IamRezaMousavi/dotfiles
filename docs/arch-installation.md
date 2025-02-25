# Arch Installation

This document is a guide for installing Arch Linux using the live system booted from an installation medium made from an official installation image. [arch-installation-guide](https://wiki.archlinux.org/title/installation_guide)

---

## Table of contents

- [Pre-installation](#pre-installation)
  - [Connect to internet](#connect-to-internet)
  - [Update the system clock](#update-the-system-clock)
  - [Partition the disks](#partition-the-disks)
  - [Format the partitions](#format-the-partitions)
  - [Mount the file systems](#mount-the-file-systems)
- [Installation](#installation)
  - [Select the mirrors](#select-the-mirrors)
  - [Install essential packages](#install-essential-packages)
- [Configure the system](#configure-the-system)
  - [Fstab](#fstab)
  - [Chroot](#chroot)
  - [Time zone](#time-zone)
  - [Localization](#localization)
  - [Hostname](#hostname)
  - [Network configuration](#network-configuration)
  - [Initramfs](#initramfs)
  - [Boot loader](#boot-loader)
- [System administration](#system-administration)
  - [Users and groups](#users-and-groups)
  - [Security](#security)
- [Package management](#package-management)
  - [Pacman](#pacman)
  - [Mirrors](#mirrors)
  - [Arch user repository](#arch-user-repository)
- [Graphical user interface](#graphical-user-interface)
  - [Display server](#display-server)
  - [Desktop environments](#desktop-environments)
- [Power managment](#power-managment)
  - [Cpu frequency scaling](#cpu-frequency-scaling)
- [Multimedia](#multimedia)
  - [Sound system](#sound-system)
- [Networking](#networking)
  - [Firewall](#firewall)
- [Input devices](#input-devices)
  - [Laptop touchscreen](#laptop-touchscreen)
- [Optimization](#optimization)
  - [Improving performance](#improving-performance)
- [System services](#system-services)
  - [Printing](#printing)
- [Appearance](#appearance)
  - [Fonts](#fonts)
  - [Gtk and Qt themes](#gtk-and-qt-themes)
- [Console improvements](#console-improvements)
  - [Tab-completion enhancements](#tab-completion-enhancements)
  - [Bash additions](#bash-additions)
  - [Session management](#session-management)
- [Missing firmwares](#missing-firmwares)
- [List of applications](#list-of-applications)
- [Bluetooth](#bluetooth)

---

## Pre-installation

### Connect to internet

#### iwctl

```bash
> iwctl
[iwd]> device list
[iwd]> station <device> scan
[iwd]> station <device> get-networks
[iwd]> station <device> connect <SSID>
[iwd]> station <device> connect-hidden <SSID>
```

#### Ping

```bash
ping archlinux.org
```

### Update the system clock

```bash
timedatectl status
```

### Partition the disks

```bash
> fdisk -l # for mbr
> fdisk /dev/the_disk_to_be_partitioned
```

```bash
> gdisk # for uefi
> cfdisk # In graphic mode
```

### Format the partitions

```bash
> mkfs.ext4 /dev/<partition_name>
> mkfs.fat -F 32 /dev/<efi_partition_name>
> mkswap /dev/<swap_partition_name>
```

### Mount the file systems

```bash
> mount /dev/<partition_name> /mnt
> mount --mkdir /dev/<efi_partition_name> /mnt/boot
> swapon /dev/<swap_partition_name>
```

---

## Installation

### Select the mirrors

```bash
> vim /etc/pacman.d/mirrorlist
```

### Install essential packages

```bash
> pacstrap -K /mnt base linux linux-firmware <intel-ucode>or<amd-ucode> networkmanager iwd vim man-db
```

---

## Configure the system

### Fstab

```bash
> genfstab -U /mnt >> /mnt/etc/fstab
```

### Chroot

```bash
> arch-chroot /mnt
```

### Time zone

```bash
> ln -sf /usr/share/zoneinfo/<region>/<city> /etc/localtime
> hwclock --systohc # to generate /etc/adjtime
```

### Localization

```bash
> nano /etc/locale.gen # uncomment en_US.UTF-8 UTF-8
> locale-gen
> echo "LANG=en_US.UTF-8" > /etc/locale.conf
```

### Hostname

```bash
> echo "<host_name>" > /etc/hostname
```

### Network configuration

```bash
> systemctl enable NetworkManager
```

### Initramfs

`-> usually not required <-`

```bash
> mkinitcpio -P
```

### Boot loader

```bash
> pacman -S grub efibootmgr
> grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
> grub-mkconfig -o /boot/grub/grub.cfg
```

---

## System administration

### Users and groups

```bash
> useradd -mG wheel <username>
> passwd <username>
```

### Security

```bash
> pacman -S sudo
> vim /etc/sudoers
# Uncomment to allow members of group wheel to execute any command
```

---

## Package management

### Pacman

```bash
> cp etc/pacman.conf /etc/pacman.conf
```

### Mirrors

```bash
> pacman -S reflector
> reflector --latest 5 --country <Country> --sort rate --save /etc/pacman.d/mirrorlist
```

### Arch User Repository

```bash
> pacman -S --needed git base-devel
> git clone https://aur.archlinux.org/yay.git
> cd yay
> makepkg -si
```

---

## Graphical user interface

### Display server

```bash
> pacman -S xorg xorg-drivers
```

### Desktop environments

```bash
> pacman -S gnome gdm gnome-tweaks gnome-shell-extensions
> systemctl enable gdm

> pacman -S gnome-terminal bash-completion
> pacman -R gnome-console
```

---

## Power managment

### CPU frequency scaling

```bash
> pacman -S power-profiles-daemon
> systemctl enable power-profiles-daemon
```

---

## Multimedia

### Sound system

```bash
> pacman -S pipewire pipewire-audio pipewire-alsa pipewire-pulse pipewire-jack
# reboot
```

---

## Networking

### Firewall

```bash
> pacman -S ufw
> systemctl enable ufw
> ufw enable
```

---

## Input devices

### Laptop touchscreen

```bash
cp etc/X11/xorg.conf.d/99-no-touchscreen.conf /etc/X11/xorg.conf.d/99-no-touchscreen.conf
```

---

## Optimization

### Improving performance

```bash
> pacman -S irqbalance
> systemctl enable irqbalance
```

---

## System services

### Printing

```bash
> pacman -S cups cups-pdf
> systemctl enable cups.socket
```

---

## Appearance

### fonts

```bash
> mkdir ~/.config/fontconfig
> cp fonts.conf ~/.config/fontconfig/
```

### GTK and Qt themes

```bash
> pacman -S adwaita-qt5 adwaita-qt6
> cp xinitrc ~/.xinitrc
```

---

## Console improvements

### Tab-completion enhancements

```bash
> pacman -S bash-completion
```

### Bash additions

```bash
> cp bashrc ~/.bashrc
```

### Session management

```bash
> pacman -S tmux
```

---

## Missing firmwares

```bash
> pacman -S linux-firmware-qlogic
> yay -S ast-firmware upd72020x-fw wd719x-firmware aic94xx-firmware
> mkinitcpio -P
```

---

## List of applications

```bash
> pacman -S firefox vlc libreoffice-fresh \
            ntfs-3g # for ntfs partition
> yay -S mkinitcpio-firmware persepolis-git gnome-terminal-transparency visual-studio-code-bin borna-fonts iran-nastaliq-fonts ttf-amiri vazirmatn-fonts ttf-pacifico ttf-architects-daughter fonts-tillana
```

---

## Bluetooth

```bash
> pacman -S bluez bluez-utils
> modprobe btusb # to load module
> systemctl enable bluetooth
```

---
