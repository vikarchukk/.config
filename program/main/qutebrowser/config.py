# qutebrowser config.py - переведено з autoconfig.yml

# Завантажити існуючі налаштування з autoconfig.yml (за бажанням)
config.load_autoconfig()

# Загальні налаштування
c.auto_save.session = True

# Завантаження та зовнішній вигляд
c.downloads.position = "bottom"
c.fonts.default_family = "monocraft"
c.fonts.default_size = "13pt"
c.zoom.default = "125%"

# Вкладки
c.tabs.favicons.show = "never"
c.tabs.indicator.width = 0
c.tabs.new_position.unrelated = "next"
c.tabs.padding = {"top": 1, "bottom": 1, "left": 3, "right": 0}
c.tabs.show = "always"
c.tabs.show_switching_delay = 3000
c.tabs.title.format = "{current_title}"

# Статус бар
c.statusbar.show = "always"
c.statusbar.widgets = ["keypress", "search_match", "url", "scroll", "progress"]

# Прокрутка
c.scrolling.bar = "never"

# Підказки (hints)
c.hints.border = "0px solid #000000"
c.hints.padding = {"top": 0, "bottom": 0, "left": 0, "right": 0}
c.hints.radius = 2
c.colors.hints.bg = "white"

# URL та пошук
c.url.default_page = "https://link.pikapod.net/bookmarks"
c.url.start_pages = ["https://link.pikapod.net/bookmarks"]
c.url.searchengines = {
    "DEFAULT": "https://www.google.com/search?q={}",
    "d": "https://translate.google.com/u/1/?sl=auto&tl=uk&text={}&op=translate",
    "y": "https://www.youtube.com/results?search_query={}"
}

# Налаштування вмісту за доменами
with config.pattern('https://whatismyaddress.net') as p:
    p.content.geolocation = True

with config.pattern('https://www.blocket.se') as p:
    p.content.geolocation = True

# JavaScript clipboard доступ
for site in [
    'https://chatgpt.com',
    'https://contacts.google.com',
    'https://developer.mozilla.org',
    'https://github.com',
    'https://translate.google.com',
    'https://web.telegram.org',
    'https://www.deepl.com',
    'https://www.emailnator.com',
    'https://www.google.com',
    'https://www.notion.so'
]:
    config.set('content.javascript.clipboard', 'access-paste', site)

# Медіа доступ
config.set('content.media.audio_capture', True, 'https://chatgpt.com')
config.set('content.media.audio_capture', True, 'https://grok.com')
config.set('content.media.video_capture', True, 'https://www.facebook.com')

# Сповіщення
config.set('content.notifications.enabled', True, 'https://calendar.google.com')
config.set('content.notifications.enabled', True, 'https://web.telegram.org')

# Обробники протоколів
config.set('content.register_protocol_handler', True, 'https://calendar.google.com?cid=%25s')
config.set('content.register_protocol_handler', True, 'https://mail.google.com?extsrc=mailto&url=%25s')

# Прив'язки клавіш - очищуємо деякі стандартні
config.unbind('<Ctrl+v>', mode='normal')
config.unbind('v', mode='normal')

# Навігація vim-стиль
config.bind('H', 'forward')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
config.bind('L', 'back')

# Швидкий доступ до сайтів (великі літери - нова вкладка)
config.bind('Zb', 'open -t https://vault.bitwarden.com/#/login')
config.bind('Zc', 'open -t https://chatgpt.com/')
config.bind('Zd', 'open -t https://translate.google.com/u/1/?sl=auto&tl=uk&op=translate')
config.bind('Zf', 'open -t https://finance.pikapod.net')
config.bind('Zg', 'open -t https://github.com/vikarchukk')
config.bind('Zl', 'open -t https://claude.ai/new')
config.bind('Zm', 'open -t https://gemini.google.com/app')
config.bind('Zn', 'open -t https://www.notion.so')
config.bind('Zs', 'open -t https://chat.deepseek.com/')
config.bind('Zt', 'open -t https://web.telegram.org/a/')
config.bind('Zw', 'open -t https://www.codewars.com')
config.bind('Zy', 'open -t https://www.youtube.com/')

# Швидкий доступ до сайтів (малі літери - поточна вкладка)
config.bind('zb', 'open https://vault.bitwarden.com/#/login')
config.bind('zc', 'open https://chatgpt.com/')
config.bind('zd', 'open https://translate.google.com/u/1/?sl=auto&tl=uk&op=translate')
config.bind('zf', 'open https://finance.pikapod.net')
config.bind('zg', 'open https://github.com/vikarchukk')
config.bind('zl', 'open https://claude.ai/new')
config.bind('zm', 'open https://gemini.google.com/app')
config.bind('zn', 'open https://www.notion.so')
config.bind('zs', 'open https://chat.deepseek.com/')
config.bind('zt', 'open https://web.telegram.org/a/')
config.bind('zw', 'open https://www.codewars.com')
config.bind('zy', 'open https://www.youtube.com/')

# Спеціальні команди
config.bind('sg', 'greasemonkey-reload')
config.bind('ss', 'config-cycle statusbar.show always in-mode')
config.bind('st', 'config-cycle tabs.show always switching')
config.bind('vv', 'open https://translate.google.com/translate?sl=auto&tl=uk&u={url}')

# cd ~/.local/share/qutebrowser/greasemonkey
#  wget https://update.greasyfork.org/scripts/9165/Auto%20Close%20YouTube%20Ads.user.js
#  wget https://update.greasyfork.org/scripts/436115/Return%20YouTube%20Dislike.user.js
#  wget https://update.greasyfork.org/scripts/394512/YouTube%20ProgressBar%20Preserver.user.js
#  wget https://gist.githubusercontent.com/vikarchukk/bc4b302100c13bf8c88f106131f2b495/raw/1077d661c26808e1aea4a8a6315aaa6a020d97cf/monocraft-font.user.js
# shift + ;
#  :greasemonkey-reload # in qutebrowser

# всі що не юзаю компінації заглушити

# qutebrowser
# ├─ команда + число + рух
# ├─ normal / escape
# |  ├─ переміщення
# |  |  ├─ по сторінці
# │  │  │  ├─ k - верх / j - вниз / h - вліво / l - вправо
# │  │  │  ├─ gg - скролити на початок / G - скролити на кінець
# │  │  │  └─ L - назад по історії / H - вперед по історії
# │  │  └─ по вкладкам
# │  │     ├─ J - назад / K - вперед
# │  │     ├─ o - нова / d - закрити
# │  │     ├─ z - відкрити котрись сайт
# │  │     ├─ v - перекласти сторінку
# │  │     └─ u - відкрити останю закриту вкладку
# │  ├─ + - збільшити зум / - - зменшити зум / = - класичний зум
# │  └─ r - перезагрузити сторінку
# ├─ follow / f - натиснути на щось
# ├─ insert / i - написати щось
# ├─ search / / - знайти щось
# │  └─ n - вперед / N - назад
# └─ command / :
#    ├─ devtools - відкрити вікно інструментів
#    ├─ download - зробити котрісь маніпуляції зі скачуванням
#    ├─ yank - скопіювати url
#    ├─ tab-only - закрити всі вкладки крім активної
#    ├─ unbind - видалити комбінацію клавіш
#    ├─ bind - додати комбінацію клавіш або переглянути що робить комбінація
#    ├─ fullscreen - робить вікно на весь екран
#    ├─ help - переглянути документацію
#    └─ qw - вийти з vieb (або ZZ)
