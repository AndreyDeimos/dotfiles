from ignis.widgets import Widget
from ignis.utils import Utils
from datetime import datetime
from modules import windows
import shared


class Clock(Widget.Button):
    def __init__(self):
        super().__init__()
        self.labellle = Widget.Label()
        Utils.Poll(1000, lambda x: self.update())
        self.calendar = Widget.Calendar(css_classes=["bar"])
        self.window = windows.Window(
            shared.window_manager,
            self.calendar,
            "calendar",
            {
                "valign": "start",
                "halign": "end",
            },
            {"margin_right": 20, "margin_top": 10},
        )
        self.set_child(self.labellle)
        self.set_on_click(lambda x: self.window.toggle())

    def update(self):
        text = datetime.now().strftime("%H : %M")
        self.labellle.set_label(text)
