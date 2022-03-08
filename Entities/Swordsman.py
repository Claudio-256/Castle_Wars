
class Swordsman:
    SWORDSMAN_COST = 6

    def __init__(self):
        self.SWORDSMAN_COST = 6
        self.SWORDSMAN_TRAIN = 2 * self.SWORDSMAN_COST
        self.SWORDSMAN_RANGE = 10
        self.SWORDSMAN_HIT = 5
        self.SWORDSMAN_REST = 1
        self.SWORDSMAN_HEALTH = 10
        self.SWORDSMAN_SPEED = 1
        self.SWORDSMAN_POS = None
        self.ON_SCREEN = False