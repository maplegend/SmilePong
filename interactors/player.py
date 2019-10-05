from sprites.paddle import Paddle
import pygame


class Player:
    def __init__(self, player_paddle, scene):
        self.playing_started = False
        self.paddle = player_paddle
        self.scene = scene

    def bind_keys(self, uinput):
        uinput.bind(pygame.K_LEFT, self.move_left)
        uinput.bind(pygame.K_a, self.move_left)
        uinput.bind(pygame.K_RIGHT, self.move_right)
        uinput.bind(pygame.K_d, self.move_right)

    def start_playing(self):
        self.scene.delete_sprite(self.paddle)
        self.paddle = Paddle(self.paddle.rect, self.paddle.renderer)
        self.scene.add_sprite(self.paddle)

    def control_key_pressed(self):
        if not self.playing_started:
            self.start_playing()
        self.playing_started = True

    def move_right(self):
        self.control_key_pressed()
        if self.paddle.rect.right < self.scene.bounds.right:
            self.paddle.move_dir += self.paddle.speed

    def move_left(self):
        self.control_key_pressed()
        if self.paddle.rect.x - self.paddle.speed > 0:
            self.paddle.move_dir -= self.paddle.speed
