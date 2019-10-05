from sprites.paddle import Paddle
from core.constants import width


class PaddleAI(Paddle):
    def __init__(self, rect, target):
        super().__init__(rect)
        self.target = target

    def update(self):
        if abs(self.target.rect.y - self.rect.y) < width//4:
            if self.target.rect.x > self.rect.x:
                self.move_dir += min(self.speed, self.target.rect.x - self.rect.x)
            elif self.target.rect.x < self.rect.x:
                self.move_dir -= min(self.speed, self.rect.x - self.target.rect.x)
        super().update()
