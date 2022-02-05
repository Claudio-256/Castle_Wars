import random

import pygame, sys
from pygame.locals import *


def init():
    tilesize = 95 #10 tiles todo tile the map and add sprites
    clock = pygame.time.Clock()
    pygame.init()

    pygame.display.set_caption("Castle wars")
    WINDOW_SIZE = (1050, 424)

    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    bg = pygame.transform.scale(pygame.image.load('../res/sprites/bg_new.png'), (1070, 424))
    castle = pygame.transform.scale(pygame.image.load('../res/sprites/castle.png'), (150, 150))
    mine2 = pygame.transform.scale(pygame.image.load('../res/sprites/mine.png'), (80, 80))
    mine1 = pygame.transform.flip(mine2, True, False)
    barracks = pygame.transform.scale(pygame.image.load('../res/sprites/african_tmp.png'), (130, 75))
    tower = pygame.transform.scale(pygame.image.load('../res/sprites/Tower.png'), (50, 150))
    wall = pygame.transform.scale(pygame.image.load('../res/sprites/wall_tmp.png'), (30, 150))
    swordsman = pygame.transform.scale(pygame.image.load('../res/sprites/knight.gif'), (150, 150))
    i = 0

    while True:
        clock.tick(60)
        screen.blit(bg, (-10, 150))
        screen.blit(castle, (0, 150))
        screen.blit(castle, (WINDOW_SIZE[0]-castle.get_size()[0], 150))
        screen.blit(mine1, (castle.get_size()[0], 225))
        screen.blit(mine2, (WINDOW_SIZE[0] - castle.get_size()[0] - mine2.get_size()[0], 225))
        screen.blit(barracks, (castle.get_size()[0] + mine2.get_size()[0] + 15, 220))
        screen.blit(barracks, (WINDOW_SIZE[0] - castle.get_size()[0] - mine2.get_size()[0] - barracks.get_size()[0] + 30, 220))
        screen.blit(tower, (castle.get_size()[0] + mine2.get_size()[0] + barracks.get_size()[0] - 20, 150))
        screen.blit(tower, (WINDOW_SIZE[0] - castle.get_size()[0] - mine2.get_size()[0] - barracks.get_size()[0] - tower.get_size()[0] + 20, 150))
        screen.blit(wall, (castle.get_size()[0] + mine2.get_size()[0] + barracks.get_size()[0] + wall.get_size()[0] + 5, 180))
        screen.blit(wall, (WINDOW_SIZE[0] - castle.get_size()[0] - mine2.get_size()[0] - barracks.get_size()[0] - tower.get_size()[0] - wall.get_size()[0] + 18, 180))

        x, y = pygame.mouse.get_pos()
        ra = random.Random()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c or True:
                    screen.blit(swordsman, (ra.randint(1, WINDOW_SIZE[0]), ra.randint(1, WINDOW_SIZE[1])))

                    i = i+1


        pygame.display.update()


