from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Union

from .DesktopNotificationConfig import DesktopNotificationConfig

@dataclass
class DesktopScheduleNotificationConfig:
    desktop_config: DesktopNotificationConfig
    notify_time: Union[datetime, timedelta, float, int]
    cancel_on_exit: bool = True