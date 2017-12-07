import wx
from nim.Event import *

import nim.ui.res.values.colors as COLORS
import nim.ui.res.values.fonts as FONTS


class SelectPlayerPanel(wx.Panel):

    def __init__(self, parent, **args):
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
        title = wx.StaticText(self, label="Select player")
        title.SetFont(FONTS.SUB_SUB_TITLE)

        # Align left and right panel horizontal
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(title, 0, wx.ALIGN_TOP | wx.ALL, 15)
        self.SetSizerAndFit(hbox)
        self.Layout()
