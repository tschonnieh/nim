from PlayerDict import MANUAL_PLAYER
from logic.State import State
from player.Player import Player


class ManualPlayer(Player):

    def __init__(self, player_name):
        super(ManualPlayer, self).__init__(MANUAL_PLAYER, player_name)

    def set_state(self, new_state):
        """
        Sets the state for the manual player.
        This state will be returned by 'self.step(...)'
        :param new_state: The new state for the player
        :return: None
        """
        self.new_state = new_state

    def step(self, actual_state: State):
        """
        returns the next valid state
        """
        return self.new_state