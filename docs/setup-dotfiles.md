# Setup Dotfiles

Refrence to setup dotfiles...

---

## Table of contents

- [Git](#git)
- [Change Default Shell](#change-default-shell)
- [Vim](#vim)
- [Set Default Application](#set-default-application)
- [Pacman cleaning](#pacman-cleaning)
- [ARM Toolchain](#arm-toolchain)
- [Android Studio](#android-studio)

---

## Git

```bash
cp gitconfig ~/.gitconfig
```

Install `gnome-keyring`, `libsecret`

For remove passwords:

```bash
rm ~/.local/share/keyrings/user.keystore
or
rm ~/.local/share/keyrings/login.keystore
```

Or

```bash
git config --global --unset credential.helper
git push
```

Export Git Repo:

```bash
# zip archive
git archive -o output.zip master
```

---

## Change Default Shell

```sh
chsh -l
chsh -s full-path-to-shell
```

---

## Vim

```bash
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
cp ./vimrc ~/.vimrc
```

then run `PluginInstall` in `vim`

---

## Set Default Application

```bash
xdg-mime query default inode/directory
xdg-mime default org.gnome.nautilus.desktop inode/directory
```

---

## Pacman Cleaning

Clean unused packages:

```bash
sudo pacman -Qtdq | sudo pacman -Rns -
```

To clean unneeded cache:

Install `pacman-contrib` and run:

```bash
paccache -r
```

and can enable `paccache.timer` with systemd

---

## ARM Toolchain

To install:

```bash
sudo pacman -S arm-none-eabi-gcc arm-none-eabi-newlib arm-none-eabi-binutils openocd
```

---

## Desktop Shortcut

To enable `switch window`:

```bash
gsettings set org.gnome.desktop.wm.keybindings switch-windows "['<Alt>Tab']"
```

---

## Android Studio

To install android studio deps:

```bash
sudo pacman -S lib32-glibc lib32-ncurses lib32-gcc-libs lib32-zlib lib32-bzip2
```

---
