from .AndroidNotificationImportance import AndroidNotificationImportance
from dataclasses import dataclass
from typing import Optional

@dataclass
class AndroidChannelNotificationConfig:
    channel_id: Optional[str] = None
    channel_name: Optional[str] = None
    description: Optional[str] = None
    importance: AndroidNotificationImportance = AndroidNotificationImportance.URGENT
    res_sound_name: Optional[str] = None
    vibrate: bool = False