from player.Player import Player
from player.PlayerDict import QLEARN_KI_PLAYER
from logic.State import State
from q_learning.QLearner import QLearner
from q_learning.SaveFileManager import SaveFileManager

class QPlayer(Player):
    def __init__(self, player_name):
        super(QPlayer, self).__init__(QLEARN_KI_PLAYER, player_name)
        self.qLogic = QLearner()

    @classmethod
    def qPlayerFromQTable(cls, player_name, qTable):
        qPlayer = cls(player_name)
        qPlayer.qLogic.qTable = qTable
        return qPlayer

    @classmethod
    def qPlayer_from_savefile(cls, player_name, pearlsPerRow):
        if SaveFileManager.has_savefile_for_size(pearlsPerRow):
            filePath = SaveFileManager.get_path_of_savefile_for_size(pearlsPerRow)
            qTable = QLearner.fromSaveFile(filePath)
            return QPlayer.qPlayerFromQTable(player_name, qTable)
        else:
            raise RuntimeError('No saveFile for the specified size')

    @staticmethod
    def has_savefile_for_size(pearlsPerRow):
        return SaveFileManager.has_savefile_for_size(pearlsPerRow)

    def step(self, gameState):
        # Get information for unflatening
        perlsPerRow = gameState.get_structure()
        flatState = gameState.to_flat_representation()

        nextFlatState = self.qLogic.step(flatState)

        return State.from_flat_representation(perlsPerRow, nextFlatState)

#a = QPlayer.has_savefile_for_size([3,2,2])
#b = QPlayer.qPlayer_from_savefile('Blub', [3,2,2])
#pass