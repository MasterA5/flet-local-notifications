from desktop_notifier import Button, ReplyField, Urgency
from typing import Any, Callable, Optional, Sequence
from dataclasses import dataclass
from pathlib import Path

try:
    from desktop_notifier import Attachment, Icon, Sound
except ImportError:
    Attachment = None
    Icon = None
    Sound = None

@dataclass
class DesktopNotificationConfig:
    title: str
    message: str
    app_name: str
    icon: Optional[Icon] = None # type: ignore # ignore
    urgency: Urgency = Urgency.Critical
    icon: Optional[Path] = None
    buttons: Sequence[Button] = ()
    reply_field: Optional[ReplyField] = None
    on_dispatched: Optional[Callable[[], Any]] = None
    on_clicked: Optional[Callable[[], Any]] = None
    on_dismissed: Optional[Callable[[], Any]] = None
    attachment: Optional[Attachment] = None # type: ignore # ignore
    sound: Optional[Sound] = None # type: ignore # ignore
    thread: Optional[str] = None
    timeout: int = -1
    use_default_icon: bool = False