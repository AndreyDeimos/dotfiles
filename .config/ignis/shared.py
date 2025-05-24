from modules import windows
from ignis.services.system_tray import SystemTrayService, SystemTrayItem

window_manager = windows.WindowManager()
system_tray = SystemTrayService.get_default()
