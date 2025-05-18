import catppuccin

config.load_autoconfig()

config.bind(",p", "spawn --userscript qute-pass --dmenu-invocation dmenu")
config.bind(
    ",P", "spawn --userscript qute-pass --dmenu-invocation dmenu --password-only"
)
config.bind(
    "<Escape>", "mode-leave ;; jseval -q document.activeElement.blur()", mode="insert"
)
c.editor.command = [
    "kitty",
    "nvim",
    "{file}",
    "-c",
    "normal {line}G{column0}l",
]
c.scrolling.smooth = True
c.content.pdfjs = True
