# Packages Used

```sh
ranger kitty rofi ksnip
```

# INFOS
For `xbacklight` control, I used `acpilight` <sup>[source](https://gitlab.com/wavexx/acpilight)</sup> since it does not work on my laptop.

`ksnip` takes time to run.

<sub>don't ask why i have 20 workspaces</sub>

## sxhdd-help
```bash
#!/bin/bash

awk '/^[a-z]/ && last {print "<small>",$0,"\t",last,"</small>"} {last=""} /^#/{last=$0}' ~/.config/sxhkd/sxhkdrc{,.common} |
    column -t -s $'\t' |
    rofi -dmenu -i -markup-rows -no-show-icons -width 1000 -lines 15 -yoffset 40
```
This scipt was taken from [this site](https://my-take-on.tech/2020/07/03/some-tricks-for-sxhkd-and-bspwm/). Although this needs some fixing.
