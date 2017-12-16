from nim.player.Player import Player
from nim.logic.State import State
from nim.logic.GameLogic import GameLogic


class Controller:

    @staticmethod
    def start_game(actual_state : State, player_1 : Player, player_2 : Player):
        has_won = GameLogic.has_won(actual_state)
        while(not has_won):
            next_state = player_1.step(actual_state)
            has_won = GameLogic.has_won(next_state)
            """ TODO: send player, next_state and has_won to ui """
            
            if(not has_won):
                next_state = player_2.step(next_state)
                has_won = GameLogic.has_won(next_state)
                """ TODO: send player, next_state and has_won to ui """
            
            actual_state = next_state

        