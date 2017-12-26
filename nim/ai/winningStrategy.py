import numpy as np

def calc_col_sum(binNimArray):
    """ calculate the sum for each column and return the sum row """
    sumRow = []
    binNimArray = np.array(binNimArray)
    transposedArray = binNimArray.transpose()
    for x in transposedArray:
        sumRow.append(sum(x))
    return sumRow

def is_winning_state(sumRow):
    """ check if the representation of the sum row is a winning state or not """
    if sum(sumRow) % 2 == 0:
        return True
    else:
        return False