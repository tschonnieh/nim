from wx import *
from ui.MainMenuePanel import *
from ui.MainGamePanel import *
from ui.SettingsPanel import *

class GameUI:

    def __init__(self):
        # Erzeugung des Fensters
        self.app = App()
        self.frame = Frame(parent=None, title="Nim Game", size=(800, 600))
        self.frame.SetBackgroundColour("white")

        # Display the panel with the startmenue
        self.main_menue_panel = MainMenuePanel(self.frame)
        self.main_menue_panel.evt_startgame.add(self.start_game)
        self.main_menue_panel.evt_show_settings.add(self.show_settings)
        
        # Create panel for settings
        self.settings_panel = SettingsPanel(self.frame)
        self.settings_panel.evt_back.add(self.show_main_menue)

        # Create the panel for the maingame
        self.main_game_panel = MainGamePanel(self.frame)

        
        self.sizer = BoxSizer(VERTICAL)
        self.sizer.Add(self.main_menue_panel, 1, EXPAND)
        self.sizer.Add(self.main_game_panel, 1, EXPAND)
        self.sizer.Add(self.settings_panel, 1, EXPAND)
        self.frame.SetSizer(self.sizer)

        self.show_main_menue()
        self.frame.Show()

    def show_main_menue(self):
        """Shows the main menue panel and hides all other panels"""
        self.main_menue_panel.Show()
        self.settings_panel.Hide()
        self.main_game_panel.Hide()

    def start_game(self):
        """Shows the main game panel and hides all other panels"""
        self.main_menue_panel.Hide()
        self.settings_panel.Hide()
        self.main_game_panel.Show()
        print("Startgame")

    def show_settings(self):
        """Shows the settings panel and hides all other panels"""
        self.main_menue_panel.Hide()
        self.settings_panel.Show()
        self.main_game_panel.Hide()


    def run(self):
        """Starts the game ui
        """
        self.app.MainLoop()