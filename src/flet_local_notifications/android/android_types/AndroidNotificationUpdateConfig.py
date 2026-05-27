from .AndroidProgressBarUpdateConfig import AndroidProgressBarUpdateConfig
from dataclasses import dataclass
from typing import Optional

@dataclass
class AndroidNotificationUpdateConfig:
    title: Optional[str] = None
    message: Optional[str] = None
    ProgressBar: Optional[AndroidProgressBarUpdateConfig] = None