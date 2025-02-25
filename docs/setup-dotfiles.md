# Setup Dotfiles

Refrence to setup dotfiles...

---

## Table of contents

- [Git](#git)
- [Change Default Shell](#change-default-shell)
- [Vim](#vim)
- [Nerd font](#nerd-font)
- [System font](#system-font)
- [Starship](#starship)
- [Desktop files](#desktop-files)
- [Set Default Application](#set-default-application)
- [Pacman cleaning](#pacman-cleaning)
- [Templates](#templates)
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

## Nerd font

Use for terminal font:

```bash
unzip ./nerd-font/DaddyTimeMono.zip -d DaddyTimeMono
mkdir -p ~/.local/share/fonts
cp ./DaddyTimeMono/*.ttf ~/.local/share/fonts/
rm -rf ./DaddyTimeMono/
```

---

## System font

Customize font of OS:

```bash
mkdir ~/.config/fontconfig
cp fonts.conf ~/.config/fontconfig/
```

---

## Starship

```bash
cp ./config/starship.toml ~/.config/
```

---

## Desktop files

Custome desktop files:

```bash
cp -r ./desktopfiles/* ~/.local/share/applications/
```

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

## Templates

create files with right click and chosing a template file:

```bash
cp -r Templates/ ~/Templates
```

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

