from windows import Window, WindowManager
from ignis.widgets import Widget
from ignis.services.bluetooth import BluetoothService

bluetooth_service = BluetoothService.get_default()


class Bluetooth(Widget.Button):
    def __init__(self, window_manager: WindowManager):
        self._disabled_icon = "bluetooth-disabled-symbolic"
        self._icon = Widget.Icon(image=self._disabled_icon)
        self._window_content = Widget.Box(
            vertical=True,
            child=[
                Widget.CenterBox(
                    start=Widget.Label(label="start test"),
                    end=Widget.Label(label="end test"),
                ),
                Widget.Box(
                    vertical=True,
                    child=[
                        Widget.Label(label="some test"),
                        Widget.Label(label="funny wrapped text"),
                    ],
                ),
            ],
        )
        self._window = Window(
            window_manager,
            self._window_content,
            {"valign": "start", "halign": "start"},
            {"margin_left": 20, "margin_top": 10},
        )
        super().__init__(self)
