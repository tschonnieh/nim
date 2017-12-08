import wx
from nim.Event import *

import nim.ui.res.values.colors as COLORS
import nim.ui.res.values.fonts as FONTS


class SelectPlayerPanel(wx.Panel):

    def __init__(self, parent):
        super(SelectPlayerPanel, self).__init__(parent)

        self.SetBackgroundColour(COLORS.PANEL_SETTINGS_DETAILS_BG)
        self.SetSize(parent.Size)

        # The events
        self.evt_back = Event()

        # Init the ui elements
        self.build_ui(parent)

    def build_ui(self, parent):
        """
        Creates all UI elements of the panel
        :return: None
        """
        # Create the title of the panel
        title = wx.StaticText(self, label="Select a player")
        title.SetFont(FONTS.SUB_SUB_TITLE)

        # Create the ListBox, which shows all possible players
        players = ['Person', 'Q-Learning', 'Random KI', 'Perfect Player (Logic)']
        info_text = ['A person is manually playing', 'A KI using the Q-Learning algorithm for learning',
                     'A KI playing with random actions',
                     'A KI, which always makes the best possible action. The KI uses a mathematical model']
        player_list_box = wx.ListBox(self, size=(-1, -1), choices=players, style=wx.LB_SINGLE)

        # Create a details panel on the right
        # self.text = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        details_panel = wx.Panel(self)
        details_box = wx.StaticBox(details_panel, label='Details')
        sbs = wx.StaticBoxSizer(details_box, orient=wx.VERTICAL)
        sbs.Add(wx.RadioButton(details_panel, label='Small (3-2-1)', style=wx.RB_GROUP))
        details_panel.SetSizer(sbs)

        # Cancel and save button
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        saveButton = wx.Button(self, label='Save')
        cancelButton = wx.Button(self, label='Cancel')
        hbox2.Add(saveButton, flag=wx.RIGHT)
        hbox2.Add(cancelButton, flag=wx.LEFT, border=5)

        # Place 'listBox' on the left and 'details_panel' on the right
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(player_list_box, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        hbox.Add(details_panel, 1, wx.ALIGN_LEFT | wx.ALL | wx.EXPAND, 5)

        # Set 'title' above the 'listBox'
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(title, 0, wx.ALIGN_TOP | wx.ALL, 15)
        vbox.Add(hbox, 0, wx.ALIGN_TOP | wx.EXPAND | wx.ALL, 15)
        vbox.AddStretchSpacer(1)
        vbox.Add(hbox2, 0, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        self.SetSizerAndFit(vbox)
        self.Layout()
