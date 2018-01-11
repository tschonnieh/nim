from typing import List

from ai.perfectPlayer import PerfectPlayer
from ai.randomPlayer import RandomPlayer
from player.ManualPlayer import ManualPlayer
from player.PlayerDict import MANUAL_PLAYER, RANDOM_KI_PLAYER, PERFECT_KI_PLAYER, QLEARN_KI_PLAYER
from q_learning.QPlayer import QPlayer


def create_player_by_type_id(player_type_id: int, player_name: str, gamesize: List):
    """
    Creates a Player object by a given player type id
    :param gamesize: The gamesize e.G. [3, 3, 3] for 3 rows with 3 pearls
    :param player_type_id: The id of the player type to create
    :param player_name: The name of the player e.g. 'Player 1' or 'Hans'
    :return:
    """
    if player_type_id == MANUAL_PLAYER.id:
        return ManualPlayer(player_name)

    elif player_type_id == RANDOM_KI_PLAYER.id:
        return RandomPlayer(player_name)

    elif player_type_id == PERFECT_KI_PLAYER.id:
        return PerfectPlayer(player_name)

    elif player_type_id == QLEARN_KI_PLAYER.id:

        # Check if game can create a QPlayer for that gamesize
        if not QPlayer.has_savefile_for_size(gamesize):
            raise Exception("Can't create QPlayer, because no pretrained QMatrix exists.")

        return QPlayer.qPlayer_from_savefile(player_name, gamesize)

    else:
        raise Exception("Invalid player_type_id: '{}'".format(player_type_id))