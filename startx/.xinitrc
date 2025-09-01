xrandr --output eDP-1 --mode 1680x1050 # зміна розшириння екрану

setxkbmap -option caps:escape # переназначиння клавіш
setxkbmap -option lv3:rwin_switch
setxkbmap -option lv5:ralt_switch

exec dwm # віконий менеджер 
