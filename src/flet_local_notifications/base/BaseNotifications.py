from abc import ABC, abstractmethod

class BaseNotification(ABC):
    def __init__(self):
        super().__init__()
        self.sender = None

    @abstractmethod
    def get_sender(self):
        return self.sender

    @abstractmethod
    async def send(config):
        pass