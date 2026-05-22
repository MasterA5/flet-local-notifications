from .AndroidNotificationButton import AndroidNotificationButton
from android_notify import NotificationStyles
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class AndroidNotificationConfig:
    title: str
    message: str
    style: NotificationStyles = NotificationStyles.DEFAULT
    channel_name: str = "default-channel-name"
    channel_id: str = "default-channel-id"
    buttons: Optional[List[AndroidNotificationButton]] = None
    body: Optional[str] = None
    big_picture: Optional[str] = None
    large_icon: Optional[str] = None
    small_icon: Optional[str] = None
    lines: Optional[List[str]] = None
    background_color: Optional[str] = None

    def add_button(cls, button: AndroidNotificationButton):
        cls.sender.addButton(
            text=button.text, 
            on_release=button.on_release, 
            receiver_name=button.receiver_name,
            action=button.action
        )

    def delete_all_buttons(cls):
        cls.buttons.clear()
        cls.sender.removeButtons()