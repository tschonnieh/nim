import ai.perfectPlayer
import q_learning.QPlayer
import logic.State

def play(startState, qStarting):
    curState = startState
    curState = logic.State.State.from_flat_representation(rows, curState)

    qsTurn = qStarting
    running = 1

    while running:
        # Step for both
        if qsTurn:
            i = curState.to_flat_representation()
            curState = qPlayer.step(curState)
            j = curState.to_flat_representation()

            # Check if that was valid
            change = i ^ j
            changeInRows = 0
            idx = 0

            for perlsPerRow in rows:
                # Calc a mask to only select a single row
                rowMask = pow(2, perlsPerRow) - 1
                rowMask = rowMask << idx

                # Check if the current row had changes
                changePerRow = change & rowMask
                if changePerRow:
                    changeInRows += 1

                # Increase index to ignore the already processed rows
                idx += perlsPerRow

            if changeInRows > 1:
                raise RuntimeError("Q-Learning invalid move!!!")

            qsTurn = 0

        else:
            curState = perfectPlayer.step(curState)

            qsTurn = 1

        # Check if won
        curQState = curState.to_flat_representation()
        for i in range(0, sum(rows)):
            winningState = pow(2, i)
            if curQState == winningState:
                running = 0
                break
        if curQState == 0:
            if qsTurn:
                return -1   # Zero state caused by perfect player
            else:
                return -2   # Zero state caused by q-learning

    return qsTurn # Return 1 if perfect Player has won, 0 if qLearning has won, -1 if we reached state all pearls removed


perfectPlayer = ai.perfectPlayer.PerfectPlayer("PerfectPlayer")
qPlayer = q_learning.QPlayer.QPlayer("QPlayer")

rows = [5, 4, 3]
rows = [3, 3, 3]
numOfStates = pow(2, sum(rows))

# Count wins from perfect player if he starts
ppWin = 0
qlWin = 0
ppZeroByPp = 0
ppZeroByQl = 0
qlZeroByPp = 0
qlZeroByQl = 0
ppLost = 0
qlLost = 0

# Start from each state and check who wins
for startState in range(1, numOfStates):
    ret = play(startState, 0)
    if ret == 1:
        ppWin += 1 # [3, 3, 3] -> Unavoidable wins: 27
    elif ret == -1:
        ppZeroByPp += 1
    elif ret == 0:
        ppLost += 1
    elif ret == -2:
        ppZeroByQl += 1

    ret = play(startState, 1)
    if ret == 0:
        qlWin += 1
    elif ret == -1:
        qlZeroByPp += 1
    elif ret == 1:
        qlLost += 1
    elif ret == -2:
        qlZeroByQl += 1


print('Perfect Player starts')
print('\twins: ' + str(ppWin))
print('\tlost: ' + str(ppLost))
print('\tzeros by pp: ' + str(ppZeroByPp))
print('\tzeros by ql: ' + str(ppZeroByQl))
print('Q-Learning Player starts')
print('\twins: ' + str(qlWin))
print('\tlost: ' + str(qlLost))
print('\tzeros by pp: ' + str(qlZeroByPp))
print('\tzeros by ql: ' + str(qlZeroByQl))
