from player.Player import Player
from player.PlayerDict import QLEARN_KI_PLAYER
from logic.State import State
from q_learning.QLearner import QLearner

class QPlayer(Player):
    def __init__(self, player_name):
        super(QPlayer, self).__init__(QLEARN_KI_PLAYER, player_name)

        # TODO: Get Information which file to load
        self.qLogic = QLearner.fromSaveFile('test.npy')

    @classmethod
    def qPlayerFromQTable(cls, player_name, qTable):
        qPlayer = cls(player_name)
        qPlayer.qLogic.qTable = qTable
        return qPlayer

    def step(self, gameState):
        # Get information for unflatening
        perlsPerRow = gameState.get_structure()
        flatState = gameState.to_flat_representation()

        nextFlatState = self.qLogic.step(flatState)

        return State.from_flat_representation(perlsPerRow, nextFlatState)
