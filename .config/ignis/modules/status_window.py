from ignis.services.fetch import FetchService
from ignis.widgets import Widget
import modules.windows

fetch_service = FetchService.get_default()


def Stats(monitor):
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
        spacing=12,
    )
    box = Widget.Box(child=[logo, cpu, mem], css_classes=["bar"], spacing=13)
    modules.windows.BackgroundWindow(
        "stats", monitor, box, {"anchor": ["bottom"], "margin_bottom": 20}
    )
