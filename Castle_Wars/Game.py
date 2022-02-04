import pygame, sys
from pygame.locals import *


def init():
    tilesize = 95 #10 tiles todo tile the map and add sprites
    clock = pygame.time.Clock()
    pygame.init()

    pygame.display.set_caption("Castle wars")
    WINDOW_SIZE = (950, 424)

    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    display = pygame.Surface((150, 100))
    bg = pygame.image.load('../res/sprites/bg.png')

    while True:
        clock.tick(60)
        screen.blit(bg, (0, 0))
        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()


