from logic.GameLogic import GameLogic
from logic.State import State
from player.Player import Player


class Controller:

    def __init__(self):
        pass

    def init_game(self, actual_state: State, player_1: Player, player_2: Player):
        self.state = actual_state
        self.players = [player_1, player_2]
        self.cur_player_id = 0

    def get_current_player(self):
        return self.players[self.cur_player_id]

    def make_step(self):
        cur_player = self.get_current_player()
        next_state = cur_player.step(self.state)
        has_won = GameLogic.has_won(next_state)
        self.cur_player_id = (self.cur_player_id + 1) % 2
        return (cur_player, next_state, has_won)

    def run_to_end(self, actual_state: State, player_1: Player, player_2: Player):
        has_won = GameLogic.has_won(actual_state)
        while (not has_won):
            next_state = player_1.step(actual_state)
            has_won = GameLogic.has_won(next_state)
            """ TODO: send player, next_state and has_won to ui """
            self.after_step_event(player_1, next_state, has_won)

            if (not has_won):
                next_state = player_2.step(next_state)
                has_won = GameLogic.has_won(next_state)
                """ TODO: send player, next_state and has_won to ui """
                self.after_step_event(player_2, next_state, has_won)

            actual_state = next_state

