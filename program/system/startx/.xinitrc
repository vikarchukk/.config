xrandr --output eDP-1 --mode 1680x1050 # зміна розшириння екрану

# переназначиння клавіш
setxkbmap -option caps:escape
setxkbmap -option lv3:rwin_switch
setxkbmap -option lv5:ralt_switch

# xset s off # виключити затемнення екрану після 10хв бездіяльності
# xset -dpms # виключити вимикання екрану після бездіяльності
# xrdb ~/.Xresources # активація налаштування розміру курсору
# bash ~/battery-alert & # сповіщення про низький рівень зарядки
# mechsim -V 100 & # звук при натискання клавіатури
# slstatus & # запуск програми для відображиння даних про пк
# exec dwm # віконий менеджер
