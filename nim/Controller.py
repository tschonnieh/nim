from logic.GameLogic import GameLogic
from logic.State import State
from player.Player import Player


class Controller:
    """
    This class controls the game flow
    """

    def __init__(self):
        self.game_over = False

    def init_game(self, actual_state: State, player_1: Player, player_2: Player):
        """
        Initializing the game
        :param actual_state: The initial game state
        :param player_1: The first player (Has the first turn)
        :param player_2: The second player (Has the second turn)
        :return: None
        """
        self.state = actual_state
        self.players = [player_1, player_2]
        self.cur_player_id = 0

    def get_current_player(self):
        """
        Returns the player, who makes the next turn
        :return: The player, who makes the next turn
        """
        return self.players[self.cur_player_id]

    def make_step(self):
        """
        The current player makes a step.
        :return: A triple in the following shape:
            (player_which_made_the_turn: Player, state_after_the_step: Step, has_won: Bool)
        """
        cur_player = self.get_current_player()
        next_state = cur_player.step(self.state)
        has_won = GameLogic.has_won(next_state)

        self.state = next_state

        if has_won:
            self.game_over = True

        self.cur_player_id = (self.cur_player_id + 1) % 2
        return (cur_player, next_state, has_won)

    def run_to_end(self, actual_state: State, player_1: Player, player_2: Player):
        has_won = GameLogic.has_won(actual_state)
        while (not has_won):
            next_state = player_1.step(actual_state)
            has_won = GameLogic.has_won(next_state)
            """ TODO: send player, next_state and has_won to ui """

            if (not has_won):
                next_state = player_2.step(next_state)
                has_won = GameLogic.has_won(next_state)
                """ TODO: send player, next_state and has_won to ui """

            actual_state = next_state

