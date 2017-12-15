from typing import List

import wx
from wx.lib.agw.shapedbutton import SButton, SBitmapButton

import ui.res.values.colors as col


class MainGamePanel(wx.Panel):

    def __init__(self, parent, **args):
        super(MainGamePanel, self).__init__(parent)

    def build_game(self,):
        # Set MainMenuePanel color and to fullscreen
        self.SetBackgroundColour(col.MAIN_MENUE_BG)
        self.SetSize(self.Parent.Size)

        # get the gamesize from the config
        self.config = wx.Config("NimGame")
        cur_size_str = self.config.Read("gamesize", "[3, 2, 1]")
        cur_size = cur_size_str.strip('[]').split(', ')
        cur_size = list(map(int, cur_size))
        print("Initialising game with size {}".format(cur_size))

        # Init the ui elements
        self.build_ui(cur_size)
        self.Layout()

    def build_ui(self, gamesize: List):

        pearls_panel = self.create_pearls_panel(gamesize)

        pearls_panel.Bind(wx.EVT_TOGGLEBUTTON, self.on_pearl_clicked)

        # Create bottom area
        buttons_panel = wx.Panel(self)
        btn_turn = wx.Button(buttons_panel, label='make turn')
        btn_reset = wx.Button(buttons_panel, label='reset')

        # Adjust buttons horizontal
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(btn_reset, 1, wx.CENTER, 10)
        btn_sizer.AddSpacer(10)
        btn_sizer.Add(btn_turn, 1, wx.CENTER, 10)
        buttons_panel.SetSizer(btn_sizer)

        # Set the positions of the 'pearls'- and 'buttons'-panel
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(pearls_panel, wx.EXPAND | wx.ALL, 5)
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
                btn.SetBackgroundColour("black")
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
        FUnction called when a button is toggled
        :param evt:
        :return:
        """
        clicked_btn = evt.EventObject
        if clicked_btn.GetBackgroundColour().RGB == 0:
            clicked_btn.SetBackgroundColour("white")
        else:
            clicked_btn.SetBackgroundColour("black")

        print(self.get_pearls_pos(clicked_btn))
        self.Layout()

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

