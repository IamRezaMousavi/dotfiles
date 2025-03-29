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
> gdisk # for uefi
```

```bash
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

#### Swap

```bash
> pacman -S zram-generator
> systemctl enable systemd-zram-setup@zram0
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
> useradd -mG wheel <username> # create and add user to wheel group
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

### ACPI events

```bash
> pacman -S acpid
> systemctl enable acpid
```

### CPU frequency scaling

```bash
> pacman -S cpupower power-profiles-daemon
> systemctl enable cpupower
> systemctl enable power-profiles-daemon
> yay -S auto-cpufreq
> systemctl auto-cpufreq
```

---

## Multimedia

### Sound system

```bash
> pacman -S pipewire pipewire-audio pipewire-alsa pipewire-pulse pipewire-jack
> reboot
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

### Solid state drives

```bash
> systemctl status fstrim.timer
> vim /etc/fstab
# Using the discard option for a mount in /etc/fstab enables continuous TRIM in device operations:
# /dev/sda1  /           ext4  defaults,discard   0  1
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
> mkdir ~/.local/share/fonts
> cp font.ttf ~/.local/share/fonts
```

---

## Console improvements

### Tab-completion enhancements

```bash
> pacman -S bash-completion
```

### Alternative shells

```bash
> pacman -S zsh zsh-completions zsh-syntax-highlighting zsh-autosuggestions
> chsh -l
> chsh -s /full/path/to/shell
```

### Bash additions

```bash
> cp bashrc ~/.bashrc
```

### Console prompt

```bash
> pacman -S starship
```

### Mouse support

```bash
> pacman -S gpm
```

### Session management

```bash
> pacman -S tmux
```

---

## List of applications

- With pacman:

  ```bash
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

  ```bash
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

```bash
> pacman -S linux-firmware-qlogic
> yay -S ast-firmware upd72020x-fw wd719x-firmware aic94xx-firmware
> mkinitcpio -P
```

---

## Bluetooth

```bash
> pacman -S bluez bluez-utils
> modprobe btusb # to load module
> systemctl enable bluetooth
```

---
