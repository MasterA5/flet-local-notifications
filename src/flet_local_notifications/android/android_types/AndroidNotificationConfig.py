from dataclasses import field
from android_notify import Notification
from .AndroidNotificationButton import AndroidNotificationButton
from android_notify import NotificationStyles
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class AndroidNotificationConfig:
    title: str
    message: str
    # pyrefly: ignore [bad-assignment]
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
    sender: Optional[Notification] = field(init=False, default=None)

    def add_button(self, button: AndroidNotificationButton):
        if not self.buttons:
            self.buttons = []

        if not self.sender:
            raise ValueError("Notification sender is not initialized. Please send the notification before adding buttons.")
        
        self.sender.addButton(
            text=button.text, 
            on_release=button.on_release, 
            receiver_name=button.receiver_name,
            action=button.action
        )

    def delete_all_buttons(self):
        if not self.buttons:
            return

        if not self.sender:
            raise ValueError("Notification sender is not initialized. Please send the notification before deleting buttons.")

        self.buttons.clear()
        self.sender.removeButtons()