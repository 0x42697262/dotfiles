# Setup fzf
# ---------
if [[ ! "$PATH" == */home/birb/.fzf/bin* ]]; then
  PATH="${PATH:+${PATH}:}/home/birb/.fzf/bin"
fi

# Auto-completion
# ---------------
[[ $- == *i* ]] && source "/home/birb/.fzf/shell/completion.zsh" 2> /dev/null

# Key bindings
# ------------
source "/home/birb/.fzf/shell/key-bindings.zsh"
