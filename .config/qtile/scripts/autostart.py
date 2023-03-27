import os
import subprocess

from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    # apps = os.path.expanduser('sh/autostart.sh')
    apps = os.path.expanduser('~/.config/qtile/scripts/sh/autostart.sh')
    subprocess.Popen([apps])
