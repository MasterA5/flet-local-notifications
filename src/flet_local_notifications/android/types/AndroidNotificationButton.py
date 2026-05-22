from typing import Callable, Optional
from dataclasses import dataclass

@dataclass
class AndroidNotificationButton:
    text: str
    on_release: Optional[Callable] = None
    receiver_name: Optional[str] = None
    action: Optional[str] = None