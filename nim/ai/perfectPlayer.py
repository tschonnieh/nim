from player.Player import Player
from logic.State import State
from PlayerDict import PERFECT_KI_PLAYER
import numpy as np
from random import randint
import copy

#test_nim_array = ([0, 0, 0], [1.0, 1.0, 0], [0, 0, 0])
#test_state = State(test_nim_array)

class PerfectPlayer(Player):

    def __init__(self, player_name):
        super(PerfectPlayer, self).__init__(PERFECT_KI_PLAYER, player_name)

    def step(self, actual_state: State):
        """
        if actual state is a winning state => make next best possible move
        if actual state is NOT a winning state => make next perfect move
        :param actual_state: actual state as a list of rows which contain float ones or float zeros
        :return: returns the next state
        """
        if (not self.is_winning_state(actual_state)):
            next_state = self.get_next_perfect_state(actual_state)
            return next_state
        else:
            next_state = self.get_next_best_possible_state(actual_state)
            return next_state

    def get_next_best_possible_state(self, actual_state : State):
        """
        if the actual state is a winning state, then pick only one pearl of a random row
        :param actual_state: actual state as a list of rows which contain float ones or float zeros
        :return: returns the next state which is NOT a winning state but the best next possible state
        """
        rand_row = self.pick_random_row(actual_state)
        idx_list = self.get_idx_list_of_ones(actual_state.Rows[rand_row])
        actual_state.toggle_pearl(rand_row, idx_list[0])
        next_state = actual_state
        #print(next_state.Rows)
        return next_state

    def pick_random_row(self, actual_state : State):
        """
        pick a random row of the actual state which contains at least one pearl
        :param actual_state: actual state as a list of rows which contain float ones or float zeros
        :return: returns the row as a number
        """
        nim_array = actual_state.Rows
        rand_row = randint(0, len(nim_array) - 1)
        """ if the random picked row contains only zeros, pick another row """
        sum_of_pearls = sum(nim_array[rand_row])
        while (sum_of_pearls == 0):
            rand_row = randint(0, len(nim_array) - 1)
            sum_of_pearls = sum(nim_array[rand_row])
        return rand_row


    def get_next_perfect_state(self, actual_state : State):
        """
        change the actual state to a winning state
        :param actual_state: actual state as a list of rows which contain float ones or float zeros
        :return: returns the next perfect state which is a winning state
        """
        nim_array = actual_state.Rows
        for row_id, row in enumerate(nim_array):
            next_state = copy.deepcopy(actual_state)
            idx_list = self.get_idx_list_of_ones(row)
            for idx in idx_list:
                next_state.toggle_pearl(row_id, idx)
                if(self.is_winning_state(next_state)):
                    #print(next_state.Rows)
                    return next_state
        print("no perfect move possible")
        return actual_state


    def get_idx_list_of_ones(self, row):
        """
        find the index of each one in the row
        :param row: the random picked row
        :return: returns a list of indices for each one in the row
        """
        idx_of_ones = []
        for idx, val in enumerate(row):
            if (val == 1):
                idx_of_ones.append(idx)
        return idx_of_ones

    def is_winning_state(self, actual_state : State):
        """
        check, if the actual state is a winning state or not
        :param actual_state: actual state as a list of rows which contain float ones or float zeros
        :return: returns True, if it is a winning state and False, if it is not
        """
        bin_state = actual_state.to_binary_representation()
        binNimArray = np.array(bin_state.Rows)
        sumRow = np.sum(binNimArray, axis=0)
        check = 0
        for val in sumRow:
            if(val != 0):
                if(val % 2 != 0 and sum(sumRow) == 1 and sumRow[-1] == 1):
                    continue
                else:
                    check += val % 2
        if check == 0:
            return True
        else:
            return False