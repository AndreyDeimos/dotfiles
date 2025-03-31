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
