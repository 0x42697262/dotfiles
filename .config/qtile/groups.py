import env
import keys

from libqtile.config    import Group, Key
from libqtile.lazy      import lazy






groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.keys.extend(
        [
            # env.mod1 + letter of group = switch to group
            Key(
                [env.mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # env.mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [env.mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # env.mod1 + shift + letter of group = move focused window to group
            # Key([env.mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
