class FileManager:
    TURN = None  # current turn
    RESOURCES = None  # n. of resources
    WALL_HEALTH = None
    WORKER_POS = None  # barracks, wall, or mine
    SWORDSMAN_POS = None  # x coord
    SWORDSMAN_HEALTH = None
    ARCHER_POS = None  # x coord
    ARCHER_HEALTH = None
    ARCHER_ARROW_POS = None  # only x coordinate is needed, arrows travel horizontally
    TOWER_ARROW_POS = (None, None)  # coords (x, y)

    '''Example:
    START Game
    TURN 4322
    END Game
    
    START Player1
    WALL 1000
    END Player1
    
    START Player2
    WALL 892
    ARCHER POS 126 HEALTH 20
    TOWER_ARROW 800 32
    END Player2
    '''

    #todo functions to save and load from text files
