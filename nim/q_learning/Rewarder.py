from q_learning.Rewards import Rewards
import numpy as np

class Rewarder():
    def __init__(self, pearlsPerRow):
        self.pearlsPerRow = pearlsPerRow
        self.rewardInvalid = Rewards['Invalid']
        self.rewardWinning = Rewards['Winning']
        self.rewardLosing = Rewards['Losing']

        self.reset()

        print('Start creating Reward-Table')
        self.createRTable(pearlsPerRow, self.rewardInvalid, self.rewardLosing, self.rewardWinning)
        print('Finished creating Reward-Table')

    def reset(self):
        sumOfPearls = sum(self.pearlsPerRow)
        self.curState = pow(2, sumOfPearls) - 1

    def getCurState(self):
        return self.curState

    def step(self, curAction):
        reward = self.R[self.curState][curAction]
        done = False

        # Set next state if action is valid
        if reward == self.rewardInvalid:
            nextState = self.curState
        else:
            nextState = curAction

        # Check if done
        # No pearls left
        if nextState == 0:
            done = True
        # Winning state
        elif reward == self.rewardWinning:
            done = True
        # Loosing is not done -> so we can train for reaching winning state

        self.curState = nextState

        return nextState, reward, done

    def createRTable(self, rows, rewardInvalid, rewardLosing, rewardWinning):
        numOfStates = pow(2, sum(rows))

        self.R = np.zeros((numOfStates, numOfStates))

        # Determine invalid states, winning states and direct loosing states
        for curState in range(0, numOfStates):
            for nextState in range(0, numOfStates):
                # Determine the change
                change = curState ^ nextState

                # Check if nothing has changed
                if not change:
                    self.R[curState][nextState] = rewardInvalid
                    continue

                # Check if we added a pearl
                if change & nextState:
                    self.R[curState][nextState] = rewardInvalid
                    continue

                # Check if more than one row changed
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
                    self.R[curState][nextState] = rewardInvalid
                    continue

                # Check if next state is a winning state
                for i in range(0, sum(rows)):
                    winningState = pow(2, i)
                    if nextState == winningState:
                        self.R[curState][nextState] = rewardWinning
                        break

                # Check if we remove all pearls -> losing
                # TODO: Losing or invalid?
                if nextState == 0:
                    self.R[curState][nextState] = rewardInvalid
                    continue

        # Determine all losing states
        for curState in range(0, numOfStates):
            for nextState in range(0, numOfStates):
                # Check if the nextState is valid
                if self.R[curState][nextState] == rewardInvalid:
                    continue

                # Check if nextNextState is a winningState -> opponent can win
                if np.any(np.greater_equal(self.R[nextState], rewardWinning)):
                    self.R[curState][nextState] = rewardLosing
