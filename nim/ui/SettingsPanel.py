import wx
from Event import *


class SettingsPanel(wx.Panel):

    def __init__(self, parent, **args):
        super(SettingsPanel, self).__init__(parent)

        # Set MainMenuePanel color and to fullscreen
        self.SetBackgroundColour("#e8e2de")
        self.SetSize(parent.Size)

        # The events
        self.evt_back = Event()

        # Init the ui elements
        self.build_ui(parent)

    def build_ui(self, parent):

        # The default font for settings
        menue_font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)

        p_demo = wx.StaticText(parent=self, style=wx.ALIGN_LEFT)
        p_demo.SetLabel("Implementation of 'SettingsPanel' is missing")
        p_demo.SetSize((600, -1))
        p_demo.SetPosition((10, 10))

        btn_back = wx.Button(self, label='Back')
        btn_back.SetFont(menue_font)
        btn_back.SetPosition((10, 100))

        # Set the function bindings for the menue buttons
        btn_back.Bind(wx.EVT_BUTTON, lambda x: self.evt_back())
