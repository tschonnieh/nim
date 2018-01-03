import numpy as np
import random
import os
import sys

class QLearner():
    def __init__(self):
        pass

    @classmethod
    def empty(cls, stateNum, actionNum):
        qLearner = cls()
        qLearner.stateNum = stateNum
        qLearner.actionNum = actionNum
        qLearner.qTable = np.zeros((stateNum, actionNum))

        # TODO: Weg?
        qLearner.gamma = 0.8
        qLearner.epsilon = 1.0 # Exploration Factor
        qLearner.learning = False
        qLearner.rewardCallback = None

        return qLearner

    @classmethod
    def fromSaveFile(cls, pathToFile):
        qLearner = cls()
        qLearner.loadQTable(pathToFile)

        return qLearner

    def step(self, curState):
        return np.argmax(self.qTable[curState])

    def learnStep(self, envCallback, gamma, epsilon, curState):
        # Exploration vs Exploitation
        r = random.random()

        if r <= epsilon:
            # Exploration -> Pick a random action
            nextAction = random.randrange(self.actionNum)
        else:
            # Exploitation -> Find max in q table to determine next action
            nextAction = np.argmax(self.qTable[curState])

        # Test if action is possible, which reward is granted and which state will be next
        # TODO: Call to environment
        reward, nextState = envCallback(curState, nextAction)

        # Update Q-Table
        nextNextState = np.max(self.qTable[nextState])
        self.qTable[curState][nextAction] = reward + self.gamma * nextNextState

    def saveQTable(self, pathToSavefile):
        if os.path.exists(pathToSavefile):
            # TODO: Ask if overwrite?
            print('Savefile: ' + str(pathToSavefile) + ' already exists -> File not saved')
        else:
            np.save(pathToSavefile, self.qTable)
            print('Saved Q-Table to ' + str(pathToSavefile))

    def loadQTable(self, pathToFile):
        if os.path.exists(pathToFile):
            self.qTable = np.load(pathToFile)
            print('Loaded Q-Table from ' + str(pathToFile))
        else:
            print('File ' +  str(pathToFile) + ' not found -> Terminate program')
            sys.exit(0)
