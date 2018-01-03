from PlayerDict import MANUAL_PLAYER
from logic.State import State
from player.Player import Player


class ManualPlayer(Player):

    def __init__(self, player_name):
        super(ManualPlayer, self).__init__(MANUAL_PLAYER, player_name)

    def step(self, actual_state: State):
        """
        returns the next valid state
        """
        raise NotImplementedError