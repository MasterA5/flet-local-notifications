from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Union

from .AndroidNotificationConfig import AndroidNotificationConfig

@dataclass
class AndroidScheduleNotificationConfig:
    android_config: AndroidNotificationConfig
    notify_time: Union[datetime, timedelta, float, int]
    cancel_on_exit: bool = True