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
  - [Mirrors](#mirrors)
  - [Arch user repository](#arch-user-repository)
- [Graphical user interface](#graphical-user-interface)
  - [Display server](#display-server)
  - [Desktop environments](#desktop-environments)
- [Power managment](#power-managment)
  - [ACPI events](#acpi-events)
  - [Cpu frequency scaling](#cpu-frequency-scaling)
- [Multimedia](#multimedia)
  - [Sound system](#sound-system)
- [Networking](#networking)
  - [Firewall](#firewall)
- [Input devices](#input-devices)
  - [Laptop touchscreen](#laptop-touchscreen)
- [Optimization](#optimization)
  - [Improving performance](#improving-performance)
  - [Solid state drives](#solid-state-drives)
- [System services](#system-services)
  - [Printing](#printing)
- [Appearance](#appearance)
  - [Fonts](#fonts)
- [Console improvements](#console-improvements)
  - [Tab-completion enhancements](#tab-completion-enhancements)
  - [Alternative shells](#alternative-shells)
  - [Bash additions](#bash-additions)
  - [Console prompt](#console-prompt)
  - [Mouse support](#mouse-support)
  - [Session management](#session-management)
- [List of applications](#list-of-applications)
- [Missing firmwares](#missing-firmwares)
- [Bluetooth](#bluetooth)

---

## Pre-installation

### Connect to internet

#### iwctl

```sh
> iwctl
[iwd]> device list
[iwd]> station <device> scan
[iwd]> station <device> get-networks
[iwd]> station <device> connect <SSID>
[iwd]> station <device> connect-hidden <SSID>
```

#### Ping

```sh
ping archlinux.org
```

### Update the system clock

```sh
timedatectl status
```

### Partition the disks

```sh
> fdisk -l # for mbr
> fdisk /dev/the_disk_to_be_partitioned
> gdisk # for uefi
```

```sh
> cfdisk # In graphic mode
```

### Format the partitions

```sh
> mkfs.ext4 /dev/<partition_name>
> mkfs.fat -F 32 /dev/<efi_partition_name>
> mkswap /dev/<swap_partition_name>
```

### Mount the file systems

```sh
> mount /dev/<partition_name> /mnt
> mount --mkdir /dev/<efi_partition_name> /mnt/boot
> swapon /dev/<swap_partition_name>
```

#### Swap

```sh
> pacman -S zram-generator
> systemctl enable systemd-zram-setup@zram0
```

---

## Installation

### Select the mirrors

```sh
> vim /etc/pacman.d/mirrorlist
```

### Install essential packages

```sh
> pacstrap -K /mnt base linux linux-firmware <intel-ucode>or<amd-ucode> networkmanager iwd vim man-db
```

---

## Configure the system

### Fstab

```sh
> genfstab -U /mnt >> /mnt/etc/fstab
```

### Chroot

```sh
> arch-chroot /mnt
```

### Time zone

```sh
> ln -sf /usr/share/zoneinfo/<region>/<city> /etc/localtime
> hwclock --systohc # to generate /etc/adjtime
```

### Localization

```sh
> nano /etc/locale.gen # uncomment en_US.UTF-8 UTF-8
> locale-gen
> echo "LANG=en_US.UTF-8" > /etc/locale.conf
```

### Hostname

```sh
> echo "<host_name>" > /etc/hostname
```

### Network configuration

```sh
> systemctl enable NetworkManager
```

### Initramfs

`-> usually not required <-`

```sh
> mkinitcpio -P
```

### Boot loader

```sh
> pacman -S grub efibootmgr
> grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
> grub-mkconfig -o /boot/grub/grub.cfg
```

---

## System administration

### Users and groups

```sh
> useradd -mG wheel <username> # create and add user to wheel group
> passwd <username>
```

### Security

```sh
> pacman -S sudo
> vim /etc/sudoers
# Uncomment to allow members of group wheel to execute any command
```

---

## Package management

### Mirrors

```sh
> pacman -S reflector
> reflector --latest 5 --country <Country> --sort rate --save /etc/pacman.d/mirrorlist
```

### Arch User Repository

```sh
> pacman -S --needed git base-devel
> git clone https://aur.archlinux.org/yay.git
> cd yay
> makepkg -si
```

---

## Graphical user interface

### Display server

```sh
> pacman -S xorg xorg-drivers
```

### Desktop environments

```sh
> pacman -S gnome gdm gnome-tweaks gnome-shell-extensions
> systemctl enable gdm

> pacman -S gnome-terminal bash-completion
> pacman -R gnome-console
```

---

## Power managment

### ACPI events

```sh
> pacman -S acpid
> systemctl enable acpid
```

### CPU frequency scaling

```sh
> pacman -S cpupower power-profiles-daemon
> systemctl enable cpupower
> systemctl enable power-profiles-daemon
> yay -S auto-cpufreq
> systemctl auto-cpufreq
```

---

## Multimedia

### Sound system

```sh
> pacman -S pipewire pipewire-audio pipewire-alsa pipewire-pulse pipewire-jack
> reboot
```

---

## Networking

### Firewall

```sh
> pacman -S ufw
> systemctl enable ufw
> ufw enable
```

---

## Input devices

### Laptop touchscreen

```sh
cp etc/X11/xorg.conf.d/99-no-touchscreen.conf /etc/X11/xorg.conf.d/99-no-touchscreen.conf
```

---

## Optimization

### Improving performance

```sh
> pacman -S irqbalance
> systemctl enable irqbalance
```

### Solid state drives

```sh
> systemctl status fstrim.timer
> vim /etc/fstab
# Using the discard option for a mount in /etc/fstab enables continuous TRIM in device operations:
# /dev/sda1  /           ext4  defaults,discard   0  1
```

---

## System services

### Printing

```sh
> pacman -S cups cups-pdf
> systemctl enable cups.socket
```

---

## Appearance

### fonts

```sh
> mkdir ~/.config/fontconfig
> cp fonts.conf ~/.config/fontconfig/
> mkdir ~/.local/share/fonts
> cp font.ttf ~/.local/share/fonts
```

---

## Console improvements

### Tab-completion enhancements

```sh
> pacman -S bash-completion
```

### Alternative shells

```sh
> pacman -S zsh zsh-completions zsh-syntax-highlighting zsh-autosuggestions
> chsh -l
> chsh -s /full/path/to/shell
```

### Bash additions

```sh
> cp bashrc ~/.bashrc
```

### Console prompt

```sh
> pacman -S starship
```

### Mouse support

```sh
> pacman -S gpm
```

### Session management

```sh
> pacman -S tmux
```

---

## List of applications

- With pacman:

  ```sh
  > pacman -S \
    libreoffice-fresh evince \
    firefox chromium \
    curl wget qbittorrent \
    thunderbird pidgin telegram-desktop \
    inkscape vlc \
    nmap tcpdump wireshark-qt bitwarden \
    alacritty gnome-terminal rsync bat eza gitea git cmake meson ninja jq dust htop fastfetch onefetch \
    virtualbox virtualbox-guest-iso \
    # virtualbox-host-module-arch \
    zram-generator ntfs-3g \
    docker \
    pkgfile
  ```

- With yay:

  ```sh
  > yay -S \
    visual-studio-code-bin \
    localsend-bin rustdesk-bin \
    p7zip-gui \
    gnome-terminal-transparency \
    activitywatch-bin \
    borna-fonts iran-nastaliq-fonts ttf-amiri vazirmatn-fonts ttf-pacifico ttf-architects-daughter fonts-tillana
  ```

---

## Missing firmwares

```sh
> pacman -S linux-firmware-qlogic
> yay -S ast-firmware upd72020x-fw wd719x-firmware aic94xx-firmware
> mkinitcpio -P
```

---

## Bluetooth

```sh
> pacman -S bluez bluez-utils
> modprobe btusb # to load module
> systemctl enable bluetooth
```

---
