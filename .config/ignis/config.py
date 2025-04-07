# fmt: off

from modules import WindowManager
from ignis.widgets import Widget
from ignis.utils import Utils
from ignis.app import IgnisApp
from ignis.services.audio import AudioService
from ignis.services.backlight import BacklightService
from ignis.services.upower import UPowerService
from ignis.services.network import NetworkService
from ignis.services.hyprland import HyprlandService
from ignis.services.system_tray import SystemTrayService, SystemTrayItem
from ignis.services.mpris import MprisService, MprisPlayer
import datetime
import subprocess


hyprland = HyprlandService.get_default()
system_tray = SystemTrayService.get_default()
mpris_service = MprisService.get_default() 
audio = AudioService.get_default()
window_manager = WindowManager()
backlight = BacklightService.get_default()

class Mpris(Widget.Label):
    def __init__(self, **kwargs):
        self.mpris = mpris_service
        super().__init__(**kwargs)
        self.set_label(self.mpris.bind("players", lambda x: "" if len(x) == 0 else x[-1].title))

    class Player:
        def __init__(self, player: MprisPlayer):
            MprisPlayer.connect("closed", lambda x: self.unparent())

        
class Tray(Widget.Box):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_spacing(10)
        system_tray.connect("added", lambda x, item: self.append(self.TrayItem(item)))
    class TrayItem(Widget.Button):
        def __init__(self, item: SystemTrayItem):
            super().__init__()
            if item.menu:
                self.menu = item.menu.copy()
                self.menu.add_css_class("tray-menu")
            else:
                self.menu = None 
            self.set_child(Widget.Box(child=[
                Widget.Icon(image=item.bind("icon")), self.menu
                ]))
            item.connect("removed", lambda x: self.unparent())
            self.set_tooltip_text(item.bind("tooltip"))
            if self.menu:
                self.set_on_click(lambda x: self.menu.popup())
                self.set_on_right_click(lambda x: self.menu.popup())
    
class Workspaces(Widget.Box):
    def __init__(self):
        super().__init__()
        self.set_spacing(5)
        self.set_child(
            hyprland.bind_many(
                ["workspaces", "active_workspace"],
                transform=lambda workspaces, *_: [
                    self.workspace_button(i) for i in workspaces
                ],
            )
        )

    class workspace_button(Widget.Button):
        def __init__(self, workspace):
            super().__init__()
            self.id = workspace.id
            self.set_child(Widget.Label(label=str(self.id)))
            self.set_on_click(lambda x: hyprland.switch_to_workspace(self.id))
            if workspace.id == hyprland.active_workspace.id:
                self.add_css_class("active")

class Clock(Widget.Button):
    def __init__(self):
        super().__init__()
        self.labellle = Widget.Label()
        self.set_child(self.labellle)
        Utils.Poll(1000, lambda x: self.update())

    def update(self):
        text = datetime.datetime.now().strftime("%H : %M")
        self.labellle.set_label(text)

class Network(Widget.Box):
    def __init__(self):
        super().__init__()
        self.network = NetworkService.get_default()
        self.icon = Widget.Icon()
        self.label = Widget.Label()
        self.update()
        Utils.Poll(1000, lambda x: self.update())
        self.set_spacing(5)
        self.set_child([self.icon])
        
    def update(self):
        if self.network.ethernet.is_connected:
            self.icon.set_image(self.network.ethernet.bind("icon_name"))
        else:
            self.icon.set_image(self.network.wifi.bind("icon_name"))

        if self.network.wifi.is_connected and not self.network.ethernet.is_connected:
            self.label.set_label(self.network.wifi.devices[0].ap.bind("ssid"))
            self.set_child([self.icon, self.label])
        else:
            self.set_child([self.icon])


class Volume(Widget.Box):
    def __init__(self):
        super().__init__()
        self.window = self.Window()
        window_manager.window_list.append(self.window)
        self.icon = Widget.Button(
                child=Widget.Icon(image=audio.speaker.bind("icon-name")),
                on_click=lambda x: self.window.toggle()
                # on_click=lambda x: self.window.toggle()
                )

        self.revealed = False

        # self.hiding = Widget.Revealer(
        #         child=self.scale,
        #         transition_type='slide_right',
        #         transition_duration=100,
        #         reveal_child=self.revealed
        #         )
        self.set_child([self.icon])
        self.set_spacing(10)
        
    def hide(self):
        self.revealed = not self.revealed
        # self.hiding.set_reveal_child(self.revealed)
        if self.revealed:
            self.set_child([self.icon, self.scale])
        else:
            self.set_child([self.icon])

    class Window(Widget.RevealerWindow):
        def __init__(self):
            self.scale = Widget.Scale(
                step=10,
                value=audio.speaker.bind("volume"),
                on_change=lambda x: audio.speaker.set_volume(x.value),
                css_classes = ["slider"],
                width_request = 90,
            )           
            self.spinbutton = Widget.SpinButton(
                step=10,
                value=audio.speaker.bind("volume"),
                on_change=lambda x, value: audio.speaker.set_volume(value),
                min=0,
                max=300
            )
            self.button = Widget.Button(
                child=Widget.Icon(
                    image=audio.speaker.bind("icon-name")
                ),
                on_click=lambda x: audio.speaker.set_is_muted(not audio.speaker.is_muted) 
            )
            self.revealer_shit = Widget.Revealer(
                    child=Widget.Box(child=[
                        self.button,
                        self.scale,
                        self.spinbutton
                    ],
                    spacing=10
                )
            )
            self.box_shit = Widget.Box(child=[self.revealer_shit])
            self.box_shit.set_css_classes(["bar"])
            super().__init__(
                visible=False,
                popup=True,
                layer="top",
                namespace="audio-revealer-window",
                child=self.box_shit,
                revealer=self.revealer_shit,
                anchor=["top", "left"],
                margin_left=20,
                margin_top=10
            )
        def toggle(self):
            window_manager.close_all_windows(ignore=self.namespace)
            self.set_visible(not self.visible)


