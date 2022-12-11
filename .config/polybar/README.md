**TODO**:
- [ ] Colors
- [ ] Bar/taskbar
  - [ ] modules-right
    - [x] pulseaudio
    - [x] backlight
    - [x] memory
    - [x] cpu
    - [x] temperature
    - [x] battery
    - [x] date

# Fonts
```sh
paru -S nerd-fonts-complete
```

# Colors
```sh
icon_settings_color                        = #bde3ce              
icon_stats_color                           = #ffbac5
icon_info_color                            = #fed792

```

# Bar
## taskbar

```
modules-left = bspwm 
modules-center = title
modules-right = pulseaudio backlight memory cpu temperature battery date 
```
Need these guys for the virtual desktops and window title.

# Module
## date
Icons
```

```

## memory
Icons
```

```

## cpu
Icons
```

```

## temperature
Icons
```

```

## battery
Icons
```

```

## pulseaudio
Icons
```
奄 奔 墳 婢
```

## backlight
```
card = amdgpu_bl0
```
Using this to check my screen brightness.

```sh
$ ls -1 /sys/class/backlight/
```
Check list of available cards.

Icons
```

```

