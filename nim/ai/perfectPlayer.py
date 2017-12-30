from nim.player.Player import Player
from nim.logic.State import State
from nim.PlayerDict import PERFECT_KI_PLAYER
import numpy as np

test_nim_array = ([1.0, 0.0, 1.0], [1.0, 0.0], [0.0])
test_state = State(test_nim_array)

class PerfectPlayer(Player):

    def __init__(self, player_name):
        super(PerfectPlayer, self).__init__(PERFECT_KI_PLAYER, player_name)

    def step(self, actual_state: State):

        raise NotImplementedError

    def is_winning_state(self, actual_state : State):
        """
        check, if the actual state is a winning state or not
        :param actual_state: actual state as a list of rows which contain float ones or float zeros
        :return: returns True, if it is a winning state and False, if it is not
        """
        sumRow = []
        binNimArray = np.array(actual_state.to_binary_representation())
        transposedArray = binNimArray.transpose()
        for x in transposedArray:
            sumRow.append(sum(x))
        if sum(sumRow) % 2 == 0:
            return True
        else:
            return False