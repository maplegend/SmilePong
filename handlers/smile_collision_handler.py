from core.update_handler import UpdateHandler
from sprites.paddle import Paddle
from sprites.smile import Smile
import pygame


class SmileCollisionHandler(UpdateHandler):
    def __init__(self, col_edge):
        super().__init__()
        self.col_edge = col_edge

    def handle_smile_collision(self, smile):
        if self.scene.bounds.x > smile.rect.x or self.scene.bounds.width < smile.rect.right:
            smile.direction.reflect_ip(pygame.Vector2(1, 0))
        if self.scene.bounds.y > smile.rect.y or self.scene.bounds.height < smile.rect.bottom:
            self.col_edge(self.scene.bounds.y > smile.rect.y)

        for paddle in [p for p in self.scene.get_sprites() if isinstance(p, Paddle)]:
            if paddle.rect.colliderect(smile.rect):
                smile.direction.reflect_ip(pygame.Vector2(0, 1))

    def update(self):
        [self.handle_smile_collision(s) for s in self.scene.get_sprites() if isinstance(s, Smile)]
