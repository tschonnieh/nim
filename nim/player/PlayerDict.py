
class PlayerType:
    """
    Represents a type of player, which can play the nim game
    """
    def __init__(self, id, name, description):
        """
        Constructor of a player type
        :param id: A unique integer id for the player type
        :param name: A string name for the player type
        :param desc_text: A text, which describes the player type
        """
        self.id = id
        self.name = name
        self.description = description


MANUAL_PLAYER = PlayerType(0, "Manual Player", "A person, which is manually playing")
RANDOM_KI_PLAYER = PlayerType(1, "Random KI", "A KI playing with random actions")
QLEARN_KI_PLAYER = PlayerType(2, "Q-Learning", "A KI using the Q-Learning algorithm for learning")
PERFECT_KI_PLAYER = PlayerType(3, "Perfect Player (Logic)",
                               "A KI, which always makes the best possible action. The KI uses a mathematical model")

ALL_PLAYERS = [MANUAL_PLAYER, RANDOM_KI_PLAYER, QLEARN_KI_PLAYER, PERFECT_KI_PLAYER]