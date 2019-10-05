from core.scene import Scene
from core.ui.user_interface import UserInterface
from core.ui.text_element import TextElement
from core.input_handler import InputHandler
from core.constants import size, width, height
from core.colors import white
from handlers.smile_collision_handler import SmileCollisionHandler
from sprites.smile import Smile
from sprites.paddle_ai import PaddleAI
from .player import Player

import pygame
import sys


class Game:
    def __init__(self):
        self.main_screen = pygame.display.set_mode(size)  # pygame.FULLSCREEN
        self.scene = Scene(pygame.Rect(0, 0, width, height), self.main_screen)
        self.input_handler = InputHandler()
        self.input_handler.bind(pygame.K_f, self.toggle_full_screen)
        self.full_screen = False

        self.ui = UserInterface(pygame.Rect(0, 0, width, height))
        self.scene.add_sprite(self.ui)
        self.score_ui = TextElement(pygame.Rect(width - 100, height // 2, 200, 200), "0:0", 40)
        self.ui.add_element(self.score_ui)

        self.scene.add_handler(SmileCollisionHandler(self.collide_edge))

        self.start_pos = width // 2 - 100, height // 2 - 100
        self.smile = Smile(self.start_pos)
        self.scene.add_sprite(self.smile)

        self.scene.add_sprite(PaddleAI(pygame.Rect(width // 2 - 100, 50, 200, 20), self.smile))

        player_paddle = PaddleAI(pygame.Rect(width // 2 - 100, height - 70, 200, 20), self.smile)
        self.scene.add_sprite(player_paddle)
        self.player = Player(player_paddle, self.scene)
        self.player.bind_keys(self.input_handler)

        self.score = [0, 0]

    def toggle_full_screen(self):
        self.full_screen = not self.full_screen
        pygame.display.quit()
        pygame.display.init()
        if self.full_screen:
            self.main_screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        else:
            self.main_screen = pygame.display.set_mode(size)

    def _render_sprite(self, sprite):
        self.main_screen.blit(sprite.rendered_sprite, sprite.rect)

    def collide_edge(self, top):
        if top:
            self.score[1] += 1
        else:
            self.score[0] += 1
        self.score_ui.text = "{}:{}".format(self.score[0], self.score[1])
        self.restart()

    def restart(self):
        self.smile.rect = pygame.Rect(self.start_pos[0], self.start_pos[1], self.smile.rect.w, self.smile.rect.h)

    def game_tick(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

        [self.input_handler.handle(i) for i, k in enumerate(pygame.key.get_pressed()) if k != 0]

        self.main_screen.fill(white)

        [h.update() for h in self.scene.get_handlers()]
        for sp in self.scene.get_sprites():
            if sp.need_render:
                sp.update_render()
                sp.need_render = False

        [self._render_sprite(sp) for sp in self.scene.get_sprites()]

        pygame.display.flip()
