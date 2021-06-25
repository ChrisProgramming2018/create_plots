# Eternal bash history.
# ---------------------
# Undocumented feature which sets the size to "unlimited".
# http://stackoverflow.com/questions/9457233/unlimited-bash-history
export HISTFILESIZE=
export HISTSIZE=
export HISTTIMEFORMAT="[%F %T] "
# Change the file location because certain bash sessions truncate .bash_history file upon close.
# http://superuser.com/questions/575479/bash-history-truncated-to-500-lines-on-each-login
export HISTFILE=~/.bash_eternal_history
# Force prompt to write history after every command.
# http://superuser.com/questions/20900/bash-history-loss
PROMPT_COMMAND="history -a; $PROMPT_COMMAND"

export LD_PRELOAD=


export PYTHONPATH=$PYTHONPATH:/home/programmer/hiwi2/BMW/layer
export PYTHONPATH=$PYTHONPATH:/home/programmer/hiwi2/BMW/layer/app
export PYTHONPATH=$PYTHONPATH:/home/programmer/hiwi2/BMW/layer/app/application/adp/planning/trajectory/lib/python/test/longitudinal/acc_tests_img.binary.runfiles/ddad/

alias sbmw="cd /home/programmer/hiwi2/BMW//layer/app/application/adp/planning/trajectory/lib/python/test/longitudinal/acc_tests_img.binary.runfiles/ddad/application/adp/planning/trajectory/lib/python/test/longitudinal"




alias rl="source /home/programmer/miniconda3/bin/activate rl"
alias lab="source /home/programmer/miniconda3/bin/activate lab"
alias iql="source /home/programmer/miniconda3/bin/activate iql"
alias tf="source /home/programmer/miniconda3/bin/activate tf"
alias go="source /home/programmer/miniconda3/bin/activate go"
alias sp="source /home/programmer/miniconda3/bin/activate space"
alias md="source /home/programmer/miniconda3/bin/activate middlevel"

alias tb="tensorboard --logdir=runs"

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia-418
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/programmer/.mujoco/mujoco200/bin

parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

PS1="\u@\h \[\033[32m\]\w - \$(parse_git_branch)\[\033[00m\] $ "

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/programmer/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/programmer/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/programmer/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/programmer/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
