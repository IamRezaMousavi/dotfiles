# Dotfiles

Documentation of environment that I like

---

## Table of contents

- [Installation](#installation)
  - [Arch Installation](#arch-installation)
  - [Setup Dotfiles](#setup-dotfiles)
- [Softwares](#softwares)
  - [Bittorret](#bittorrent)
  - [Command-line Interface](#command-line-interface)
  - [Cryptography](#cryptography)
  - [Editor](#editor)
  - [Email](#email)
  - [File Management](#file-management)
    - [File Archiver](#file-archiver)
  - [Finances](#finances)
  - [Firewall](#firewall)
  - [Font](#font)
  - [Launcher](#launcher)
  - [Media Player](#media-player)
  - [Office](#office)
  - [Password Manager](#password-manager)
  - [Programming Language](#programming-language)
  - [Screen Recorder](#screen-recorder)
  - [Self hosted](#self-hosted)
  - [Version Control](#version-control)
  - [Virtualization](#virtualization)
  - [Wine](#wine)

---

## Installation

### Arch Installation

See [arch-installation](./arch-installation.md)

### Setup Dotfiles

See [setup-dotfiles](./setup-dotfiles.md)

---

## Softwares

### Bittorrent

**[`^    back to top    ^`](#table-of-contents)**

BitTorrent is a communication protocol for peer-to-peer file sharing (P2P), which enables users to distribute data and electronic files over the Internet in a decentralized manner. [wikipedia](https://en.wikipedia.org/wiki/BitTorrent)

- [qbittorrent](https://www.qbittorrent.org/): qBittorrent is a cross-platform free and open-source BitTorrent client written in native C++. It relies on Boost, Qt 6 toolkit and the libtorrent-rasterbar library, with an optional search engine written in Python. [github](https://github.com/qbittorrent/qBittorrent) `GPL-3.0` `C++`
  - arch: `qbittorrent`

---

### Command-Line Interface

**[`^    back to top    ^`](#table-of-contents)**

A command-line interface (CLI) is a means of interacting with a device or computer program with commands from a user or client, and responses from the device or program, in the form of lines of text. [wikipedia](https://en.wikipedia.org/wiki/Command-line_interface)

See [cli](./cli.md)

---

### Cryptography

**[`^    back to top    ^`](#table-of-contents)**

Encryption software is software that uses cryptography to prevent unauthorized access to digital information. Cryptography is used to protect digital information on computers as well as the digital information that is sent to other computers over the Internet. [wikipedia](https://en.wikipedia.org/wiki/Encryption_software)

- [GnuPG](https://gnupg.org/): GnuPG is a complete and free implementation of the OpenPGP standard as defined by RFC4880 (also known as PGP). GnuPG allows you to encrypt and sign your data and communications; it features a versatile key management system, along with access modules for all kinds of public key directories. [source-code](https://git.gnupg.org/) `GPL-3.0-or-later` `C`
  - For usage see [gpg-usage](./gpg-usage.md)

---

### Editor

**[`^    back to top    ^`](#table-of-contents)**

A text editor is a type of computer program that edits plain text. [wikipedia](https://en.wikipedia.org/wiki/Text_editor)

A source-code editor is a text editor program designed specifically for editing source code of computer programs. [wikipedia](https://en.wikipedia.org/wiki/Source-code_editor)

See [editor](./editor.md)

---

### Email

**[`^    back to top    ^`](#table-of-contents)**

Electronic mail (email or e-mail) is a method of transmitting and receiving messages using electronic devices. [wikipedia](https://en.wikipedia.org/wiki/Email)

- [thunderbird](https://www.thunderbird.net/): Mozilla Thunderbird is a free and open-source cross-platform email client, personal information manager, news client, RSS and chat client that is operated by the Mozilla Foundation's subsidiary MZLA Technologies Corporation. [source-code](https://hg.mozilla.org/comm-central) `MPL-2.0` `C`
  - arch: `thunderbird`

---

### File Management

**[`^    back to top    ^`](#table-of-contents)**

#### File Archiver

- p7zip: 7-Zip is a free and open-source file archiver, a utility used to place groups of files within compressed containers known as "archives". [github](https://github.com/p7zip-project/p7zip) `LGPL-2.1-or-later` `C`
  - arch: `p7zip`
  - [p7zip-gui](https://p7zip.sourceforge.net/): Graphic user interface (alpha quality) for the 7zip file archiver. [source-code](https://sourceforge.net/projects/p7zip/) `LGPL` `C++`
    - aur: `p7zip-gui`

---

### Finances

**[`^    back to top    ^`](#table-of-contents)**

Finance is the study and discipline of money, currency and capital assets. [wikipedia](https://en.wikipedia.org/wiki/Finance)

- Denaro: Manage your personal finances. [github](https://github.com/NickvisionApps/Denaro) `MIT` `C#`
  - aur: `denaro`

- [Trust wallet](https://trustwallet.com/): Trust Wallet is the best ethereum wallet and cryptocurrency wallet to store your favourite BEP2, ERC20 and ERC721, tokens. [github](https://github.com/trustwallet/wallet-core) `MIT` `C++`
  - Just for mobiles and browsers

---

### Firewall

**[`^    back to top    ^`](#table-of-contents)**

Firewall is a network security system that monitors and controls incoming and outgoing network traffic based on configurable security rules. [wikipedia](https://en.wikipedia.org/wiki/Firewall_(computing))

- UFW: Uncomplicated Firewall. [source-code](https://git.launchpad.net/ufw) `GPL` `Python`
  - arch: `ufw`
  - see [ufw](./ufw.md)

---

### Font

**[`^    back to top    ^`](#table-of-contents)**

Each font is a matched set of type, with a piece (a "sort") for each glyph. A typeface consists of various fonts that share an overall design. [wikipedia](https://en.wikipedia.org/wiki/Font)

See [font](./font.md)

---

### Launcher

**[`^    back to top    ^`](#table-of-contents)**

- [ulauncher](https://ulauncher.io/): Linux Application Launcher. [github](https://github.com/Ulauncher/Ulauncher) `GPL-3.0` `Python`
  - aur: `ulauncher`

---

### Media Player

**[`^    back to top    ^`](#table-of-contents)**

Media player software is a type of application software for playing multimedia computer files like audio and video files. [wikipedia](https://en.wikipedia.org/wiki/Media_player_software)

- [Amberol](https://apps.gnome.org/app/io.bassi.Amberol/): A small and simple sound and music player that is well integrated with GNOME. [source-code](https://gitlab.gnome.org/World/amberol) `GPL-3.0-or-later` `Rust`
  - aur: `amberol`
  - flathub: `io.bassi.Amberol`

- [vlc](https://www.videolan.org/vlc/): VLC is a free and open source cross-platform multimedia player and framework that plays most multimedia files, and various streaming protocols. [source-code](https://code.videolan.org/videolan/vlc) `GPL-2.0-or-later` `C-C++`
  - arch: `vlc`

---

### Office

**[`^    back to top    ^`](#table-of-contents)**

An office suite is a bundle of productivity software (a software suite) intended to be used by office workers. [wikipedia](https://en.wikipedia.org/wiki/Productivity_software#Office_suite)

- [libreoffice](https://www.libreoffice.org/): LibreOffice is a free and powerful office suite [source-code](https://git.libreoffice.org/core) `MPL-2.0` `C++`
  - arch: `libreoffice-fresh`

---

### Password Manager

**[`^    back to top    ^`](#table-of-contents)**

A password manager is a computer program that allows users to store. Password managers can generate passwords and fill online forms. [wikipedia](https://en.wikipedia.org/wiki/Password_manager)

- [Bitwarden (Client)](https://bitwarden.com/): Bitwarden is an integrated open source password management solution for individuals, teams, and business organizations. [github](https://github.com/bitwarden/clients) `GPL-3.0-only` `Typescript`
  - arch: `bitwarden`

---

### Programming Language

**[`^    back to top    ^`](#table-of-contents)**

A programming language is a system of notation for writing computer programs. [wikipedia](https://en.wikipedia.org/wiki/Programming_language)

- See [programming-languages](./programming-languages.md)

---

### Screen Recorder

**[`^    back to top    ^`](#table-of-contents)**

A screencast is a digital recording of computer screen output, also known as a video screen capture or a screen recording, often containing audio narration. [wikipedia](https://en.wikipedia.org/wiki/Screencast)

- [OBS Studio](https://obsproject.com/): Free and open source software for live streaming and screen recording. [github](https://github.com/obsproject/obs-studio) `GPL-2.0-or-later` `C`
  - arch: `obs-studio`

---

### Self Hosted

**[`^    back to top    ^`](#table-of-contents)**

Self-hosting is the practice of running and maintaining a website or service using a private web server, instead of using a service outside of someone's own control. Self-hosting allows users to have more control over their data, privacy, and computing infrastructure, as well as potentially saving costs and improving skills. [wikipedia](https://en.wikipedia.org/wiki/Self-hosting_(web_services))

See [self-hosted](./self-hosted.md)

---

### Version Control

**[`^    back to top    ^`](#table-of-contents)**

In software engineering, version control is a class of systems responsible for managing changes to computer programs, documents, large web sites, or other collections of information. Version control is a component of software configuration management. [wikipedia](https://en.wikipedia.org/wiki/Version_control)

- [Git](https://git-scm.com/): Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. [source-code](https://git.kernel.org/pub/scm/git/git.git) `GPL-2.0-only` `C`
  - arch: `git`

---

### Virtualization

**[`^    back to top    ^`](#table-of-contents)**

Virtualization is the act of creating a virtual version of something at the same abstraction level, including virtual computer hardware platforms, storage devices, and computer network resources. [wikipedia](https://en.wikipedia.org/wiki/Virtualization)

- [docker](https://www.docker.com/): Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. [github](https://github.com/moby/moby) `Apache-2.0` `Go`
  - arch: `docker`
  - desktop: [link](https://www.docker.com/products/docker-desktop/)

- [virtualbox](https://www.virtualbox.org/): VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use. [source-code](https://www.virtualbox.org/browser/vbox/trunk) `GPL-3.0` `C++`
  - arch: `virtualbox` (`virtualbox-host-modules-arch`)
  - arch: `virtualbox-guest-iso`

---

### Wine

**[`^    back to top    ^`](#table-of-contents)**

Wine is a free and open-source compatibility layer that aims to allow application software and computer games developed for Microsoft Windows to run on Unix-like operating systems. [wikipedia](https://en.wikipedia.org/wiki/Wine_(software))

License: `LGPL-2.0-or-later`

Written in: `C`

[source-code](https://source.winehq.org/git/wine.git)

- [Bottles](https://usebottles.com/): Bottles is free and open source software that uses environments to help you easily manage and run Windows apps on Linux. [github](https://github.com/bottlesdevs/Bottles) `GPL-3.0` `Python`
  - flathub (recommended): `com.usebottles.bottles`
    - permision: `flatpak override com.usebottles.bottles --user --filesystem=xdg-data/applications`

---
