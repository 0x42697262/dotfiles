# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=10000
SAVEHIST=10000
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '$HOME/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

###
#
# Load my aliases
if [ -f ~/.config/.zsh/.aliases ]; then
  source ~/.config/.zsh/.aliases
fi

export PATH="$HOME/.local/bin/:$PATH"
