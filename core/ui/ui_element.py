from abc import ABC, abstractmethod


class UIElement(ABC):
    def __init__(self, rect):
        self.rect = rect
        self._ui_update = lambda: None

    @abstractmethod
    def render(self, screen, rect):
        pass

    def update(self):
        self._ui_update()
