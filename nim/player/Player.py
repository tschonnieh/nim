from nim.PlayerDict import PlayerType
from nim.logic.State import State

class Player:
    """
    Player is an interface for all possible players (see PlayerDict)
    To implement the interface use:
        class MyPlayer(Player):
    """

    def __init__(self, player_type : PlayerType):
        self.PlayerType = player_type

    def step(self, actual_state : State):
        """
        returns the next valid state
        """
        raise NotImplementedError