import pygame
import sys
from interactors.game import Game

"""
WARNING
if game will be lagging press F to enter full screen mode
for some reasons pygame works in full screen faster
"""


def main():
    pygame.init()
    game = Game()

    game.input_handler.bind(pygame.K_ESCAPE, lambda: sys.exit())

    clock = pygame.time.Clock()

    while 1:
        game.game_tick()
        clock.tick(60)


if __name__ == "__main__":
    main()
