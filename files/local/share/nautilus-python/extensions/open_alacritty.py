#!/usr/bin/python3

from gi import require_version

require_version("Gtk", "4.0")
require_version("Nautilus", "4.0")

from gi.repository import Nautilus, GObject

import os
import subprocess

PROCESSNAME = "alacritty"


class OpenAlacrittyExtension(GObject.GObject, Nautilus.MenuProvider):
    def launch_alacritty(self, _menu: Nautilus.MenuItem, files):
        path = ""
        args = "--working-directory"

        for file in files:
            dirpath = file.get_location().get_path()
            if os.path.isdir(dirpath):
                path = dirpath
            elif os.path.isfile(dirpath):
                path = os.path.dirname(dirpath)

        subprocess.Popen([PROCESSNAME, args, path], shell=False)

    def get_file_items(self, files):
        item = Nautilus.MenuItem(
            name="OpenAlacrittyExtension::file",
            label="Open Alacritty here",
            tip="Open a terminal window here using Alacritty",
        )
        item.connect("activate", self.launch_alacritty, files)
        return [item]

    def get_background_items(self, current_dir):
        item = Nautilus.MenuItem(
            name="OpenAlacrittyExtension::background",
            label="Open Alacritty here",
            tip="Open a terminal window here using Alacritty",
        )
        item.connect("activate", self.launch_alacritty, [current_dir])
        return [item]

