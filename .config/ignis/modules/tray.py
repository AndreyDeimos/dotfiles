from ignis.widgets import Widget
from ignis.services.system_tray import SystemTrayService, SystemTrayItem
import shared


class Tray(Widget.Box):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_spacing(10)
        shared.system_tray.connect("added", lambda x, item: self.append(TrayItem(item)))
        self.set_css_classes(
            shared.system_tray.bind("items", lambda x: ["bar"] if len(x) != 0 else [])
        )


class TrayItem(Widget.Button):
    def __init__(self, item: SystemTrayItem):
        super().__init__()
        if item.menu:
            self.menu = item.menu.copy()
            # self.menu.add_css_class("tray-menu")
        else:
            self.menu = None
        self.set_child(
            Widget.Box(child=[Widget.Icon(image=item.bind("icon")), self.menu])
        )
        item.connect("removed", lambda x: self.unparent())
        self.set_tooltip_text(item.bind("tooltip"))
        if self.menu:
            self.set_on_click(lambda x: self.menu.popup())
            self.set_on_right_click(lambda x: self.menu.popup())
