from nim.player.Player import Player
from nim.logic.State import State
from nim.PlayerDict import PERFECT_KI_PLAYER

class PerfectPlayer(Player):

    def __init__(self, player_name):
        super(PerfectPlayer, self).__init__(PERFECT_KI_PLAYER, player_name)

    def step(self, actual_state: State):

        raise NotImplementedError

    def get_current_state(self):

        raise NotImplementedError