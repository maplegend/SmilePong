from core.renderer import Renderer
from core.colors import white, black
import pygame


class PaddleRenderer(Renderer):
    def render(self, screen, rect):
        screen.set_colorkey(white)
        screen.fill(white)

        pygame.draw.rect(screen, black, (rect.x+rect.h//2, rect.y, rect.w - rect.h, rect.h))
        pygame.draw.circle(screen, black, (rect.x+rect.h//2, rect.y + rect.h//2), rect.h//2)
        pygame.draw.circle(screen, black, (rect.x+rect.w-rect.h//2, rect.y + rect.h//2), rect.h//2)
