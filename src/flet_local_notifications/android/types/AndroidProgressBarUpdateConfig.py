from dataclasses import dataclass
from typing import Optional

@dataclass
class AndroidProgressBarUpdateConfig:
    current_value: Optional[int] = None
    message: Optional[str] = None
    title: Optional[str] = None