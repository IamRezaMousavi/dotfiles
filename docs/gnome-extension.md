# Gnome Extensions

Extensions that installed in gnome edsktop

---

## Extension List

- blur-my-shell

    ```sh
    git clone https://github.com/aunetx/blur-my-shell.git \
    && cd blur-my-shell \
    && make install
    ```

- dash-to-dock

    ```sh
    sudo pacman -S sassc \
    && git clone https://github.com/micheleg/dash-to-dock.git \
    && make -C dash-to-dock install
    ```

- desk-changer

    ```sh
    git clone -b develop git@github.com:BigE/desk-changer.git \
    && cd desk-changer \
    && make all \
    && make install
    ```

- desktop icon ng

    ```sh
    git clone https://gitlab.com/rastersoft/desktop-icons-ng.git \
    && ./local_install.sh
    ```

- gsconnect

    ```sh
    sudo pacman -S meson ninja \
    && git clone https://github.com/GSConnect/gnome-shell-extension-gsconnect.git \
    && cd gnome-shell-extension-gsconnect/ \
    && meson _build . \
    && ninja -C _build install-zip
    ```

- no-overview

    ```sh
    git clone https://github.com/fthx/no-overview.git \
    && no-overview \
    && mkdir -p ~/.local/share/gnome-shell/extensions/o-overview@fthx
    && cp metadata.json extension.js ~/.local/share/gnome-shell/extensions/o-overview@fthx/
    ```

- persian-gnome-calendar

    ```sh
    git clone https://github.com/IamRezaMousavi/persian-gnome-calendar-extension.git \
    && make install
    ```

- PrivacyMenu

    ```sh
    git clone https://github.com/stuarthayhurst/privacy-menu-extension.git \
    && cd privacy-menu-extension \
    && make build \
    && make install
    ```

- Tray-Icons-Reloaded

    ```sh
    git clone https://github.com/MartinPL/Tray-Icons-Reloaded.git \
    && make zip \
    && gnome-extension install trayIconsReloaded@selfmade.pl.zip
    ```
