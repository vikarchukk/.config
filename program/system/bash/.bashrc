#
# ~/.bashrc
#

# If not running interactively, don't do anything
# [[ $- != *i* ]] && return

# модифікація команд
alias ls="ls --color=auto -a"
alias v="vim"

# рядок перед курсором
off="\[\033[0m\]"
purple="\[\033[1;35m\]"
green="\[\033[1;32m\]"
red="\[\033[1;31m\]"
export PS1="${green}[${off}${purple}\w${off}${green}]${off}${red}\$${off} "

# заголовок вікна
export PROMPT_COMMAND='printf "\033]0;${PWD/#$HOME/~}\007"'
