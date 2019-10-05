from core.sprite import Sprite
from core.ui.user_inteface_renderer import UserInterfaceRender


class UserInterface(Sprite):
    def __init__(self, rect):
        self.elements = []
        super().__init__(rect, UserInterfaceRender(self.elements))
        self.hashed = []

    def add_element(self, el):
        self.elements.append(el)
        self.hashed.append(hash(el))
        self.need_render = True

    def update(self):
        super().update()
        for i, e in enumerate(self.elements):
            if hash(e) != self.hashed[i]:
                self.need_render = True
                self.hashed[i] = hash(e)
