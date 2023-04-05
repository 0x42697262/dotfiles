import env

from libqtile.lazy import lazy
from libqtile.config import Click, Drag

# Drag floating layouts.
mouse = [
    Drag([env.mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([env.mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([env.mod], "Button2", lazy.window.bring_to_front()),
]