class Backlight(Widget.Box):
    def __init__(self):
        super().__init__()
        self.window = self.Window()
        window_manager.window_list.append(self.window)
        self.icon = Widget.Button(
                child=Widget.Icon(image="weather-clear-symbolic"),
                on_click=lambda x: self.window.toggle()
                )


        self.revealed = False

        # self.hiding = Widget.Revealer(
        #         child=self.scale,
        #         transition_type='slide_right',
        #         transition_duration=100,
        #         reveal_child=self.revealed
        #         )
        self.set_child([self.icon])
        self.set_spacing(10)
        
    class Window(Widget.RevealerWindow):
        def __init__(self):
            self.scale = Widget.Scale(
                step=10,
                max=backlight.max_brightness,
                value=backlight.bind("brightness"),
                on_change=lambda x: backlight.set_brightness(x.value),
                css_classes = ["slider"],
                width_request = 90,
            )         
            self.icon = Widget.Icon(image="weather-clear-symbolic")

            self.revealer_shit = Widget.Revealer(
                    child=Widget.Box(child=[
                        self.icon,
                        self.scale
                    ],
                    spacing=10
                )
            )
            self.box_shit = Widget.Box(child=[self.revealer_shit])
            self.box_shit.set_css_classes(["bar"])
            super().__init__(
                visible=False,
                popup=True,
                layer="top",
                namespace="backlight-revealer-window",
                child=self.box_shit,
                revealer=self.revealer_shit,
                anchor=["top", "left"],
                margin_left=20,
                margin_top=10
            )
        def toggle(self):
            window_manager.close_all_windows(ignore=self.namespace)
            self.set_visible(not self.visible)

class Power(Widget.Box):
    def __init__(self):
        super().__init__()
        self.power = UPowerService.get_default()
        self.icon = Widget.Icon(image=self.power.devices[0].bind("icon_name"))
        self.label = Widget.Label(
                label=self.power.devices[0].bind("percent", lambda value: f"{str(int(value))}%"),
                )
        
        self.set_spacing(5)
        self.set_child([self.label, self.icon])

class buttons:
    @staticmethod
    def poweroff_button(button):
        button.set_child(Widget.Icon(image="system-shutdown-symbolic"))
        button.set_on_click(lambda button: subprocess.run(["systemctl", "poweroff"]))

    @staticmethod
    def lock_button(button):
        button.set_child(Widget.Icon(image="system-lock-screen-symbolic"))
        button.set_on_click(lambda button: subprocess.run(["hyprlock"]))

class Bar:
    def __init__(self):
        self.clock = Clock()
        self.poweroff = Widget.Button(setup=lambda self: buttons.poweroff_button(self))
        self.lock = Widget.Button(setup=lambda self: buttons.lock_button(self))
        self.volume = Volume()
        self.backlight = Backlight()
        self.power = Power()
        self.network = Network()
        self.workspaces = Workspaces()
        self.tray = Tray()
        self.mpris = Mpris()

        
        self.workspaces.add_css_class("bar")
        self.tray.set_css_classes(system_tray.bind("items", lambda x: ["bar"] if len(x) != 0 else []))
        self.mpris.set_css_classes(mpris_service.bind("players", lambda x: [] if len(x) == 0 else ["bar"]))

        self.start = Widget.Box(
            child=[
                self.workspaces,
                Widget.Box(child=[self.network, self.backlight, self.volume], css_classes=["bar"], spacing = 10),
                self.tray
            ],
            spacing = 10
        )

        self.center = Widget.Box(
            child=[
                # self.mpris
            ],
            spacing = 10
        )


        self.end = Widget.Box(
            spacing=10,
            css_classes=["bar"],
            child=[
                self.power,
                self.clock,
                self.lock,
                self.poweroff,
            ]
        )

        self.child = Widget.CenterBox(
            width_request=1560,
            start_widget=self.start,
            center_widget=self.center,
            end_widget=self.end
        )

    def init(self, monitor):
        return Widget.Window(
            namespace=f"window-{monitor}",
            monitor=monitor,
            child=self.child,
            margin_top=16,
            anchor=["top"],
            exclusivity="exclusive",
        )


app = IgnisApp.get_default()

app.apply_css("/home/deimos/.config/ignis/style.scss")


bar = Bar()

bar.init(0)

# revealery = Widget.Revealer(
#     child=Widget.Label(label="smth", css_classes=["bar"])
# )
#
# boxy = Widget.Box(
#     child=[revealery],
#     valign="center",
#     halign="center",
# )
#
# smth = Widget.RevealerWindow(
#     namespace="my-window",
#     anchor=["left", "right", "top", "bottom"],  # to make a window fullscreen
#     child=Widget.Overlay(
#         child=Widget.Button(
#             vexpand=True,
#             hexpand=True,
#             can_focus=False,
#             on_click=lambda x: app.close_window("my-window"), # e.g., app.close_window("my-window")
#         ),
#         overlays=[boxy],
#     ),
#     revealer=revealery
# )

# window_manager.window_list.append(smth)
# toggle not made for windows that are hust variables

# Widget.RegularWindow(
#         namespace="lol",
#         child=Widget.Label(label="what"),
#         resizable=False,
#         default_width = 900,
#         default_height = 600
#         )
#while True:
# print(mpris_service.players)
