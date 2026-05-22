from flet import Page, PagePlatform, OptionalControlEventCallable
from .schedule.schedule_types import ScheduleNotificationConfig
from .android.AndroidNotification import AndroidNotification
from .desktop.DesktopNotification import DesktopNotification
from android_notify import Notification, NotificationHandler
from .desktop.types import DesktopNotificationConfig
from .android.types import AndroidNotificationConfig
from desktop_notifier import DesktopNotifier
from datetime import datetime, timedelta
import asyncio

class FletLocalNotification:
    def __init__(self, page: Page, on_permission_accepted: OptionalControlEventCallable = None):
        self.page = page
        self.__android_sender = AndroidNotification()
        self.__desktop_sender = DesktopNotification()
        self.__on_permission_accepted = on_permission_accepted

        if not self.page:
            raise ValueError("Page is required")

        self.__init_handler()
        
    @property
    def android_sender(self) -> Notification:
        return self.__android_sender.get_sender()
    
    @property
    def desktop_sender(self) -> DesktopNotifier:
        return self.__desktop_sender.get_sender()

    def __init_handler(self) -> None:
        if self.is_android():
            NotificationHandler.asks_permission(self.__on_permission_accepted)
            self.__handler = self.__android_sender
        elif self.is_desktop():
            self.__handler = self.__desktop_sender
        else:
            self.__handler = None

    def is_android(self) -> bool:
        return self.page.platform == PagePlatform.ANDROID

    def is_desktop(self) -> bool:
        return self.page.platform in (PagePlatform.LINUX, PagePlatform.WINDOWS, PagePlatform.MACOS)

    async def send(
        self, 
        android_config: AndroidNotificationConfig, 
        desktop_config: DesktopNotificationConfig
    ) -> None:
        await self.__handler.send(config=android_config if self.is_android() else desktop_config)

    async def schedule(
        self, 
        config: ScheduleNotificationConfig, 
        android_config: AndroidNotificationConfig, 
        desktop_config: DesktopNotificationConfig
    ) -> asyncio.Task:
        if isinstance(config.notify_time, datetime):
            delta = config.notify_time - datetime.now()
            wait_seconds = max(0, delta.total_seconds())
        elif isinstance(config.notify_time, timedelta):
            wait_seconds = max(0, config.notify_time.total_seconds())
        else:
            wait_seconds = max(0, float(config.notify_time))
        
        async def _waiter():
            await asyncio.sleep(wait_seconds)
            await self.send(android_config, desktop_config)
        
        task = asyncio.create_task(_waiter())
        
        if config.cancel_on_exit:
            self.page.on_close = lambda e: task.cancel()
        
        return task