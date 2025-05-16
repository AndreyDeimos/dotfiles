import catppuccin

config.load_autoconfig()

config.bind(",p", "spawn --userscript qute-pass --dmenu-invocation dmenu")
config.bind(
    ",P", "spawn --userscript qute-pass --dmenu-invocation dmenu --password-only"
)
c.editor.command = [
    "kitty",
    "nvim",
    "{file}",
    "-c",
    "normal {line}G{column0}l",
]
