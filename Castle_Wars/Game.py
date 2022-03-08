import pygame, sys

from Entities import Worker, Swordsman, Archer
from Entities.Player import Player
from Commands import Commands
from pygame.locals import *


def init():
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
    swordsman1 = pygame.transform.scale(pygame.image.load('../res/sprites/knight.gif'), (100, 100))
    swordsman2 = pygame.transform.flip(swordsman1, True, False)
    worker1 = pygame.transform.scale(pygame.image.load("../res/sprites/woodcutter-001_side.png"), (50, 50))
    worker2 = pygame.transform.flip(worker1, True, False)
    archer1 = pygame.transform.scale(pygame.image.load("../res/sprites/archer.png"), (50, 50))
    archer2 = pygame.transform.flip(archer1, True, False)

    worker1_at_mine_pos = (castle.get_size()[0] + 30, 250)
    worker2_at_mine_pos = (WINDOW_SIZE[0] - castle.get_size()[0] - mine2.get_size()[0], 250)
    worker1_at_wall_pos = (castle.get_size()[0] + 195, 250)
    worker2_at_wall_pos = (WINDOW_SIZE[0] - castle.get_size()[0] - mine2.get_size()[0] - 160, 250)
    swordsman1_at_enemy_pos = (castle.get_size()[0] + mine2.get_size()[0] + barracks.get_size()[0] + wall.get_size()[0] + 10, 210)
    swordsman2_at_enemy_pos = (WINDOW_SIZE[0] - castle.get_size()[0] - mine2.get_size()[0] - barracks.get_size()[0] - tower.get_size()[0] - wall.get_size()[0] - 60, 210)
    swordsman1_at_enemy_wall_pos = (castle.get_size()[0] + mine2.get_size()[0] + barracks.get_size()[0] + wall.get_size()[0] + 130, 210)
    swordsman2_at_enemy_wall_pos = (WINDOW_SIZE[0] - castle.get_size()[0] - mine2.get_size()[0] - barracks.get_size()[0] - tower.get_size()[0] - wall.get_size()[0] - 180, 210)
    archer1_on_tower_pos = (castle.get_size()[0] + mine2.get_size()[0] + barracks.get_size()[0] - 10, 110)
    archer2_on_tower_pos = (WINDOW_SIZE[0] - castle.get_size()[0] - mine2.get_size()[0] - barracks.get_size()[0] - tower.get_size()[0] + 10, 110)

    player1 = Player()
    player2 = Player()
    turn = True     #Player1's turn

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




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if turn: # player1
                    if event.key == Commands.p1_train_worker:
                        if player1.castle.INIT_RESOURCES >= Worker.Worker.WORKER_COST:
                            player1.castle.INIT_RESOURCES -= Worker.Worker.WORKER_COST
                            print("[P1] Adding worker")
                            tmp_worker = Worker.Worker()
                            player1.worker_list.append(tmp_worker)
                            turn = False
                        else:
                            print("[P1] Insufficient resources! You have: " + str(player1.castle.INIT_RESOURCES) + ", needed: " + str(Worker.Worker.WORKER_COST))
                    elif event.key == Commands.p1_train_swordsman:
                        if player1.castle.INIT_RESOURCES >= Swordsman.Swordsman.SWORDSMAN_COST:
                            player1.castle.INIT_RESOURCES -= Swordsman.Swordsman.SWORDSMAN_COST
                            print("[P1] Adding swordsman")
                            tmp_swordsman = Swordsman.Swordsman()
                            player1.swordsman_list.append(tmp_swordsman)
                            turn = False
                        else:
                            print("[P1] Insufficient resources! You have: " + str(player1.castle.INIT_RESOURCES) + ", needed: " + str(Swordsman.Swordsman.SWORDSMAN_COST))
                    elif event.key == Commands.p1_train_archer:
                        if player1.castle.INIT_RESOURCES >= Archer.Archer.ARCHER_COST:
                            player1.castle.INIT_RESOURCES -= Archer.Archer.ARCHER_COST
                            print("[P1] Adding archer")
                            tmp_archer = Archer.Archer()
                            player1.archer_list.append(tmp_archer)
                            turn = False
                        else:
                            print("[P1] Insufficient resources! You have: " + str(player1.castle.INIT_RESOURCES) + ", needed: " + str(Archer.Archer.ARCHER_COST))
                    elif event.key == Commands.p1_dispatch_worker_mine:
                        if len(player1.worker_list):        #worker list is not empty
                            player1.worker_list[-1].WORKER_POS = worker1_at_mine_pos
                            player1.worker_list[-1].ON_SCREEN = True
                            turn = False
                        else:
                            print("[P1] You have no available workers")
                    elif event.key == Commands.p1_dispatch_worker_wall:
                        if len(player1.worker_list):  # worker list is not empty
                            player1.worker_list[-1].WORKER_POS = worker1_at_wall_pos
                            player1.worker_list[-1].ON_SCREEN = True
                            turn = False
                        else:
                            print("[P1] You have no available workers")
                    elif event.key == Commands.p1_dispatch_swordsman_attack:
                        pass
                    elif event.key == Commands.p1_dispatch_archer_attack:
                        pass
                    elif event.key == Commands.p1_dispatch_unleash_all:
                        pass

                else: # player2
                    if event.key == Commands.p2_train_worker:
                        if player2.castle.INIT_RESOURCES >= Worker.Worker.WORKER_COST:
                            player2.castle.INIT_RESOURCES -= Worker.Worker.WORKER_COST
                            print("[P2] Adding worker")
                            tmp_worker = Worker.Worker()
                            player2.worker_list.append(tmp_worker)
                            turn = True
                        else:
                            print(
                                "[P2] Insufficient resources! You have: " + str(player2.castle.INIT_RESOURCES) + ", needed: " + str(Worker.Worker.WORKER_COST))
                    elif event.key == Commands.p2_train_swordsman:
                        if player2.castle.INIT_RESOURCES >= Swordsman.Swordsman.SWORDSMAN_COST:
                            player2.castle.INIT_RESOURCES -= Swordsman.Swordsman.SWORDSMAN_COST
                            print("[P2] Adding swordsman")
                            tmp_swordsman = Swordsman.Swordsman()
                            player2.swordsman_list.append(tmp_swordsman)
                            turn = True
                        else:
                            print("[P2] Insufficient resources! You have: " + str(player2.castle.INIT_RESOURCES) + ", needed: " + str(Swordsman.Swordsman.SWORDSMAN_COST))
                    elif event.key == Commands.p2_train_archer:
                        if player2.castle.INIT_RESOURCES >= Archer.Archer.ARCHER_COST:
                            player2.castle.INIT_RESOURCES -= Archer.Archer.ARCHER_COST
                            print("[P1] Adding archer")
                            tmp_archer = Archer.Archer()
                            player2.archer_list.append(tmp_archer)
                            turn = True
                        else:
                            print("[P2] Insufficient resources! You have: " + str(player2.castle.INIT_RESOURCES) + ", needed: " + str(Archer.Archer.ARCHER_COST))
                    elif event.key == Commands.p2_dispatch_worker_mine:
                        if len(player2.worker_list):  # worker list is not empty
                            player2.worker_list[-1].WORKER_POS = worker2_at_mine_pos
                            player2.worker_list[-1].ON_SCREEN = True
                            turn = True
                        else:
                            print("[P2] You have no available workers")
                    elif event.key == Commands.p2_dispatch_worker_wall:
                        if len(player2.worker_list):  # worker list is not empty
                            player2.worker_list[-1].WORKER_POS = worker2_at_wall_pos
                            player2.worker_list[-1].ON_SCREEN = True
                            turn = True
                        else:
                            print("[P2] You have no available workers")
                    elif event.key == Commands.p2_dispatch_swordsman_attack:
                        pass
                    elif event.key == Commands.p2_dispatch_archer_attack:
                        pass
                    elif event.key == Commands.p2_dispatch_unleash_all:
                        pass


        for w in player1.worker_list:
            if w.ON_SCREEN:
                screen.blit(worker1, w.WORKER_POS)

        for w in player2.worker_list:
            if w.ON_SCREEN:
                screen.blit(worker2, w.WORKER_POS)

        for s in player1.swordsman_list:
            if s.ON_SCREEN:
                screen.blit(swordsman1, swordsman1_at_enemy_pos)

        for s in player2.swordsman_list:
            if s.ON_SCREEN:
                screen.blit(swordsman2, swordsman2_at_enemy_pos)

        for a in player1.archer_list:
            if a.ON_SCREEN:
                screen.blit(archer1, archer1_on_tower_pos)

        for a in player2.archer_list:
            if a.ON_SCREEN:
                screen.blit(archer2, archer2_on_tower_pos)


        pygame.display.update()


