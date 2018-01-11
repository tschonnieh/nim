import numpy as np
import random
import os
from q_learning.Rewards import Rewards

class QLearner():
    def __init__(self):
        pass

    @classmethod
    def empty(cls, numberOfStates, numberOfActions):
        qLearner = cls()
        qLearner.numberOfStates = numberOfStates
        qLearner.numberOfActions = numberOfActions
        qLearner.qTable = np.zeros((numberOfStates, numberOfActions), np.float16)

        qLearner.gamma = 0.8
        qLearner.epsilon = 1.0 # Exploration Factor
        qLearner.learningRate = 0.1

        return qLearner

    @classmethod
    def fromSaveFile(cls, pathToFile):
        qLearner = cls()
        qLearner.loadQTable(pathToFile)

        return qLearner

    def step(self, curState):
        return np.argmax(self.qTable[curState])

    def setParameter(self, parameter, value):
        if hasattr(self, parameter):
            setattr(self, parameter, value)
        else:
            print("No parameter named: " + parameter)

    def learnStep(self, curState):
        # Exploration vs Exploitation
        r = random.random()
        if r <= self.epsilon:
            # Exploration -> Pick a random, possible action
            # action = random.randrange(numOfStates)

            # First we try to find the state action pairs we have not tried yet
            # Check if there are actions we have not tried yet
            unknownActions = np.argwhere(self.qTable[curState] == 0.0)
            if len(unknownActions) > 0:
                action = np.random.choice(unknownActions[:, 0])
            # Else we choice a valid action
            else:
                validActions = np.argwhere(self.qTable[curState] > Rewards['Invalid'])
                action = np.random.choice(validActions[:, 0])
        else:
            # Exploitation -> Find max in q table to determine next action
            action = np.argmax(self.qTable[curState])

        return action

    def updateQ(self, startState, action, finalState):
        reward = 0 # Rewards are only provided through immediateReward
        oldQ = self.qTable[startState][action]
        maxQNewState = np.max(self.qTable[finalState])
        self.qTable[startState][action] = oldQ + self.learningRate * (reward + self.gamma * maxQNewState - oldQ)

    def immediateReward(self, startState, action, reward):
        self.qTable[startState][action] = reward

    def getNumberOfUnknownActions(self):
        return self.numberOfStates * self.numberOfActions - np.count_nonzero(self.qTable)

    def saveQTable(self, pathToSavefile):
        if os.path.exists(pathToSavefile):
            print('Savefile: ' + str(pathToSavefile) + ' already exists')
            print('O: Overwrite K: Keep the old file')

            while True:
                c = input()
                c = c.lower()
                if c == 'o':
                    break
                elif c == 'k':
                    return

        np.save(pathToSavefile, self.qTable)
        print('Saved Q-Table to ' + str(pathToSavefile))

    def loadQTable(self, pathToFile):
        if os.path.exists(pathToFile):
            self.qTable = np.load(pathToFile)
            print('Loaded Q-Table from ' + str(pathToFile))
        else:
            raise RuntimeError(str(pathToFile) + ' not found')
