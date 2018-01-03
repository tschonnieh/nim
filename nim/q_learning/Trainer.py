from q_learning.QLearner import QLearner
from q_learning.Rewarder import Rewarder
from logic.State import State

import numpy as np
import datetime

class Trainer():
    def __init__(self, pearlsPerRow):
        self.pearlsPerRow = pearlsPerRow

        # Determine number of states and actions

        # TODO: Self nur für count Zero elements -> evtl in QLearner Function dafür bereitstellen
        self.numOfStates = pow(2, sum(rows))
        self.numOfActions = pow(2, sum(rows))

        # Initialize qLearner
        self.qLearn = QLearner.empty(self.numOfStates, self.numOfActions)

    def setEnv(self, env):
        self.env = env
        self.env.reset()

    def trainEpisode(self, gamma, epsilon):
        self.env.reset()

        self.trainEpisodeDone = False
        # TODO: Is this clever or better not as self but local?
        self.curState = self.env.getCurState()
        self.trainEpisodeDone = False

        while not self.trainEpisodeDone:
            self.qLearn.learnStep(self.envCallback, gamma, epsilon, self.curState)

    def trainEpoch(self, gamma, epsilon, episodesPerEpoch):
        for e in range(0, episodesPerEpoch):
            self.trainEpisode(gamma, epsilon)

    def trainEpochs(self, gamma, startEpsilon, episodesPerEpoch, epochs):
        epsilon = startEpsilon
        epsilonDecrement = 1.0 / epochs

        for e in range(0, epochs):
            self.trainEpoch(gamma, epsilon, episodesPerEpoch)

            print(str(e+1) + ' / ' + str(epochs) + ' Epochs')
            print('Number of zero Elements: ' + str(self.numOfStates * self.numOfActions - np.count_nonzero(self.qLearn.qTable)))

            epsilon -= epsilonDecrement

    def envCallback(self, curState, action):
        nextState, reward, done = self.env.step(action)

        self.trainEpisodeDone = done
        self.curState = nextState

        return reward, nextState

    def startTraining(self):
        startTime = datetime.datetime.now()

        self.trainEpochs(0.8, 1.0, 200, 500)

        endTime = datetime.datetime.now()
        print(endTime - startTime)

        # Save q Table
        print(self.qLearn.qTable)
        self.qLearn.saveQTable('test.npy')

# Define size of game field
rows = [3, 3, 3]

# Initialize rewarder and create reward table
rewarder = Rewarder(rows)

tr = Trainer(rows)
tr.setEnv(rewarder)
tr.startTraining()
