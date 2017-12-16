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

    def to_binary_representation(self):
        """
        returns the binary state of the given state
        """
        nr_of_pearls_per_row = []
        for row in self.Rows:
            nr_of_pearls_per_row.append(np.sum(row))

        max_nr_of_pearls = max(nr_of_pearls_per_row)
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







