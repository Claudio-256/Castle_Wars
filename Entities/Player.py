from Entities.Castle import Castle
import Entities.Mine as M
import Entities.Barrack as B
import Entities.Tower as T
import Entities.Wall as Wall


class Player:
    def __init__(self):
        self.castle = Castle()
        self.mine = M.Mine()
        self.barrack = B.Barrack()
        self.tower = T.Tower()
        self.wall = Wall.Wall()

        self.swordsman_list = []
        self.archer_list = []
        self.worker_list = []
