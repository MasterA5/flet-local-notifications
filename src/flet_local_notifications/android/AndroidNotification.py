from typing import Literal
from typing import cast
import asyncio
from datetime import datetime, timedelta

from ..base.BaseNotifications import BaseNotification
from android_notify import Notification
from .android_types import (
    AndroidScheduleNotificationConfig,
    AndroidChannelNotificationConfig,
    AndroidNotificationUpdateConfig,
    AndroidNotificationConfig
)
from flet import Page

class AndroidNotification(BaseNotification):
    def __init__(self, page: Page):
        self.sender: Notification = Notification()
        self.page = page

    def get_sender(self) -> Notification:
        return self.sender

    def update_notification(self, new_config: AndroidNotificationUpdateConfig):
        if new_config.message:
            self.sender.updateMessage(new_config.message)

        if new_config.title:
            self.sender.updateTitle(new_config.title)

        if new_config.ProgressBar:
            title = new_config.ProgressBar.title if new_config.ProgressBar.title else ''
            message = new_config.ProgressBar.message if new_config.ProgressBar.message else ''
            current_value = new_config.ProgressBar.current_value if new_config.ProgressBar.current_value is not None else 0

            self.sender.updateProgressBar(
                title=title,
                message=message,
                current_value=current_value,
            )

    def create_channel(self, channel_config: AndroidChannelNotificationConfig):
        self.sender.createChannel(
            id=channel_config.channel_id,
            name=channel_config.channel_name if channel_config.channel_name else 'default-channel-name',
            description=channel_config.description,
            importance=cast(Literal['urgent', 'high', 'medium', 'low', 'none'], channel_config.importance.value),
            res_sound_name=channel_config.res_sound_name,
            vibrate=channel_config.vibrate
        )

    async def send(self, config: AndroidNotificationConfig):  # type: ignore[override]
        self.sender = Notification(
            title=config.title,
            message=config.message,
            style=config.style,
            channel_name=config.channel_name,
            channel_id=config.channel_id,
            logs=False
        )

        if config.background_color:
            self.sender.setColor(config.background_color)

        if config.lines:
            for line in config.lines:
                self.sender.addLine(line)

        if config.large_icon:
            self.sender.setLargeIcon(config.large_icon)

        if config.small_icon:
            self.sender.setSmallIcon(config.small_icon)

        if config.big_picture:
            self.sender.setBigPicture(config.big_picture)

        if config.body:
            self.sender.setBigText(config.body)

        if config.buttons and len(config.buttons) <= 3:
            for button in config.buttons:
                self.sender.addButton(
                    text=button.text,
                    on_release=button.on_release,
                    receiver_name=button.receiver_name,
                    action=button.action,
                )

        self.sender.send()

    async def send_schedule(self, schedule_android_config: AndroidScheduleNotificationConfig) -> asyncio.Task[None]:
        if isinstance(schedule_android_config.notify_time, datetime):
            delta = schedule_android_config.notify_time - datetime.now()
            wait_seconds = max(0, delta.total_seconds())
        elif isinstance(schedule_android_config.notify_time, timedelta):
            wait_seconds = max(0, schedule_android_config.notify_time.total_seconds())
        else:
            wait_seconds = max(0, float(schedule_android_config.notify_time))
        
        async def _waiter():
            await asyncio.sleep(wait_seconds)
            await self.send(schedule_android_config.android_config)
        
        task = asyncio.create_task(_waiter())
        
        if schedule_android_config.cancel_on_exit:
            self.page.on_close = lambda e: task.cancel()
        
        return task