# Command-Line Interface

A command-line interface (CLI) is a means of interacting with a device or computer program with commands from a user or client, and responses from the device or program, in the form of lines of text. [wikipedia](https://en.wikipedia.org/wiki/Command-line_interface)

---

## Table of contents

- [CLI Application](#cli-application)
  - [Benchmarking](#benchmarking)
  - [Disk Usage Analyzer](#disk-usage-analyzer)
  - [Document Site Generator](#document-site-generator)
  - [Game](#game)
  - [Git](#git)
  - [Files](#files)
  - [System Information](#system-information)
  - [Terminal Multiplexer](#terminal-multiplexer)
  - [Text Editor](#text-editor)
- [Customization](#customization)
- [Linter](#linter)
- [Shell](#shell)
- [Terminal Emulator](#terminal-emulator)

---

## CLI Application

**[`^    back to top    ^`](#table-of-contents)**

A command-line interface (CLI) is a means of interacting with a device or computer program with commands from a user or client, and responses from the device or program, in the form of lines of text. [wikipedia](https://en.wikipedia.org/wiki/Command-line_interface)

### Benchmarking

Benchmarking is the practice of comparing business processes and performance metrics to industry bests and best practices from other companies. Dimensions typically measured are quality, time and cost. [wikipedia](https://en.wikipedia.org/wiki/Benchmarking)

- hyperfine: A command-line benchmarking tool. [github](https://github.com/sharkdp/hyperfine) `Apache-2.0, MIT` `Rust`
  - arch: `hyperfine`

### Disk Usage Analyzer

- erdtree (erd): A modern, cross-platform, multi-threaded, and general purpose filesystem and disk-usage utility that is aware of .gitignore and hidden file rules. [github](https://github.com/solidiquis/erdtree) `MIT` `Rust`
  - arch: `erdtree`

### Document Site Generator

- doctave: Doctave is an opinionated documentation site generator that converts your Markdown files into a beautiful documentation site with minimal effort. [github](https://github.com/Doctave/doctave) `MIT` `Rust`

### Game

- [nudoku](http://jubalh.github.io/nudoku/): nudoku is a ncurses based sudoku game. [github](https://github.com/jubalh/nudoku) `GPL-3.0` `C`
  - aur: `nudoku`

### Git

- [onefetch](https://onefetch.dev/): Onefetch is a command-line Git information tool that displays project information and code statistics for a local Git repository directly to your terminal. [github](https://github.com/o2sh/onefetch) `MIT` `Rust`
  - arch: `onefetch`

### Files

- bat: A cat(1) clone with syntax highlighting and Git integration. [github](https://github.com/sharkdp/bat) `Apache-2.0 and MIT` `Rust`
  - arch: `bat`
- [eza](https://the.exa.website/):  A modern replacement for `ls`. [github](https://github.com/eza-community/eza) `MIT` `Rust`
  - aur: `eza`

### System Information

- neofetch: Neofetch displays information about your operating system, software and hardware in an aesthetic and visually pleasing way. [github](https://github.com/dylanaraps/neofetch) `MIT` `Bash`
  - arch: `neofetch`

- fastfetch: Fastfetch is a neofetch-like tool for fetching system information and displaying them in a pretty way. It is written mainly in C, with performance and customizability in mind. Currently, Linux, Android, FreeBSD, MacOS and Windows 7+ are supported. [github](https://github.com/fastfetch-cli/fastfetch) `MIT` `C`
  - arch: `fastfetch`

### Terminal Multiplexer

- [tmux](https://github.com/tmux/tmux/wiki): tmux is a terminal multiplexer. It lets you switch easily between several programs in one terminal, detach them (they keep running in the background) and reattach them to a different terminal. [github](https://github.com/tmux/tmux) `ISC` `C`
  - arch: `tmux`

### Text Editor

See [editor](./editor.md#console)

---

## Customization

**[`^    back to top    ^`](#table-of-contents)**

- [Starship](https://starship.rs/): The minimal, blazing-fast, and infinitely customizable prompt for any shell! [github](https://github.com/starship/starship) `ISC license` `Rust`
  - arch: `starship`

---

## Linter

**[`^    back to top    ^`](#table-of-contents)**

See [linter](./linter.md#shell)

---

## Shell

**[`^    back to top    ^`](#table-of-contents)**

A shell is a computer program that exposes an operating system's services to a human user or other programs. In general, operating system shells use either a command-line interface (CLI) or graphical user interface (GUI), depending on a computer's role and particular operation. It is named a shell because it is the outermost layer around the operating system. [wikipedia](https://en.wikipedia.org/wiki/Shell_(computing))

- [Bash](https://www.gnu.org/software/bash/): Bash is the GNU Project's shell—the Bourne Again SHell. [source-code](https://git.savannah.gnu.org/cgit/bash.git) `GPL-3.0-or-later` `C`
  - arch: `bash`

- [Zsh](https://www.zsh.org/): Zsh is a shell designed for interactive use, although it is also a powerful scripting language. [source-code](https://sf.net/p/zsh/code/) `MIT-Modern-Variant` `C`
  - arch: `zsh`

- [Powershell](https://microsoft.com/PowerShell): PowerShell is a cross-platform (Windows, Linux, and macOS) automation and configuration tool/framework that works well with your existing tools and is optimized for dealing with structured data (e.g. JSON, CSV, XML, etc.), REST APIs, and object models. [github](https://github.com/PowerShell/PowerShell) `MIT` `C#`
  - aur: `powershell`

---

## Terminal Emulator

**[`^    back to top    ^`](#table-of-contents)**

- [Alacritty](https://alacritty.org/): Alacritty is a modern terminal emulator that comes with sensible defaults, but allows for extensive configuration. [github](https://github.com/alacritty/alacritty) `MIT-or-Apache-2.0` `Rust`
  - arch: `alacritty`

- [Gnome Terminal](https://wiki.gnome.org/Apps/Terminal): A terminal emulator for the GNOME desktop [source-code](https://gitlab.gnome.org/GNOME/gnome-terminal) `GPL-3.0` `C++`
  - arch: `gnome-terminal`
  - plugins:
    - aur: `gnome-terminal-transparency`

- [Windows Terminal](https://aka.ms/terminal): The new Windows Terminal and the original Windows console host, all in the same place! [github](https://github.com/microsoft/terminal) `MIT` `C++`
  - winget: `--id Microsoft.WindowsTerminal -e`
  - scoop:

    ```sh
    scoop bucket add extras
    scoop install windows-terminal
    ```
