echo хуй
# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=100000
SAVEHIST=100000
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/deimos/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word
bindkey  "^[[H"   beginning-of-line
bindkey  "^[[F"   end-of-line
bindkey  "^[[3~"  delete-char
bindkey "^H" backward-kill-word
alias help="echo 'I need somebody'"
alias cura="env QT_QPA_PLATFORM=wayland flatpak run com.ultimaker.cura -platformtheme gtk3"
alias find="find 2> /dev/null"
alias cd="z"

of() {
    loffice "$(find . -type f -iname "$1" | fzf)"
}
function y() {
	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
	yazi "$@" --cwd-file="$tmp"
	if cwd="$(command cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
		builtin cd -- "$cwd"
	fi
	rm -f -- "$tmp"
}
eval "$(zoxide init zsh)"
export PS1='%~> '
# print "⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢄⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⡠⠠⠠⡀⡀⡀⠀
# ⠀⠀⠀⠀⠀⠀⠠⠐⠈⠄⠌⠔⡨⠨⠨⡨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⠨⡨⢊⠔⡡⠡⢂⢐⠀⠂
# ⠀⠀⠀⢀⠠⠈⠠⠈⠌⠠⠡⡑⠄⢕⠡⢂⠅⢅⠅⠅⠅⠅⢅⠅⠅⢅⠅⠅⠅⠅⠅⠅⠅⠅⠅⠅⠅⠅⠅⠅⠅⠅⠅⠅⠅⠅⠅⢅⠕⡡⢊⠢⡑⢌⠌⡂⡂⠌⡈
# ⠀⠐⠈⠀⠠⠈⠄⠡⠈⠄⢕⠨⡨⢂⠅⠕⡌⡢⠡⡑⡡⠡⡑⠌⢌⢂⠪⠨⡨⠨⠨⡨⠨⠨⡨⠨⠨⡊⠌⠌⠌⠌⠌⠌⠌⠌⢌⢂⠪⡐⢅⠕⢌⠢⡑⡐⡐⡁⠢
# ⠀⠐⢈⠀⠂⡁⠄⠡⠈⠨⡂⢕⠨⠢⡑⢕⠌⡢⢑⢐⠌⡂⡪⠨⡂⡢⠡⡑⠌⢌⠪⡐⠅⢕⠨⠨⡊⠄⢅⠅⠅⠅⠅⠅⢅⠅⢕⠠⡑⢌⠢⡑⢅⠪⡐⢌⠢⠨⠨
# ⠀⠁⡀⠄⢁⠀⠂⠂⠁⢅⠪⡐⢅⢣⢑⠅⢕⠨⡂⢕⠨⡂⡪⠨⡂⡪⠨⡂⢕⠡⡊⢔⠡⡑⠌⢌⠢⠡⡑⠌⢌⠌⡊⢌⢂⠪⡐⡱⢨⠢⡑⢌⠢⡑⢌⠢⠡⠡⢑
# ⠀⢀⠀⠀⢂⠀⡁⠄⠁⡢⡑⡌⢎⠢⡑⢌⠢⡑⢌⠢⡑⢌⠢⡑⢌⠢⡑⢌⠢⡑⢌⠢⡑⢌⢌⠢⡑⢅⠪⠨⡂⡪⢐⠡⡂⢕⢐⢌⠢⡑⢌⠢⡑⢌⠢⡑⠡⢑⠐
# ⠀⠄⠀⠁⡀⠄⠠⠀⡂⡢⠣⡊⡢⢑⠌⡢⢑⠨⡂⠕⢌⠢⡑⢌⠢⡑⢌⠢⡑⢌⠢⡑⢌⠢⡢⡑⢌⠢⡡⢑⢐⠌⡢⢑⠌⡢⡑⢔⢑⢌⠢⡑⢌⠢⡑⠌⢌⢐⠨
# ⠠⠀⠂⠁⠀⠐⢈⠠⡘⢌⠪⡐⢌⠢⡑⢌⢂⠅⡊⢌⠢⡑⢌⠢⡑⢌⠢⡑⢌⠢⡑⢌⠢⡑⢌⠪⡢⡱⡨⠢⡑⢌⠢⡑⢌⠢⡊⡢⢱⢐⠱⡨⠢⡑⢜⠈⠄⡂⠌
# ⠌⠐⡀⠄⠁⠌⠠⠐⢌⠢⡑⢌⠢⢑⠨⠐⠀⠂⢌⠢⡑⠨⠢⡑⢌⠢⡑⢌⠢⡑⢌⠢⡑⢌⠢⡑⢌⢆⢣⠱⡨⢢⢑⢌⠢⡑⢌⠪⡢⡑⡑⢌⠪⡸⠐⡈⡐⠠⢁
# ⠠⠁⠄⠂⠁⠄⠡⠈⠐⠐⠈⡀⠂⢀⠠⢀⠡⠡⡑⡐⢌⢂⠁⢊⠢⡑⢌⠢⡑⢌⠢⡑⢌⠢⡑⢌⠢⡑⢜⢌⠪⡢⢱⢘⢌⢎⠜⡌⡢⡑⢌⠢⡱⠨⢐⢀⠂⠅⡂
# ⠌⠐⡈⠠⠁⠄⠂⡀⠁⢀⠁⡀⡐⡀⡂⡂⡪⠨⡂⡪⢐⢐⠅⢄⠐⢈⠐⡁⠪⠐⠡⠊⡐⠅⢊⠢⡑⢌⠢⠪⡘⡌⢎⢢⠣⡊⢎⠢⡑⢌⠢⡑⠅⠌⠄⡂⠌⠀⠄
# ⠄⠡⠠⢈⠐⡀⠡⠀⢂⠀⡂⡢⢂⠪⡐⢌⠢⡑⡐⢌⠢⡑⢌⢂⠪⡀⠄⠀⠂⠁⡀⠂⢀⠐⠀⡐⠀⠅⠪⡨⢂⢇⢣⢱⢑⠕⢅⠕⡨⠢⡑⠡⠨⠠⠁⢀⠄⠡⢁
# ⠄⡁⢐⠠⠐⠀⠂⡁⠄⠐⠀⠌⠢⡑⡨⢐⠡⢂⠪⡐⢅⠪⡐⡐⢅⠪⠨⡊⠔⡁⠄⢄⢀⠀⠂⠀⡈⠀⠅⠌⡢⡑⡕⡕⢅⠣⡑⢌⠢⡑⠈⠄⠁⠠⢈⠄⠌⠨⢀
# ⠠⠐⢀⠐⡀⢁⠁⠠⠐⠈⠀⠂⠁⠐⠨⠂⠌⠐⠨⢐⠐⢅⢂⠪⠠⠡⡑⠌⢌⠢⢑⢐⠔⠡⠡⡂⠠⠈⡀⢁⠢⡱⡸⡸⡐⢅⠪⠐⢁⠠⠁⠠⠈⠌⡀⡂⠡⢁⢂
# ⠀⠌⠀⠄⠐⡀⢈⠀⠂⢈⠀⡁⠈⡀⠂⡰⡐⠠⠈⠀⠡⡑⡐⡡⠡⠑⢄⢑⢐⠨⢐⢐⠨⠨⢊⠔⠡⡡⢂⢐⠨⢢⠣⡪⢐⠁⢀⠈⠀⢀⠠⠈⠄⠡⠐⠠⢁⢂⠐
# ⠁⠄⠁⠄⢁⠠⠀⠄⠁⡀⠄⠀⠄⠀⢰⢱⠑⠀⠀⠢⠀⠪⡐⠄⢅⢑⠐⢀⠠⡀⠀⠀⠈⠌⡐⠌⢌⢂⢂⠢⠨⡪⡊⡢⠡⢐⠔⡁⠁⠄⠐⢈⠠⠁⠌⡐⢀⢂⠐
# ⠀⠂⠁⠐⢀⠠⠐⠀⠄⠀⡀⠄⠐⢀⠌⠪⡂⠂⠄⠂⠀⢕⢐⠡⢂⠂⡐⡅⡇⠐⠀⡂⠀⠀⡀⠌⡐⡐⠄⢅⢣⠱⠡⢐⠨⢀⠂⠀⠐⠀⡁⠄⠐⢈⠠⠐⠠⠐⢈
# ⠀⢁⠈⠠⠀⡀⠠⠀⡀⠂⠀⠀⠀⢐⠅⠅⠄⠅⠂⠡⡘⢔⠠⡑⡐⠠⢘⢜⠀⠄⠂⠑⠀⠁⡄⡀⠢⡢⡑⡌⡎⡊⠨⢐⠈⠀⠀⠀⠁⠠⠀⠠⠁⠠⠐⠈⠠⢈⠠
# ⠄⠠⠐⠀⠄⠠⠐⠀⠀⠀⠀⠀⠀⠐⡅⢕⠡⡊⢌⢪⠨⢂⠅⠢⠨⠐⡈⠜⢔⢀⠂⠄⠂⠜⡐⢄⢇⢇⢇⢇⠣⠨⠈⠀⠀⠀⠀⠀⠀⠀⠀⠂⢈⠀⠂⢁⠈⡀⠄
# ⠠⠀⡀⠂⠀⠈⠐⢀⠂⡀⢂⠈⠄⢁⠪⡐⢅⠪⡸⢐⠅⠢⠨⠨⠨⢐⠠⠨⢀⢂⠐⠄⠅⢅⠢⡱⡸⡸⡸⠘⠀⠀⠄⠂⠈⠀⠈⠀⠀⠂⠀⠀⠀⠀⠈⡀⠄⠠⠀
# ⠀⠂⠀⠀⠀⠠⠐⠀⠀⠂⠠⠈⠈⠀⢌⠢⡑⢕⠌⡢⠨⠨⠨⠨⡨⢂⠌⡂⡂⡢⠨⡂⠕⢌⢊⢆⠣⡱⢁⠐⠈⢀⠠⠀⠐⠈⠀⠈⠀⡀⠐⠀⠀⠂⠀⠀⠀⠂⡈
# ⠀⠀⠀⡀⠄⠀⢀⠀⢀⠐⠀⡂⠐⡀⡢⡑⢕⢅⠪⡐⢅⢕⠡⡑⠄⢕⠨⡐⡐⠌⡂⡊⠌⡂⡢⢂⠕⢌⠠⠀⠅⠂⡀⠐⠀⠂⠈⡀⠄⠀⡀⠄⠂⠀⢀⠠⠀⠀⠀
# ⠂⠁⠀⠀⠀⢀⠀⠠⠀⠀⢐⠀⠅⡰⡘⡌⢆⢪⢪⢸⢰⢡⢃⠎⡌⡂⡊⡐⠌⡂⠢⠨⡂⠢⡊⡢⡑⠡⡂⠌⠠⠁⠄⡁⠂⢁⠐⠸⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⡀⠠⠐⠈⠀⠀⠠⠐⠈⠀⠐⡐⡌⡎⡜⡜⡜⡜⡜⡜⡜⢔⢱⠨⢂⢂⠂⢅⠊⢌⢂⠪⡨⢢⠑⠀⠐⠠⠁⠅⠡⢁⠐⡐⢀⠠⠁⡐⠀⢀⠀⠁⠀⠁⠀⡀⠈⠀
# ⠄⠀⠀⠀⢀⠀⠂⠀⠄⠠⠈⡰⡘⡜⡜⡜⡜⡜⡜⡜⡜⠜⢌⠢⢑⠐⢄⠑⠄⢕⢐⠔⡑⡌⠎⠀⠐⠀⠀⠂⠁⢁⠐⡀⠂⠄⠂⡁⡐⠠⠀⠄⠈⠀⠐⠀⠀⠀⠀
# ⠀⠀⠂⠁⠀⡀⠄⠁⠠⠀⠈⡐⢅⠣⡣⡣⡣⡣⠣⡃⡪⡨⡢⡑⡅⢕⠡⠨⡈⡂⡢⡑⢜⠌⠂⠁⠀⠀⠀⢀⠀⠀⢀⠀⠂⠐⠀⠄⠐⢈⠐⠐⠈⡀⠄⠀⠐⠈⠀
# ⠀⠂⠀⠐⠀⢀⠠⠐⠀⡈⠀⠄⠡⢊⢐⢑⠌⠌⡊⢆⠣⡣⠣⡣⡣⡣⡑⢅⠢⠨⡂⢎⠪⠀⠀⠀⢀⠠⠈⠀⠀⠀⠀⠀⠀⠐⠀⠐⠈⠀⡀⠁⠂⡀⠀⠂⠠⠀⠀
# ⠀⠀⠈⠀⠈⠀⢀⠀⠂⢀⠀⠄⠠⠀⢐⢐⠈⠐⢐⠠⢑⢌⠪⡢⡂⡑⢕⠡⡈⡪⢨⠂⠂⠀⠐⠈⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⡀⠐⠀⠀⠈⠀⡀⠂⠀⡀⠐⠈
# ⠀⠀⠁⠈⠀⠁⡀⠀⠁⠀⠀⡀⠄⠂⢐⠐⠈⡀⠄⠨⠐⠠⢑⢐⠑⢌⠂⠅⡂⡊⡂⠂⠄⠡⠐⠀⢀⠀⠄⠂⠈⠀⠀⠀⢀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀"
#
# print "
# ███╗░░██╗░█████╗░  ██████╗░░█████╗░░██████╗██╗░░██╗░█████╗░
# ████╗░██║██╔══██╗  ██╔══██╗██╔══██╗██╔════╝██║░░██║██╔══██╗
# ██╔██╗██║██║░░██║  ██████╦╝███████║╚█████╗░███████║╚═╝███╔╝
# ██║╚████║██║░░██║  ██╔══██╗██╔══██║░╚═══██╗██╔══██║░░░╚══╝░
# ██║░╚███║╚█████╔╝  ██████╦╝██║░░██║██████╔╝██║░░██║░░░██╗░░
# ╚═╝░░╚══╝░╚════╝░  ╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░" 
clear
#echo хуй
