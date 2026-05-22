from desktop_notifier import DesktopNotifier, Urgency
from .types import DesktopNotificationConfig
from ..base.BaseNotifications import BaseNotification
from pathlib import Path
import os

try:
    from desktop_notifier import Icon
    FLET_APP_ICON = os.path.join(os.getenv("FLET_ASSETS_DIR/icon.png", f"{os.getcwd()}\\assets\\"), "icon.png") # <- default icon in assets folder
except ImportError:
    Icon = None

class DesktopNotification(BaseNotification):
    def __init__(self):
        self.sender: DesktopNotifier = None

    def get_sender(self) -> DesktopNotifier:
        return self.sender

    async def send(self, config: DesktopNotificationConfig):
        self.sender = DesktopNotifier(
            app_name=config.app_name,
            app_icon=Icon(
                path=config.icon if isinstance(config.icon, Path) else Path(FLET_APP_ICON)
            )
        )

        await self.sender.send(
            title=config.title,
            message=config.message,
            urgency=Urgency.Critical,
            buttons=config.buttons,
            reply_field=config.reply_field,
            on_dispatched=config.on_dispatched,
            on_clicked=config.on_clicked,
            on_dismissed=config.on_clicked,
            attachment=config.attachment,
            sound=config.sound,
            thread=config.thread,
            timeout=config.timeout,
        )