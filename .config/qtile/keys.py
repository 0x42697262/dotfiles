import env

from libqtile.lazy      import lazy
from libqtile.config    import Key


"""
    Key shortcut configuration    


    TODO:
        Everything here is to be riced
        Will have to grab my sxhkd configs and transfer it here.
"""


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([env.mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([env.mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([env.mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([env.mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([env.mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([env.mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([env.mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([env.mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([env.mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([env.mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([env.mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([env.mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([env.mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([env.mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [env.mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([env.mod], "Return", lazy.spawn(env.terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([env.mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([env.mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([env.mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([env.mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([env.mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

