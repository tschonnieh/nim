from Controller import Controller
from ai.perfectPlayer import PerfectPlayer
from ai.randomPlayer import RandomPlayer
from logic.State import State


def print_turn(player, state, has_won):
    print("{}:\n\t{} - has_won: {}".format(player, state, has_won))


if __name__ == '__main__':

    print("Testing --> 'controller.run_to_end()'")
    contoller = Controller()
    init_state = State.get_start_state([3, 2, 1])
    p1 = PerfectPlayer("Player 1")
    p2 = PerfectPlayer("Player 2")

    print("Initializing controller:\n - {}\n - {}\n - {}".format(p1, p2, init_state))
    contoller.init_game(init_state, p1, p2)
    contoller.run_to_end(print_turn)
    print("\n")

    print("Testing --> 'controller.step()'")
    contoller = Controller()
    init_state = State.get_start_state([3, 2, 1])
    p1 = RandomPlayer("Player 1")
    p2 = PerfectPlayer("Player 2")

    print("Initializing controller:\n - {}\n - {}\n - {}".format(p1, p2, init_state))
    contoller.init_game(init_state, p1, p2)
    while True:
        (player, state, has_won) = contoller.make_step()
        print_turn(player, state, has_won)
        if contoller.game_over:
            print("Breaking because game over")
            break
