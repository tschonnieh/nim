import wx
from Event import *

import ui.res.values.colors as COLORS
import ui.res.values.fonts as FONTS


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
        content_vbox_sizer = wx.StaticBoxSizer(content_box, orient=wx.VERTICAL)

        # Create radio buttons
        radio_btn_1 = wx.RadioButton(content_panel, label='Small (3-2-1)', style=wx.RB_GROUP)
        radio_btn_1.SetFont(FONTS.TXT_NORMAL)
        radio_btn_2 = wx.RadioButton(content_panel, label='Normal (4-3-2)')
        radio_btn_2.SetFont(FONTS.TXT_NORMAL)
        radio_btn_3 = wx.RadioButton(content_panel, label='Large (5-4-3)')
        radio_btn_3.SetFont(FONTS.TXT_NORMAL)

        # Add radio buttons to content_box_sizer
        content_vbox_sizer.Add(radio_btn_1, 0, wx.LEFT, 5)
        content_vbox_sizer.AddSpacer(3)
        content_vbox_sizer.Add(radio_btn_2, 0, wx.LEFT, 5)
        content_vbox_sizer.AddSpacer(3)
        content_vbox_sizer.Add(radio_btn_3, 0, wx.LEFT, 5)
        content_vbox_sizer.AddSpacer(3)
        content_panel.SetSizer(content_vbox_sizer)

        # Create the radio button for a custom gamesize
        custom_button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        radio_btn_custom = wx.RadioButton(content_panel, label='Custom')
        radio_btn_custom.SetFont(FONTS.TXT_NORMAL)
        txt_ctrl_custom = wx.TextCtrl(content_panel)
        txt_ctrl_custom.SetFont(FONTS.TXT_NORMAL)
        custom_button_sizer.Add(radio_btn_custom)
        custom_button_sizer.Add(txt_ctrl_custom, flag = wx.LEFT, border = 5)
        content_vbox_sizer.Add(custom_button_sizer, 0, wx.LEFT, 5)

        # Aligns butttons horizontal
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        saveButton = wx.Button(self, label='Save')
        saveButton.Bind(wx.EVT_BUTTON, self.save_button_clicked)
        cancelButton = wx.Button(self, label='Cancel')
        cancelButton.Bind(wx.EVT_BUTTON, self.cancel_button_clicked)
        button_sizer.Add(saveButton, flag=wx.RIGHT)
        button_sizer.Add(cancelButton, flag=wx.LEFT, border=5)

        # Place content on the top and buttons at bottom
        vertical_box = wx.BoxSizer(wx.VERTICAL)
        vertical_box.AddSpacer(3)
        vertical_box.Add(content_panel, proportion=2, flag=wx.EXPAND | wx.RIGHT, border=5)
        vertical_box.AddStretchSpacer(1)
        vertical_box.Add(button_sizer, 0, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        self.SetSizerAndFit(vertical_box)

    def save_button_clicked(self, evt):
        """
        Action when the 'save' button is clicked
        :param evt: The wx event object
        :return:
        """
        print("Save clicked")

    def cancel_button_clicked(selfself, evt):
        """
        Action when the 'cancel' button is clicked
        :param evt: The wx event object
        :return:
        """
        print("Cancel clicked")
