from q_learning.QLearner import QLearner
from q_learning.Rewarder import Rewarder
from logic.State import State
from ai.randomPlayer import RandomPlayer
from q_learning.Evaluator import Evaluator

import numpy as np
import datetime
import random

class Trainer():
    def __init__(self, pearlsPerRow):
        self.pearlsPerRow = pearlsPerRow
        self.numOfStates = pow(2, sum(rows))
        self.numOfActions = pow(2, sum(rows))

        # Initialize qLearner
        self.qLearn = QLearner.empty(self.numOfStates, self.numOfActions)

        # For Training against AI -> best is randomPlayer
        self.secondPlayer = RandomPlayer("RandomPlayer")
        self.rewarder = Rewarder(pearlsPerRow)
        self.evaluator = Evaluator(pearlsPerRow, self.qLearn)

        self.episodesPerEpoch = 1000
        self.trainedEpisodes = 0

    def trainEpisode(self):
        curState = self.rewarder.getInitState()
        otherPlayerFirst = bool(random.getrandbits(1))
        done = False

        # Otherplayer first
        if otherPlayerFirst:
            curState = State.from_flat_representation(rows, curState)
            curState = self.secondPlayer.step(curState)
            curState = curState.to_flat_representation()

        while not done:
            qStartState = curState

            # Q-Learning
            if not done:
                while curState == qStartState:
                    curState = self.qLearn.learnStep(curState)

                    # Check if move was valid
                    # TODO: Environment
                    if self.rewarder.getReward(qStartState, curState) == self.rewarder.rewardInvalid or curState == 0:
                        self.qLearn.immediateReward(qStartState, curState, self.rewarder.rewardInvalid)
                        curState = qStartState

                qAction = curState

            # Check if Q-Learning won
            if self.rewarder.getReward(qStartState, curState) == self.rewarder.rewardWinning:
                done = True
                self.qLearn.immediateReward(qStartState, qAction, self.rewarder.rewardWinning)

            rStatState = curState
            # Other Player
            if not done:
                while rStatState == curState:
                    curState = State.from_flat_representation(rows, curState)
                    curState = self.secondPlayer.step(curState)
                    curState = curState.to_flat_representation()

                # TODO: No need to check if this player makes wrong states
                if self.rewarder.getReward(rStatState, curState) == self.rewarder.rewardInvalid or curState == 0:
                    curState = rStatState

            qFinalState = curState

            # Check if Other Player won
            if self.rewarder.getReward(rStatState, qFinalState) == self.rewarder.rewardWinning:
                done = True
                self.qLearn.immediateReward(qStartState, qAction, self.rewarder.rewardLosing)

            # Update Q-Table
            if not done:
                self.qLearn.updateQ(qStartState, qAction, qFinalState)

    def trainEpoch(self):
        # Group episodes to epochs -> only calculate performance stats after epoch -> saves time
        for e in range(0, self.episodesPerEpoch):
            self.trainEpisode()
            self.trainedEpisodes += 1

    def trainEpochs(self):
        # 2 Steps in training
        numberOfUnplayableActions = (sum(rows) + 1) * self.numOfStates # All winning states + no pearls left are states which will never require action
        numberOfUnknownActions = self.numOfStates * self.numOfStates # State action pairs we did not try yet

        # 1) Explore al state action pairs -> High Exploration Factor and Learning Rate
        print("Start exploration of unknown state-action-pairs")
        # TODO: Optimize Parameters
        self.qLearn.setParameter('gamma', 0.9)
        self.qLearn.setParameter('epsilon', 1.0)
        self.qLearn.setParameter('learningRate', 1.0)

        while numberOfUnknownActions > numberOfUnplayableActions:
            self.trainEpoch()
            numberOfUnknownActions = self.qLearn.getNumberOfUnknownActions()
            print("Unknown state-action-pairs: " + str( numberOfUnknownActions - numberOfUnplayableActions ))
        print("Finished exploration of unknown state-action-pairs")

        # 2) Find optimal solution -> Smaller Exploration Factor and Learning Rate
        print("Start optimization towards optimal strategy")
        numberOfLosingStates = self.numOfStates
        # TODO: Optimize Parameters
        self.qLearn.setParameter('gamma', 0.9)
        self.qLearn.setParameter('epsilon', 0.3)
        self.qLearn.setParameter('learningRate', 0.3)

        while numberOfLosingStates > 0:
            self.trainEpoch()
            numberOfLosingStates = self.evaluator.evaluate()
            print("Losing in " + str(numberOfLosingStates) + ' start states against a perfect player')
        print("Reached optimal strategy")

    def startTraining(self):
        startTime = datetime.datetime.now()
        print("Start training at: " + str(startTime) )

        self.trainEpochs()

        endTime = datetime.datetime.now()
        print("Finished training at: " + str(endTime))
        print("Duration: " + str(endTime - startTime) )
        print("Trained for " + str(self.trainedEpisodes) + " episodes")

        # TODO: Save qTable

# Define size of game field
rows = [3, 2, 2]

tr = Trainer(rows)

tr.startTraining()
np.save('test.npy', tr.qLearn.qTable)

# TODO: Function save file laden
# TODO: Größen definieren
# TODO: __main__