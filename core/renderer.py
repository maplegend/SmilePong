from abc import ABC, abstractmethod


class Renderer(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def render(self, screen, rect):
        pass
