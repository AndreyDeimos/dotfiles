from ignis.services.fetch import FetchService
from ignis.widgets import Widget
from ignis.utils import Utils
import modules.windows

fetch_service = FetchService.get_default()


def separator_maker():
    return Widget.Label(label="|")


def Stats(monitor):
    logo = Widget.Icon(image=fetch_service.bind("os_logo"))
    cpu = Widget.Label(
        label=fetch_service.bind("cpu_temp", lambda x: f"  : {round(x)}")
    )
    Utils.Poll(
        timeout=1_000,
        callback=lambda self: cpu.set_label(
            fetch_service.bind("cpu_temp", lambda x: f"  : {round(x)}")
        ),
    )
    mem_used = Widget.Scale(
        min=0,
        max=fetch_service.bind("mem_total"),
        value=fetch_service.bind("mem_used"),
        width_request=100,
        css_classes=["slider"],
    )
    mem = Widget.Box(
        child=[Widget.Label(label=" "), mem_used],
        spacing=15,
    )
    Utils.Poll(
        timeout=1_000,
        callback=lambda self: mem_used.set_value(fetch_service.bind("mem_used")),
    )
    uptime = Widget.Label(
        label=fetch_service.bind("uptime", lambda x: f"{x[0]}:{x[1]}:{x[2]}")
    )
    Utils.Poll(
        timeout=1_000,
        callback=lambda self: uptime.set_label(
            f"{fetch_service.uptime[0]}:{fetch_service.uptime[1]}:{fetch_service.uptime[2]}"
        ),
    )
    box = Widget.Box(
        child=[
            logo,
            separator_maker(),
            cpu,
            separator_maker(),
            mem,
            separator_maker(),
            uptime,
        ],
        css_classes=["bar"],
        spacing=13,
    )
    modules.windows.BackgroundWindow(
        "stats", monitor, box, {"anchor": ["bottom"], "margin_bottom": 20}
    )
