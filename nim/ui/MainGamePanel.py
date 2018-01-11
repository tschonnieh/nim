from typing import List

import copy
import wx

from Event import *
from Controller import Controller
from logic.GameLogic import GameLogic
from logic.State import State
from player.Player import Player
from player.PlayerDict import ALL_PLAYERS, MANUAL_PLAYER
from player.create_player_by_type_id import create_player_by_type_id

import ui.res.values.fonts as FONTS
import ui.res.values.colors as COLORS


class MainGamePanel(wx.Panel):
    """
    The panel containing the main game.
    It shows multiple rows of pearls
    """

    def __init__(self, parent, **args):
        super(MainGamePanel, self).__init__(parent)

        # The events
        self.evt_back = Event()

    def build_game(self):

        self.ClearBackground()
        self.Refresh()

        # Set MainMenuePanel color and to fullscreen
        self.SetBackgroundColour(COLORS.MAIN_MENUE_BG)
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
        try:
            self.player1 = create_player_by_type_id(player1_type_id, "Player 1", cur_size)
            self.player2 = create_player_by_type_id(player2_type_id, "Player 2", cur_size)
        except Exception as ex:
            print(ex)
            self.leave_game_with_error(str(ex))

        self.cur_player = self.player1
        self.last_state = State.get_start_state(cur_size)
        self.cur_state = State.get_start_state(cur_size)
        self.controller = Controller()
        self.controller.init_game(self.cur_state, self.player1, self.player2)

        # Init the ui elements
        self.build_ui(cur_size)

        # Draws the initial state
        self.draw_new_state(self.cur_state)
        self.show_active_player(self.player1)

        self.Layout()

    def build_ui(self, gamesize: List):

        # Open dialog when palyer pressed 'ESC'
        self.Bind(wx.EVT_CHAR_HOOK, self.open_leave_game_dialog)

        self.pearls_panel = self.create_pearls_panel(gamesize)
        self.pearls_panel.Bind(wx.EVT_TOGGLEBUTTON, self.on_pearl_clicked)

        # Create info area
        info_panel = wx.Panel(self)
        self.player1_label = wx.StaticText(info_panel, label=str(self.player1))
        self.player2_label = wx.StaticText(info_panel, label=str(self.player2))
        self.player1_label.SetFont(FONTS.TXT_BIG)
        self.player2_label.SetFont(FONTS.TXT_BIG)
        info_panel_sizer = wx.BoxSizer(wx.HORIZONTAL)
        info_panel_sizer.Add(self.player1_label, 1, wx.TOP | wx.BOTTOM | wx.EXPAND | wx.ALIGN_CENTER, 15)
        info_panel_sizer.AddSpacer(5)
        info_panel_sizer.Add(self.player2_label, 1, wx.TOP | wx.BOTTOM | wx.EXPAND | wx.ALIGN_CENTER, 15)
        info_panel.SetSizer(info_panel_sizer)

        # Create bottom area
        buttons_panel = wx.Panel(self)
        self.btn_turn = wx.Button(buttons_panel, label='make turn')
        self.btn_reset = wx.Button(buttons_panel, label='reset')
        self.stop_game = wx.Button(buttons_panel, label='Stop game')

        # Add events to buttons
        self.btn_turn.Bind(wx.EVT_BUTTON, self.turn_button_pressed)
        self.btn_reset.Bind(wx.EVT_BUTTON, self.reset_button_pressed)
        self.stop_game.Bind(wx.EVT_BUTTON, self.open_leave_game_dialog)

        # Adjust buttons horizontal
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(self.stop_game, 0, wx.ALIGN_LEFT | wx.CENTER, 10)
        btn_sizer.AddStretchSpacer()
        btn_sizer.Add(self.btn_reset, 0, wx.ALIGN_CENTER | wx.CENTER, 10)
        btn_sizer.AddSpacer(10)
        btn_sizer.Add(self.btn_turn, 0, wx.ALIGN_CENTER | wx.CENTER, 10)
        btn_sizer.AddStretchSpacer()
        btn_sizer.AddSpacer(50)

        buttons_panel.SetSizer(btn_sizer)

        # Set the positions of the 'pearls'- and 'buttons'-panel
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.pearls_panel, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(info_panel, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(buttons_panel, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL | wx.CENTER, 10)
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
        # Allows changing the pearls only if manual player is playing
        if self.cur_player.PlayerType.id != MANUAL_PLAYER.id or self.controller.game_over:
            return False

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
        """
        Draws the new state on the UI
        :param new_state: The state to draw
        :return: None
        """
        for (row_id, buttons) in enumerate(self.pearls_per_row):
            for (col_id, btn) in enumerate(buttons):
                pearl_state = new_state.Rows[row_id][col_id]

                if pearl_state == 0:
                    btn.SetBackgroundColour("white")
                else:
                    btn.SetBackgroundColour("black")

    def show_active_player(self, cur_player: Player):
        """
        Displays the name of the player which is on turn
        :param cur_player: The player which is making the next turn
        :return: None
        """
        if cur_player == self.player1:
            self.player1_label.SetBackgroundColour(COLORS.CUR_PLAYER_BG)
            self.player2_label.SetBackgroundColour(COLORS.WAITING_PLAYER_BG)
        else:
            self.player1_label.SetBackgroundColour(COLORS.WAITING_PLAYER_BG)
            self.player2_label.SetBackgroundColour(COLORS.CUR_PLAYER_BG)

    def turn_button_pressed(self, evt):
        """
        Action executed, when 'turn' button is clicked
        :param evt: The event object
        :return: None
        """
        # If current player is MANUAL, set the position from ui pearls
        if self.cur_player.PlayerType.id == MANUAL_PLAYER.id:

            # Check if the user action is valid, if not break here
            if not GameLogic.is_valid(self.last_state, self.cur_state):
                print("Turn is not valid ...")
                wx.MessageBox("Turn is not valid ...", 'Invalid changes', wx.OK | wx.ICON_ERROR)
                return
            else:
                # print("UI sends state:\n{}".format(self.cur_state))
                self.cur_player.set_state(self.cur_state)

        # Make the next step
        (player, state, has_won) = self.controller.make_step()
        print("{}:\n{} - has_won: {}".format(player.name, state, has_won))
        self.last_state = state
        self.cur_state = copy.deepcopy(state)

        self.cur_player = self.controller.get_current_player()
        self.show_active_player(self.cur_player)
        self.draw_new_state(state)

        # What to do when player won the game
        if self.controller.game_over:
            # Disable the buttons if the game is over
            self.btn_turn.Disable()
            self.btn_reset.Disable()
            # Show winning message
            winning_message = "{} has won the game".format(self.cur_player)
            print(winning_message)
            wx.MessageBox(winning_message, 'Game over', wx.OK | wx.ICON_INFORMATION)

        self.Layout()

    def reset_button_pressed(self, evt):
        """
        Action executed, when 'reset' button is clicked
        :param evt: The event object
        :return: None
        """
        print('Resetting state ...')
        self.cur_state = copy.deepcopy(self.last_state)
        self.draw_new_state(self.cur_state)

    def leave_game_with_error(self, err_message):
        """
        Displays an error dialog end goes back to the main menue.
        :param err_message:
        :return:
        """
        dlg = wx.MessageDialog(None, err_message, 'Error while creating player', wx.ICON_ERROR)
        dlg.ShowModal()
        self.Unbind(wx.EVT_CHAR_HOOK)
        self.evt_back()

    def open_leave_game_dialog(self, event):
        """
        Opens a dialog, which allows user to stop the game and go back to the main menue.
        When the game is already over, no dialog is displayed.
        :return:
        """
        if self.controller.game_over:
            self.evt_back()
            return

        dlg = wx.MessageDialog(None, "Do you want to stop the game?", 'Stop game', wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        if result == wx.ID_YES:
            print("Yes pressed")
            self.Unbind(wx.EVT_CHAR_HOOK)
            self.evt_back()
        else:
            print("No pressed")

    def on_key_up_pressed(self, event):
        """
        Event called when KEY_UP event is fired
        :param event:
        :return:
        """
        print("OnKeyUP pressed!")
        keyCode = event.GetKeyCode()
        if keyCode == wx.WXK_ESCAPE:
            self.open_leave_game_dialog()
        event.Skip()


