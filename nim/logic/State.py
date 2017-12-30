import numpy as np
from typing import List

class State:

    def __init__(self, rows : List):
        """
        Constructor of a State
        :param rows: the pearl rows as np.array with 1's and 0's
        """
        self.Rows = rows

    @staticmethod
    def get_start_state(nr_of_pearls_per_row : List):
        """
        returns a state to start the game
        """
        rows = []
        for nr_of_perls in nr_of_pearls_per_row:
            rows.append(np.ones(nr_of_perls))

        return State(rows)

    def __eq__(self, other_state):
        """
        Checks if to states are the same (contains the same state information)
        :param other_state: The other state to compare with
        :return: True, if the 'other_state' has the same state than this state. Otherwise False
        """
        for (row_id, row) in enumerate(self.Rows):
            if not np.array_equal(row, other_state.Rows[row_id]):
                return False
        return True

    def toggle_pearl(self, row_id, col_id):
        """
        Toggles the status of a single pearl in the state
        :param row_id: The row number of the pearl to toggle
        :param col_id: The column number of the pearl to toggle
        :return:
        """
        if self.Rows[row_id][col_id] == 0:
            self.Rows[row_id][col_id] = 1
        else:
            self.Rows[row_id][col_id] = 0

    def to_binary_representation(self):
        """
        returns the binary state of the given state
        """
        nr_of_pearls_per_row = []
        for row in self.Rows:
            nr_of_pearls_per_row.append(int(np.sum(row)))

        max_nr_of_pearls = int(max(nr_of_pearls_per_row))
        max_length_of_binary = len("{0:b}".format(max_nr_of_pearls))

        binary_rows = []
        for nr_of_pearls in nr_of_pearls_per_row:
            binary = "{0:b}".format(nr_of_pearls)
            binary_row = np.array([])
            for i in range(0, max_length_of_binary - len(binary)):
                binary_row = np.append(binary_row, 0)
            for i in range(0, len(binary)):
                binary_row = np.append(binary_row, int(binary[i]))
            binary_rows.append(binary_row)

        return State(binary_rows)







