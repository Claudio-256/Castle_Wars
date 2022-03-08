import pygame

class Commands:
    #train
    p1_train_worker = pygame.K_q
    p1_train_swordsman = pygame.K_w
    p1_train_archer = pygame.K_e

    p2_train_worker = pygame.K_p
    p2_train_swordsman = pygame.K_o
    p2_train_archer = pygame.K_i


    #dispatch
    p1_dispatch_worker_mine = pygame.K_a
    p1_dispatch_worker_wall = pygame.K_s
    p1_dispatch_swordsman_attack = pygame.K_d
    p1_dispatch_archer_attack = pygame.K_f
    p1_dispatch_unleash_all = pygame.K_z

    p2_dispatch_worker_mine = pygame.K_l
    p2_dispatch_worker_wall = pygame.K_k
    p2_dispatch_swordsman_attack = pygame.K_j
    p2_dispatch_archer_attack = pygame.K_h
    p2_dispatch_unleash_all = pygame.K_m


    #save and load
    #todo define keys for save&load