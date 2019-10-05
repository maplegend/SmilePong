from abc import ABC, abstractmethod


class UpdateHandler(ABC):
    def __init__(self):
        self.scene = None

    @abstractmethod
    def update(self):
        pass