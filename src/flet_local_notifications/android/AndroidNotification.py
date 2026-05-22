from ..base.BaseNotifications import BaseNotification
from android_notify import Notification
from .types import (
    AndroidChannelNotificationConfig,
    AndroidNotificationUpdateConfig,
    AndroidNotificationConfig,
)

class AndroidNotification(BaseNotification):
    def __init__(self):
        self.sender: Notification = None

    def update_notification(self, new_config: AndroidNotificationUpdateConfig):
        if new_config.message:
            self.sender.updateMessage(new_config.message)

        if new_config.title:
            self.sender.updateTitle(new_config.title)

        if new_config.ProgressBar:
            self.sender.updateProgressBar(
                title=new_config.ProgressBar.title,
                message=new_config.ProgressBar.message,
                current_value=new_config.ProgressBar.current_value,
            )

    def create_channel(self, channel_config: AndroidChannelNotificationConfig):
        self.sender.createChannel(
            id=channel_config.channel_id,
            name=channel_config.channel_name,
            description=channel_config.description,
            importance=channel_config.importance.value,
            res_sound_name=channel_config.res_sound_name,
            vibrate=channel_config.vibrate
        )

    async def send(self, config: AndroidNotificationConfig):   
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

    def get_sender(self) -> Notification:
        return self.sender