import wx
from wx.lib.scrolledpanel import ScrolledPanel

from Event import *
from ui.settings.SelectGamesizePanel import *
from ui.settings.SelectPlayerPanel import *

import ui.res.values.colors as COLORS
import ui.res.values.fonts as FONTS


class SettingsPanel(ScrolledPanel):

    def __init__(self, parent, **args):
        super(SettingsPanel, self).__init__(parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.HSCROLL | wx.VSCROLL)
        self.SetupScrolling()

        # Set MainMenuePanel color and to fullscreen
        self.SetBackgroundColour(COLORS.MAIN_MENUE_BG)
        self.SetSize(parent.Size)
        self.SetMinSize(wx.Size(400, 400))

        # The events
        self.evt_back = Event()

        # Init the ui elements
        self.build_ui(parent)

    def build_ui(self, parent):
        """
        Creates all UI elements of the panel
        :return: None
        """
        # Create two panels (right and left side)
        left_panel = self.build_menue_panel()

        # Create all panels, which can be on the right side
        self.right_panels = []

        self.right_empty_panel = wx.Panel(self)
        self.right_empty_panel.SetBackgroundColour(COLORS.SETTINGS_DETAILS_BG)
        self.right_panels.append(self.right_empty_panel)

        self.select_gamesize_panel = SelectGamesizePanel(self)
        self.right_panels.append(self.select_gamesize_panel)

        self.select_player1_panel = SelectPlayerPanel(self, 0)
        self.right_panels.append(self.select_player1_panel)

        self.select_player2_panel = SelectPlayerPanel(self, 1)
        self.right_panels.append(self.select_player2_panel)

        for panel in self.right_panels:
            panel.Hide()

        # Align left and right panel horizontal
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox.Add(left_panel, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        self.hbox.Add(self.right_empty_panel, 1, wx.ALIGN_RIGHT | wx.EXPAND | wx.RIGHT | wx.TOP | wx.BOTTOM, 10)
        self.hbox.Add(self.select_gamesize_panel, 1, wx.ALIGN_RIGHT | wx.EXPAND | wx.RIGHT | wx.TOP | wx.BOTTOM, 10)
        self.hbox.Add(self.select_player1_panel, 1, wx.ALIGN_RIGHT | wx.EXPAND | wx.RIGHT | wx.TOP | wx.BOTTOM, 10)
        self.hbox.Add(self.select_player2_panel, 1, wx.ALIGN_RIGHT | wx.EXPAND | wx.RIGHT | wx.TOP | wx.BOTTOM, 10)
        self.SetSizerAndFit(self.hbox)
        self.Layout()

    def build_menue_panel(self) -> wx.Panel:
        """Create the menue panel, which is displayed at the left side
        
        Returns:
            wx.Panel -- The menue panel, completly constructed with all child elemnts
        """
        left_panel = wx.Panel(self)
        left_panel.SetBackgroundColour(COLORS.SETTING_MENUE_BG)

        # The ui elements of the left panel
        title = wx.StaticText(left_panel, label="Settings")
        title.SetFont(FONTS.SUB_TITLE)

        btn_gamesize = wx.Button(left_panel, label='Gamesize')
        btn_gamesize.SetFont(FONTS.SUB_MENUE_ITEM)
        btn_gamesize.SetBackgroundColour(COLORS.SETTINGS_BTN)

        btn_player1 = wx.Button(left_panel, label='Player 1')
        btn_player1.SetFont(FONTS.SUB_MENUE_ITEM)
        btn_player1.SetBackgroundColour(COLORS.SETTINGS_BTN)

        btn_player2 = wx.Button(left_panel, label='Player 2')
        btn_player2.SetFont(FONTS.SUB_MENUE_ITEM)
        btn_player2.SetBackgroundColour(COLORS.SETTINGS_BTN)

        btn_back = wx.Button(left_panel, label='Back')
        btn_back.SetFont(FONTS.SUB_MENUE_ITEM)
        btn_back.SetBackgroundColour(COLORS.SETTINGS_BTN)

        # Set the function bindings for the menue buttons
        btn_gamesize.Bind(wx.EVT_BUTTON, lambda e: self.show_select_gamesize())
        btn_player1.Bind(wx.EVT_BUTTON, lambda e: self.show_select_player1())
        btn_player2.Bind(wx.EVT_BUTTON, lambda e: self.show_select_player2())
        btn_back.Bind(wx.EVT_BUTTON, lambda e: self.evt_back())

        # Align all elements vertical 
        vbox_left = wx.BoxSizer(wx.VERTICAL)
        vbox_left.Add(title, 0, wx.ALIGN_CENTER | wx.ALL, 20)
        vbox_left.Add(btn_gamesize, 0, wx.ALIGN_CENTER | wx.EXPAND | wx.ALL, 10)
        vbox_left.Add(btn_player1, 0, wx.ALIGN_CENTER | wx.EXPAND | wx.ALL, 10)
        vbox_left.Add(btn_player2, 0, wx.ALIGN_CENTER | wx.EXPAND | wx.ALL, 10)
        vbox_left.Add(btn_back, 0, wx.ALIGN_CENTER | wx.EXPAND | wx.ALL, 10)
        left_panel.SetSizerAndFit(vbox_left)
        return left_panel

    def show_select_gamesize(self):
        """ Shows the selection panel to choose the size of the game """
        self.show_panel(self.select_gamesize_panel)

    def show_select_player1(self):
        """ Shows the selection panel to choose the first player """
        self.show_panel(self.select_player1_panel)

    def show_select_player2(self):
        """ Shows the selection panel to choose the second player """
        self.show_panel(self.select_player2_panel)

    def show_panel(self, to_show_panel):
        """
        Shows a panel and hides all others
        :param to_show_panel: The panel to show in the frame
        """
        for panel in self.right_panels:
            panel.Hide()
        to_show_panel.Show()
        self.Layout()
