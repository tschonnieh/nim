from logic.State import State
import numpy as np

class GameLogic:

    @staticmethod
    def has_won(actual_state : State):
        for row in actual_state.Rows:
            for pearl in row:
                if(pearl == 1):
                    return False
        
        return True

    @staticmethod
    def is_valid(old_state : State, actual_state : State):
        decrease = False
        for i in range(0, len(old_state.Rows)):
            nr_of_pearls_old = np.sum(old_state.Rows[i])
            nr_of_pearls_actual = np.sum(actual_state.Rows[i])
            
            if(nr_of_pearls_actual < nr_of_pearls_old):
                if(not decrease):
                    decrease = True
                else:
                    return False
            if(nr_of_pearls_actual > nr_of_pearls_old):
                return False

        if(decrease):
            return True

        return False



        