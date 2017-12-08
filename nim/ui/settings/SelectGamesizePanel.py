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
        content_panel = wx.Panel(self)

        content_box = wx.StaticBox(content_panel, label='Select the gamesize')
        content_box.SetFont(FONTS.SUB_MENUE_ITEM)
        content_box_sizer = wx.StaticBoxSizer(content_box, orient=wx.VERTICAL)
        content_box_sizer.Add(wx.RadioButton(content_panel, label='Small (3-2-1)', style=wx.RB_GROUP))
        content_box_sizer.Add(wx.RadioButton(content_panel, label='Normal (4-3-2)'))
        content_box_sizer.Add(wx.RadioButton(content_panel, label='Large (5-4-3)'))
        content_panel.SetSizer(content_box_sizer)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(wx.RadioButton(content_panel, label='Custom'))
        hbox1.Add(wx.TextCtrl(content_panel), flag=wx.LEFT, border=5)
        content_box_sizer.Add(hbox1)

        # Aligns butttons horizontal
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        saveButton = wx.Button(self, label='Save')
        cancelButton = wx.Button(self, label='Cancel')
        button_sizer.Add(saveButton, flag=wx.RIGHT)
        button_sizer.Add(cancelButton, flag=wx.LEFT, border=5)

        # Place content on the top and buttons at bottom
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(content_panel, proportion=2, flag=wx.EXPAND | wx.RIGHT, border=5)
        vbox1.AddStretchSpacer(1)
        vbox1.Add(button_sizer, 0, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        self.SetSizerAndFit(vbox1)
