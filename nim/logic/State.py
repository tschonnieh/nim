import numpy as np
from typing import List

class State:

    def __init__(self, rows : List):
        """
        rows are a list of np.array 
        """
        self.Rows = rows

    @staticmethod
    def get_start_state(nr_of_pearls_per_row : List):
        rows = []
        for nr_of_perls in nr_of_pearls_per_row:
            rows.append(np.ones(nr_of_perls))

        return State(rows)





