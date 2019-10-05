from core.renderer import Renderer
from core.colors import white


class UserInterfaceRender(Renderer):
    def __init__(self, elements):
        super().__init__()
        self.elements = elements

    def render(self, screen, rect):
        screen.set_colorkey(white)
        screen.fill(white)
        for el in self.elements:
            el.render(screen, rect)
