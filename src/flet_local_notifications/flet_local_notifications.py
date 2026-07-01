from typing import Callable, Optional, Union

from flet import Page, PagePlatform, OptionalControlEventCallable
from .android.AndroidNotification import AndroidNotification
from .desktop.DesktopNotification import DesktopNotification
from android_notify import Notification, NotificationHandler
from .desktop.desktop_types import DesktopNotificationConfig, DesktopScheduleNotificationConfig
from .android.android_types import AndroidNotificationConfig, AndroidScheduleNotificationConfig
from desktop_notifier import DesktopNotifier

class FletLocalNotification:
    def __init__(self, page: Page, on_permission_accepted: OptionalControlEventCallable = None):
        self.page = page
        
        if not self.page:
            raise ValueError("Page is required")
        
        self.__on_permission_accepted = on_permission_accepted
        
        if self.is_android():
            NotificationHandler.asks_permission(self.__on_permission_accepted)
        
        self.__android = AndroidNotification(self.page)
        self.__desktop = DesktopNotification(self.page)
        
    @property
    def android_sender(self) -> Notification:
        return self.__android.get_sender()
    
    @property
    def desktop_sender(self) -> DesktopNotifier:
        return self.__desktop.get_sender()

    def is_android(self) -> bool:
        return self.page.platform == PagePlatform.ANDROID

    def is_desktop(self) -> bool:
        return self.page.platform in (PagePlatform.LINUX, PagePlatform.WINDOWS, PagePlatform.MACOS)

    async def send(
        self, 
        android_config: Optional[AndroidNotificationConfig] = None, 
        desktop_config: Optional[DesktopNotificationConfig] = None, 
        on_sent: Optional[Callable[[], None]] = None
    ) -> None:
        if not android_config and self.is_android():
            raise ValueError("You must configure your notification for the Android platform using the AndroidNotificationConfig class")
        
        if not desktop_config and self.is_desktop():
            raise ValueError("You must configure your notification for the Desktop platform using the DesktopNotificationConfig class")

        if self.is_desktop() and desktop_config:
            await self.__desktop.send(desktop_config)
        
        if self.is_android() and android_config:
            await self.__android.send(android_config)

        if on_sent:
            on_sent()

    async def schedule(
        self, 
        android_schedule_config: Optional[AndroidScheduleNotificationConfig] = None,
        desktop_schedule_config: Optional[DesktopScheduleNotificationConfig] = None, 
    ) -> None:
        if not desktop_schedule_config and self.is_desktop():
            raise ValueError("You need to configure your schedule for notifications using the `DesktopScheduleNotificationConfig` class")
        
        if not android_schedule_config and self.is_android():
            raise ValueError("You need to configure your schedule for notifications using the `AndroidScheduleNotificationConfig` class")
        
        if self.is_android() and android_schedule_config:
            await self.__android.send_schedule(android_schedule_config)

        if self.is_desktop() and desktop_schedule_config:
            await self.__desktop.send_schedule(desktop_schedule_config)