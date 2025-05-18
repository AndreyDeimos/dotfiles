from ignis.services.fetch import FetchService
from ignis.widgets import Widget
from ignis.utils import Utils
import modules.windows

fetch_service = FetchService.get_default()


def Stats(monitor):
    separator1 = Widget.Label(label="|")
    separator2 = Widget.Label(label="|")
    separator3 = Widget.Label(label="|")
    logo = Widget.Icon(image=fetch_service.bind("os_logo"))
    cpu = Widget.Label(label=fetch_service.bind("cpu_temp", lambda x: f"  : {x}"))
    mem = Widget.Box(
        child=[
            Widget.Label(label=" "),
            Widget.Scale(
                min=100,
                max=fetch_service.bind("mem_total"),
                value=fetch_service.bind("mem_used"),
                width_request=100,
                css_classes=["slider"],
            ),
        ],
        spacing=15,
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
        child=[logo, separator1, cpu, separator2, mem, separator3, uptime],
        css_classes=["bar"],
        spacing=13,
    )
    modules.windows.BackgroundWindow(
        "stats", monitor, box, {"anchor": ["bottom"], "margin_bottom": 20}
    )
