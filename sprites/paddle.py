from core.sprite import Sprite
from core.utils import rand_vec
from renderers.paddle_renderer import PaddleRenderer


class Paddle(Sprite):
    def __init__(self, rect, renderer=PaddleRenderer()):
        super().__init__(rect, renderer)
        self.speed = 5
        self.direction = rand_vec(1)
        self.move_dir = 0

    def update(self):
        self.rect.move_ip((self.move_dir, 0))
        self.move_dir = 0
