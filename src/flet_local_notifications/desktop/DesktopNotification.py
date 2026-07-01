import asyncio
from datetime import datetime, timedelta
import os
from pathlib import Path

from ..base.BaseNotifications import BaseNotification
from desktop_notifier import DesktopNotifier, Urgency
from .desktop_types import DesktopNotificationConfig, DesktopScheduleNotificationConfig
from flet import Page

try:
    from desktop_notifier import Icon
    FLET_APP_ICON = Path(os.path.join(os.getenv("FLET_ASSETS_DIR") or "", "icon.png")) # <- default icon created by flet in assets folder
except ImportError:
    Icon = None
except TypeError:
    FLET_APP_ICON = None

class DesktopNotification(BaseNotification):
    def __init__(self, page: Page):
        self.sender: DesktopNotifier = DesktopNotifier(app_name="Flet App")
        self.page = page

        if not self.page:
            raise ValueError("Page is required")
        
    def get_sender(self) -> DesktopNotifier:
        return self.sender

    async def send_schedule(self, schedule_desktop_config: DesktopScheduleNotificationConfig) -> asyncio.Task[None]:
        if isinstance(schedule_desktop_config.notify_time, datetime):
            delta = schedule_desktop_config.notify_time - datetime.now()
            wait_seconds = max(0, delta.total_seconds())
        elif isinstance(schedule_desktop_config.notify_time, timedelta):
            wait_seconds = max(0, schedule_desktop_config.notify_time.total_seconds())
        else:
            wait_seconds = max(0, float(schedule_desktop_config.notify_time))
        
        async def _waiter():
            await asyncio.sleep(wait_seconds)
            await self.send(schedule_desktop_config.desktop_config)
        
        task = asyncio.create_task(_waiter())
        
        if schedule_desktop_config.cancel_on_exit:
            self.page.on_close = lambda e: task.cancel()
        
        return task

    async def send(self, config: DesktopNotificationConfig):
        icon_path = config.icon if isinstance(config.icon, Path) else FLET_APP_ICON if FLET_APP_ICON else Path(__file__).parent.parent.resolve() / "assets" / "default_icon.png"
        self.sender = DesktopNotifier(
            app_name=config.app_name,
            # pyrefly: ignore [not-callable]
            app_icon=Icon(
                path=icon_path
            )
        )

        await self.sender.send(
            title=config.title,
            message=config.message,
            urgency=Urgency.Critical,
            # pyrefly: ignore [not-callable]
            icon=Icon(path=icon_path),
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