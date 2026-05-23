import os
from pathlib import Path

from flet_local_notifications import FletLocalNotification, DesktopNotificationConfig, AndroidNotificationConfig
from flet import *

def main(page: Page):
    """
    Basic Minimun Example App For Send Notification In Desktop And Android Devices
    """

    notification_manager = FletLocalNotification(page)

    async def send(e: ControlEvent):
        await notification_manager.send(
            desktop_config=DesktopNotificationConfig("hello", "hello", app_name="Nose"),
            android_config=AndroidNotificationConfig("hello", "hello"),
            on_sent=lambda: (page.controls.append(Text("Notification Sented !!")), page.update())
        )

    page.add(Button("Send", on_click=send))
app(target=main)