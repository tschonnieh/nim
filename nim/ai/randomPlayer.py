from nim.player import Player
from nim.logic import State
from nim.PlayerDict import RANDOM_KI_PLAYER

class RandomPlayer(Player):

    def __init__(self, player_name):
        super(RandomPlayer, self).__init__(RANDOM_KI_PLAYER, player_name)

    def step(self, actual_state: State):

        raise NotImplementedError

    def get_current_state(self):

        raise NotImplementedError