from .ui_element import UIElement
from core.colors import black, white
import pygame


class TextElement(UIElement):
    def __init__(self, rect, text, font_size):
        super().__init__(rect)
        self.font = pygame.font.Font(pygame.font.get_default_font(), font_size)
        self.text = text

    def render(self, screen, rect):
        text = self.font.render(self.text, True, black, white)
        screen.blit(text, self.rect)

    def __hash__(self):
        return hash(self.text)
