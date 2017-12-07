from wx import *

from ui.MainMenuePanel import *
from ui.MainGamePanel import *
from ui.SettingsPanel import *

class GameUI:
    """ The main window of the nim UI. Contains the 'frame' object of wxpython """

    def __init__(self):
        # Erzeugung des Fensters
        self.app = App()
        self.frame = Frame(parent=None, title="Nim Game", size=(800, 600))
        self.frame.SetBackgroundColour("white")


        # Set the icon of the frame
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("./ressources/icon.ico", wx.BITMAP_TYPE_ANY))
        self.frame.SetIcon(icon)

        # All panels which can be open by the menue buttons
        self.main_panels = []
        self.create_main_panels()

        self.show_main_menue()
        self.frame.Show()

    def create_main_panels(self):
        """
        Creates all child panels of the frame
        """
        # Display the panel with the startmenue
        self.main_menue_panel = MainMenuePanel(self.frame)
        self.main_menue_panel.evt_startgame.add(self.start_game)
        self.main_menue_panel.evt_show_settings.add(self.show_settings)
        self.main_panels.append(self.main_menue_panel)

        # Create panel for settings
        self.settings_panel = SettingsPanel(self.frame)
        self.settings_panel.evt_back.add(self.show_main_menue)
        self.main_panels.append(self.settings_panel)

        # Create the panel for the maingame
        self.main_game_panel = MainGamePanel(self.frame)
        self.main_panels.append(self.main_game_panel)

        # Set the size of the shown panel to maximum framesize
        self.sizer = BoxSizer(VERTICAL)
        self.sizer.Add(self.main_menue_panel, 1, EXPAND)
        self.sizer.Add(self.main_game_panel, 1, EXPAND)
        self.sizer.Add(self.settings_panel, 1, EXPAND)
        self.frame.SetSizer(self.sizer)

    def show_main_menue(self):
        """ Shows the main menue panel and hides all other panels """
        self.show_panel(self.main_menue_panel)

    def start_game(self):
        """ Shows the main game panel and hides all other panels """
        self.show_panel(self.main_game_panel)

    def show_settings(self):
        """ Shows the settings panel and hides all other panels """
        self.show_panel(self.settings_panel)

    def show_panel(self, to_show_panel):
        """
        Shows a panel and hides all others
        :param to_show_panel: The panel to show in the frame
        """
        for panel in self.main_panels:
            panel.Hide()
        to_show_panel.Show()
        self.frame.Layout()


    def run(self):
        """Starts the game ui"""
        self.app.MainLoop()