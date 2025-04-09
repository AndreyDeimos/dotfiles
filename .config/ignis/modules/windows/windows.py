from ignis.widgets import Widget


class WindowManager:
    __gtype_name__ = "WindowManager"

    def __init__(self):
        self.window_list = []

    def close_all_windows(self, ignore=None):
        for i in self.window_list:
            if ignore:
                if i.namespace == ignore:
                    continue
            if i.visible:
                i.toggle()


class Window(Widget.RevealerWindow):
    __gtype_name__ = "Window"

    def __init__(self, window_manager, content, window_name, box_args, window_args):
        self.window_manager = window_manager
        self.window_manager.window_list.append(self)

        self._revealer = Widget.Revealer(child=content)

        self._box = Widget.Box(child=[self._revealer], **box_args)

        self._overlay = Widget.Overlay(
            child=Widget.Button(
                vexpand=True,
                hexpand=True,
                can_focus=False,
                on_click=lambda x: self.toggle(),  # e.g., app.close_window("my-window")
            ),
            overlays=[self._box],
        )

        super().__init__(
            namespace=window_name,
            anchor=["left", "right", "top", "bottom"],
            child=self._overlay,
            revealer=self._revealer,
            popup=True,
            visible=False,
            **window_args,
        )

    def toggle(self):
        self.window_manager.close_all_windows(ignore=self.namespace)
        self.set_visible(not self.visible)
