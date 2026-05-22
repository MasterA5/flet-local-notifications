from enum import Enum

class AndroidNotificationImportance(Enum):
    URGENT = 'urgent'
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'
    NONE = 'none'