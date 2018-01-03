from player.Player import Player
from logic.State import State
from PlayerDict import RANDOM_KI_PLAYER
from random import randint

#test_nim_array = ([1.0, 0.0, 1.0], [1.0, 0.0], [0.0])
#test_state = State(test_nim_array)

class RandomPlayer(Player):

    def __init__(self, player_name):
        super(RandomPlayer, self).__init__(RANDOM_KI_PLAYER, player_name)

    def step(self, actual_state : State):
        """
        toggle random pearls of the actual given state (only in one row, so the step is valid)
        :param actual_state: actual state as a list of rows which contain float ones or float zeros
        :return: returns next state
        """
        next_state = actual_state
        idx_list = self.pick_random_pearls(next_state)
        for i, idx in enumerate(idx_list):
            next_state.toggle_pearl(idx[0], idx[1])
        return next_state

    def pick_random_pearls(self, actual_state : State):
        """
        pick random row which contains at least one pearl and pick a random amount of pearls in this row
        :param actual_state: actual state as a list of rows which contain float ones or float zeros
        :return: returns a list which contains the indices of the random picked pearls
        """
        return_idx_list = []
        nim_array = actual_state.Rows
        rand_row = randint(0, len(nim_array) - 1)
        """ if the random picked row contains only zeros, pick another row """
        sum_of_pearls = sum(nim_array[rand_row])
        while(sum_of_pearls == 0):
            rand_row = randint(0, len(nim_array) - 1)
            sum_of_pearls = sum(nim_array[rand_row])

        """ random amount of pearls which will be picked in next step """
        rand_amount_of_pearls = randint(1, sum_of_pearls)

        idx_list = self.get_idx_list_of_ones(nim_array[rand_row])
        """ write indices of randomly picked pearls in return list """
        for i in range(0, rand_amount_of_pearls):
            return_idx_list.append([rand_row, idx_list[i]])
        return return_idx_list

    def get_idx_list_of_ones(self, row):
        """
        find the index of each one in the row
        :param row: the random picked row
        :return: returns a list of indices for each one in the row
        """
        idx_of_ones = []
        for idx, val in enumerate(row):
            if(val == 1):
                idx_of_ones.append(idx)
        return idx_of_ones