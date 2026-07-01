from typing import Any
from abc import ABC, abstractmethod

class BaseNotification(ABC):
    def __init__(self):
        super().__init__()
        self.sender: Any = None

    @abstractmethod
    def get_sender(self):
        return self.sender

    @abstractmethod
    async def send(self, config: Any) -> None:
        pass