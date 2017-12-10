import wx
from nim.Event import *

import nim.ui.res.values.colors as COLORS
import nim.ui.res.values.fonts as FONTS


class SelectGamesizePanel(wx.Panel):

    def __init__(self, parent, **args):
        super(SelectGamesizePanel, self).__init__(parent)

        self.SetBackgroundColour(COLORS.SETTINGS_DETAILS_BG)
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

        # Create radio buttons
        radio_btn_1 = wx.RadioButton(content_panel, label='Small (3-2-1)', style=wx.RB_GROUP)
        radio_btn_1.SetFont(FONTS.TXT_NORMAL)
        radio_btn_2 = wx.RadioButton(content_panel, label='Normal (4-3-2)', style=wx.RB_GROUP)
        radio_btn_2.SetFont(FONTS.TXT_NORMAL)
        radio_btn_3 = wx.RadioButton(content_panel, label='Large (5-4-3)', style=wx.RB_GROUP)
        radio_btn_3.SetFont(FONTS.TXT_NORMAL)

        # Add radio buttons to content_box_sizer
        content_box_sizer.Add(radio_btn_1)
        content_box_sizer.Add(radio_btn_2)
        content_box_sizer.Add(radio_btn_3)
        content_panel.SetSizer(content_box_sizer)

        # Create the custom radio button
        custom_button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        custom_button_sizer.Add(wx.RadioButton(content_panel, label='Custom'))
        custom_button_sizer.Add(wx.TextCtrl(content_panel), flag=wx.LEFT, border=5)
        content_box_sizer.Add(custom_button_sizer)

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
