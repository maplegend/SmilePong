from core.sprite import Sprite
from core.utils import rand_vec
from renderers.smile_renderer import SmileRenderer
import pygame


class Smile(Sprite):
    def __init__(self, pos):
        super().__init__(pygame.Rect((pos[0], pos[1], 200, 200)), SmileRenderer())
        self.speed = 10
        self.direction = rand_vec(1)

    def update(self):
        self.rect.move_ip(self.direction * self.speed)
