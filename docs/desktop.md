# Desktop Environment

Documentation of Desktop Environment usage

---

## Table of contents

- [Gnome](#gnome)

---

## Gnome

GNOME is a free and open-source desktop environment for Linux and other Unix-like operating systems. `GPL-2.0-or-later` `C`

### Desktop Shortcut

To enable `switch window`:

```sh
gsettings set org.gnome.desktop.wm.keybindings switch-windows "['<Alt>Tab']"
```

---

## X Desktop Group

freedesktop.org (fd.o), formerly X Desktop Group (XDG), is a project to work on interoperability and shared base technology for free-software desktop environments for the X Window System (X11) and Wayland on Linux and other Unix-like operating systems. [wikipedia](https://en.wikipedia.org/wiki/Freedesktop.org)

### Default Application

To set default application, run this:

```sh
xdg-mime query default inode/directory
xdg-mime default org.gnome.nautilus.desktop inode/directory
```

---
