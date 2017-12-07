import wx
from nim.Event import *

import nim.ui.res.values.colors as COLORS
import nim.ui.res.values.fonts as FONTS


class SelectGamesizePanel(wx.Panel):

    def __init__(self, parent, **args):
        super(SelectGamesizePanel, self).__init__(parent)

        self.SetBackgroundColour(COLORS.PANEL_SETTINGS_DETAILS_BG)
        self.SetSize(parent.Size)

        # The events
        self.evt_back = Event()

        # Init the ui elements
        self.build_ui()

    def build_ui(self):
        """
        Creates all UI elements of the panel
        :return: None
        """
        radiobox_panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(self, label="Select the gamesize")
        title.SetFont(FONTS.SUB_SUB_TITLE)

        sb = wx.StaticBox(radiobox_panel, label='Gamesize')
        sbs = wx.StaticBoxSizer(sb, orient=wx.VERTICAL)
        sbs.Add(wx.RadioButton(radiobox_panel, label='Small (3-2-1)', style=wx.RB_GROUP))
        sbs.Add(wx.RadioButton(radiobox_panel, label='Normal (4-3-2)'))
        sbs.Add(wx.RadioButton(radiobox_panel, label='Large (5-4-3)'))

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(wx.RadioButton(radiobox_panel, label='Custom'))
        hbox1.Add(wx.TextCtrl(radiobox_panel), flag=wx.LEFT, border=5)
        sbs.Add(hbox1)

        radiobox_panel.SetSizer(sbs)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        saveButton = wx.Button(self, label='Save')
        cancelButton = wx.Button(self, label='Cancel')
        hbox2.Add(saveButton, flag=wx.RIGHT)
        hbox2.Add(cancelButton, flag=wx.LEFT, border=5)

        vbox.Add(title, 0, wx.ALIGN_CENTER | wx.EXPAND | wx.ALL, 15)
        vbox.Add(radiobox_panel, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        self.SetSizerAndFit(vbox)
