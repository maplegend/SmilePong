import pygame
from abc import ABC, abstractmethod
from .update_handler import UpdateHandler


class Sprite(UpdateHandler, ABC):
    def __init__(self, rect, renderer):
        super().__init__()
        self.need_render = True
        self.rect = rect
        self.renderer = renderer
        self.rendered_sprite = pygame.Surface((rect.width, rect.height))
        self.update_render()

    def render(self, screen, rect):
        self.renderer.render(screen, rect)

    def update_render(self):
        self.render(self.rendered_sprite, pygame.Rect(0, 0, self.rect.width, self.rect.height))