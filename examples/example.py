from datetime import timedelta

from flet_local_notifications import (
    FletLocalNotification, 
    DesktopNotificationConfig, 
    AndroidNotificationConfig, 
    DesktopScheduleNotificationConfig, 
    AndroidScheduleNotificationConfig
)
from flet import *

def main(page: Page):
    """
    Basic Minimun Example App For Send Notification In Desktop And Android Devices
    """

    notification_manager = FletLocalNotification(page)

    async def send(e: ControlEvent):
        await notification_manager.send(
            desktop_config=DesktopNotificationConfig("hello", "hello", app_name="Flet App"),
            android_config=AndroidNotificationConfig("hello", "hello"),
            on_sent=lambda: (page.controls.append(Text("Notification Sented !!")), page.update())
        )
    
    async def send_schedule(e: ControlEvent):
        await notification_manager.schedule(
            desktop_schedule_config=DesktopScheduleNotificationConfig(
                desktop_config=DesktopNotificationConfig("hello", "hello", app_name="Flet App"),
                notify_time=timedelta(seconds=5) # <- 5 secconds for wait
            ),
            android_schedule_config=AndroidScheduleNotificationConfig(
                android_config=AndroidNotificationConfig("hello", "hello"),
                notify_time=timedelta(seconds=5) # <- 5 secconds for wait
            )
        )
    

    page.add(Button("Send", on_click=send), Button("Send Schedule", on_click=send_schedule))
app(target=main)