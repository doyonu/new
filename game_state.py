from enum import Enum

class GameState(Enum):
    NOT_STARTED = 0
    ROUND_PLAYER = 1
    ROUND_ENNEMY = 2
    ROUND_DONE = 3
    GAME_OVER = 4