# Home Configs

|Distro|WM|Bar|Compositor|Terminal|Shell|Package Manager|
|------|------|------|------|------|------|------|
|[Arch](https://archlinux.org/)|[BSPWM](https://github.com/baskerville/bspwm)|[Polybar](https://github.com/polybar/polybar)|[Picom](https://github.com/Arian8j2/picom)|[Kitty](https://github.com/kovidgoyal/kitty)|[Zsh](https://github.com/zsh-users/zsh)|[Paru](https://aur.archlinux.org/packages/paru)|

# Setup (WIP)
---
## Zsh & Oh-My-Zsh

### Packages Used
```sh
fd powerline-fonts ttf-font-awesome 
```
### Plugins
- [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)
- [zsh-autosuggestions](zsh-autosuggestions)
- [zsh-Z](https://github.com/agkozak/zsh-z)
- [fzf](https://github.com/junegunn/fzf)

### Installing Oh-My-Zsh and plugins
1. Download and execute the [install script](https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh). Make sure to copy your old `.zshrc` configs to the new config.
2. Clone `zsh-syntax-highlighting` to `oh-my-zsh` plugins.
3. Clone `zsh-autosuggestions` to `oh-my-zsh` plugins.
4. CLone `zsh-Z` to `oh-my-zsh` plugins.
5. Clone and install `fzf`.
6. Install `fd`
7. Add the omz plugins in `.zshrc` config. ` fzf git history-substring-search colored-man-pages zsh-autosuggestions zsh-syntax-highlighting zsh-z`
8. Install [Powerlevel10k](https://github.com/romkatv/powerlevel10k#oh-my-zsh) and set the theme `powerlevel10k/powerlevel10k`.

```sh
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

git clone https://github.com/agkozak/zsh-z $ZSH_CUSTOM/plugins/zsh-z

git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install

paru -S fd

git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```
