from logic.State import State
from player.PlayerDict import PlayerType


class Player:
    """
    Player is an interface for all possible players (see PlayerDict)
    To implement the interface use:
        class MyPlayer(Player):
    """

    def __init__(self, player_type: PlayerType, player_name):
        self.PlayerType = player_type
        self.name = player_name

    def step(self, actual_state: State):
        """
        returns the next valid state
        """
        raise NotImplementedError
