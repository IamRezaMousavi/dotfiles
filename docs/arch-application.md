# Arch Application

Applications that installed in arch linux desktop

---

## Application List

With `pacman`:

```bash
sudo pacman -S linux-firmware-qlogic \
fastfetch onefetch \
firefox \
git \
vlc \
libreoffice-fresh \
v2ray \
gnome-terminal bash-completion \
ntfs-3g dosfstools \
tmux vim nvim \
virtualbox virtualbox-guest-iso \
# virtualbox-host-module-arch
starship bat eza \
cups cups-pdf \
ufw \
irqbalance power-profiles-daemon \
man-db \
docker \
p7zip \
evince \
gnome-sudoku gnome-chess gnuchess \
meson ninja \
nodejs npm \
pkgfile
```

With `yay`:

```bash
yay -S \
ast-firmware upd72020x-fw wd719x-firmware aic94xx-firmware \
gnome-terminal-transparency \
qv2ray \
visual-studio-code-bin \
borna-fonts iran-nastaliq-fonts ttf-amiri vazirmatn-fonts ttf-pacifico ttf-architects-daughter fonts-tillana \
postman-bin \
anydesk-bin rustdesk-bin \
p7zip-gui \
localsend-bin \
marktext \
google-chrome
```

With `flatpak`:

```bash
flatpak install flathub \
io.bassi.Amberol \
com.usebottles.bottles \
&& flatpak override com.usebottles.bottles --user --filesystem=xdg-data/applications
```
