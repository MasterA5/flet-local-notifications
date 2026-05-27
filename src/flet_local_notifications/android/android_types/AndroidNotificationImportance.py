from typing import Literal
from enum import Enum

class AndroidNotificationImportance(str, Enum):
    URGENT = 'urgent'
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'
    NONE = 'none'
