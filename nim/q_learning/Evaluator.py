import ai.perfectPlayer
from q_learning.QPlayer import QPlayer
import logic.State

DEBUG = False

class Evaluator():
    def __init__(self, perlsPerRow, qLearner):
        self.perlsPerRow = perlsPerRow
        self.numOfStates = pow(2, sum(self.perlsPerRow))

        self.qPlayer = QPlayer.qPlayerFromQTable('QPlayer', qLearner.qTable)
        self.perfectPlayer = ai.perfectPlayer.PerfectPlayer("PerfectPlayer")

    def playFromStartState(self, startState, qStarting):
        curState = startState
        curState = logic.State.State.from_flat_representation(self.perlsPerRow, curState)

        qsTurn = qStarting
        running = 1

        while running:
            # Step for both
            if qsTurn:
                i = curState.to_flat_representation()
                curState = self.qPlayer.step(curState)
                j = curState.to_flat_representation()

                # Check if that was valid
                change = i ^ j
                changeInRows = 0
                idx = 0

                for perlsPerRow in self.perlsPerRow:
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
                    #raise RuntimeError("Q-Learning invalid move!!!")
                    # lose
                    curState = logic.State.State.from_flat_representation(self.perlsPerRow, 3)

                qsTurn = 0

            else:
                curState = self.perfectPlayer.step(curState)

                qsTurn = 1

            # Check if won
            curQState = curState.to_flat_representation()
            for i in range(0, sum(self.perlsPerRow)):
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

    def evaluate(self):
        # Count wins and losses for each start state and each player starting
        ppWin = 0
        qlWin = 0
        ppZeroByPp = 0
        ppZeroByQl = 0
        qlZeroByPp = 0
        qlZeroByQl = 0
        ppLost = 0
        qlLost = 0

        lostStartStates = []

        # Start from each state and check who wins
        for startState in range(1, self.numOfStates):
            ret = self.playFromStartState(startState, 0)
            if ret == 1:
                ppWin += 1 # [3, 3, 3] -> Unavoidable wins: 27
            elif ret == -1:
                ppZeroByPp += 1
            elif ret == 0:
                ppLost += 1
            elif ret == -2:
                ppZeroByQl += 1
            retPp = ret

            ret = self.playFromStartState(startState, 1)
            if ret == 0:
                qlWin += 1
            elif ret == -1:
                qlZeroByPp += 1
            elif ret == 1:
                qlLost += 1
            elif ret == -2:
                qlZeroByQl += 1
            retQl = ret

            if (retPp == 1 and retQl == 1):
                lostStartStates.append(startState)

        if DEBUG:
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
            print('---------------------------------')
            print('Lost in start states: ' + str(len(lostStartStates)))
            print('Lost in start states: ' + str(lostStartStates))

        return len(lostStartStates)
