from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Union

@dataclass
class ScheduleNotificationConfig:
    notify_time: Union[datetime, timedelta, float, int]
    cancel_on_exit: bool = True