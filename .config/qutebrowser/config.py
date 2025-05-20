import catppuccin

config.load_autoconfig()

config.bind(",p", "spawn --userscript qute-pass --dmenu-invocation dmenu")
config.bind(
    ",P", "spawn --userscript qute-pass --dmenu-invocation dmenu --password-only"
)
config.bind(
    "<Escape>", "mode-leave ;; jseval -q document.activeElement.blur()", mode="insert"
)
config.bind("aq", "quickmark-add {url} {title}")
config.bind("<Ctrl-D>", "cmd-repeat 10 scroll down")
config.bind("<Ctrl-U>", "cmd-repeat 10 scroll up")
c.editor.command = [
    "kitty",
    "nvim",
    "{file}",
    "-c",
    "normal {line}G{column0}l",
]
c.scrolling.smooth = True
c.content.pdfjs = True
catppuccin.setup(c, "macchiato")
