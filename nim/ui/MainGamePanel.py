from typing import List
import wx

from PlayerDict import ALL_PLAYERS
import ui.res.values.colors as col

from Controller import Controller
from logic.GameLogic import GameLogic
from logic.State import State
from player.ManualPlayer import ManualPlayer
from player.Player import Player


class MainGamePanel(wx.Panel):
    """
    The panel containing the main game.
    It shows multiple rows of pearls
    """

    def __init__(self, parent, **args):
        super(MainGamePanel, self).__init__(parent)

    def build_game(self):
        # Set MainMenuePanel color and to fullscreen
        self.SetBackgroundColour(col.MAIN_MENUE_BG)
        self.SetSize(self.Parent.Size)

        # Read the gamesize and playertypes from the config
        self.config = wx.Config("NimGame")
        cur_size_str = self.config.Read("gamesize", "[3, 2, 1]")
        cur_size = cur_size_str.strip('[]').split(', ')
        cur_size = list(map(int, cur_size))
        player1_type_id = self.config.ReadInt("player0", 0)
        player2_type_id = self.config.ReadInt("player1", 1)
        print("Initialising game with the following settings:")
        print("\tgamesize: {}".format(cur_size))
        print("\tplayer1: {} - '{}'".format(player1_type_id, ALL_PLAYERS[player1_type_id].name))
        print("\tplayer2: {} - '{}'".format(player2_type_id, ALL_PLAYERS[player2_type_id].name))

        # Create players and game controller
        self.player1 = ManualPlayer("Player 1 - {}".format(ALL_PLAYERS[player1_type_id].name))
        self.player2 = ManualPlayer("Player 2 - {}.format(ALL_PLAYERS[player2_type_id].name")
        self.last_state = State.get_start_state(cur_size)
        self.cur_state = State.get_start_state(cur_size)

        # Init the ui elements
        self.build_ui(cur_size)

        # Draws the initial state
        self.draw_new_state(self.cur_state)
        self.draw_player_name(self.player1)

        self.Layout()

        # start the game logic
        # self.controller = Controller.start_game(self.cur_state, self.player1, self.player2)

    def build_ui(self, gamesize: List):

        pearls_panel = self.create_pearls_panel(gamesize)

        pearls_panel.Bind(wx.EVT_TOGGLEBUTTON, self.on_pearl_clicked)

        # Create info area
        info_panel = wx.Panel(self)
        cur_player_label = wx.StaticText(info_panel, label="current player:")
        self.cur_player = wx.StaticText(info_panel, label="Player XXX")
        info_panel_sizer = wx.BoxSizer(wx.HORIZONTAL)
        info_panel_sizer.Add(cur_player_label, 1, wx.CENTER, 10)
        info_panel_sizer.AddSpacer(5)
        info_panel_sizer.Add(self.cur_player, 1, wx.CENTER, 10)
        info_panel.SetSizer(info_panel_sizer)

        # Create bottom area
        buttons_panel = wx.Panel(self)
        btn_turn = wx.Button(buttons_panel, label='make turn')
        btn_reset = wx.Button(buttons_panel, label='reset')

        # Add events to buttons
        btn_turn.Bind(wx.EVT_BUTTON, self.turn_button_pressed)
        btn_reset.Bind(wx.EVT_BUTTON, self.reset_button_pressed)

        # Adjust buttons horizontal
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(btn_reset, 1, wx.CENTER, 10)
        btn_sizer.AddSpacer(10)
        btn_sizer.Add(btn_turn, 1, wx.CENTER, 10)
        buttons_panel.SetSizer(btn_sizer)

        # Set the positions of the 'pearls'- and 'buttons'-panel
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(pearls_panel, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(info_panel, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(buttons_panel, 0, wx.ALL | wx.CENTER, 10)
        self.SetSizer(main_sizer)

    def create_pearls_panel(self, row_sizes):
        """
        Creates the panel, which contains the pearls
        :return: The panel containing the pearls
        """
        pearls_panel = wx.Panel(self)
        btn_size = (35, 35)

        self.pearls_per_row = []

        rows_sizer = wx.BoxSizer(wx.VERTICAL)

        # All rows
        for row_size in row_sizes:
            row_btns = []
            hor_row_sizer = wx.BoxSizer(wx.HORIZONTAL)

            # Create the buttons for the row
            for btn_id in range(row_size):
                btn = wx.ToggleButton(pearls_panel, size=btn_size)
                row_btns.append(btn)
                hor_row_sizer.Add(btn, proportion=0, flag=wx.ALIGN_LEFT, border=0)

                # Add space between buttons
                if btn_id != row_size - 1:
                    hor_row_sizer.AddSpacer(5)

            # Add row buttons o list containing all rows
            self.pearls_per_row.append(row_btns)

            # Add the row to the vertical layout
            rows_sizer.Add(hor_row_sizer, 0, wx.CENTER)
            rows_sizer.AddSpacer(5)

        pearls_panel.SetSizer(rows_sizer)

        return pearls_panel

    def on_pearl_clicked(self, evt):
        """
        Function called when a button is toggled
        :param evt:
        :return:
        """
        clicked_btn = evt.EventObject
        clicked_pos = self.get_pearls_pos(clicked_btn)

        # toggle the state
        self.cur_state.toggle_pearl(clicked_pos[0], clicked_pos[1])

        # Check if action is valid or the last state (no changes)
        action_valid = GameLogic.is_valid(self.last_state, self.cur_state)
        is_last_state = self.cur_state == self.last_state

        if action_valid or is_last_state:
            # If UI action is okay, draw the state change
            self.draw_new_state(self.cur_state)
        else:
            # Reset state if action is not allowed
            self.cur_state.toggle_pearl(clicked_pos[0], clicked_pos[1])

    def get_pearls_pos(self, clicked_btn):
        """
        Gets the col- and row- id of a clicked button
        :param clicked_btn: THe button which was clicked by the user
        :return: A tuple containing the column- and row id of the clicked button. e.g. (0, 1)
        """
        for (row_id, buttons) in enumerate(self.pearls_per_row):
            for (col_id, btn) in enumerate(buttons):
                if clicked_btn == btn:
                    return row_id, col_id

    def draw_new_state(self, new_state):
        for (row_id, buttons) in enumerate(self.pearls_per_row):
            for (col_id, btn) in enumerate(buttons):
                pearl_state = new_state.Rows[row_id][col_id]

                if pearl_state == 0:
                    btn.SetBackgroundColour("white")
                else:
                    btn.SetBackgroundColour("black")

    def draw_player_name(self, player: Player):
        """
        Displays the name of the player which is on turn
        :param player: The player which shall be displayed
        :return: None
        """
        self.cur_player.SetLabel(player.name)

    def turn_button_pressed(self, evt):
        print("turn_button_pressed")

    def reset_button_pressed(self, evt):
        print("reset_button_pressed")