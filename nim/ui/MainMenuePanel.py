import wx

from nim.Event import *
import nim.ui.res.values.colors as col
import nim.ui.res.values.fonts as FONTS


class MainMenuePanel(wx.Panel):

    def __init__(self, parent, **args):
        super(MainMenuePanel, self).__init__(parent)

        # The events
        self.evt_startgame = Event()
        self.evt_show_settings = Event()

        # Set MainMenuePanel color and to fullscreen
        self.SetBackgroundColour(col.MAIN_PANEL_BG)
        self.SetSize(parent.Size)

        # Init the ui elements
        self.build_ui()

    def build_ui(self):

        # Create menue buttons
        btn_max_size = wx.Size(250, -1)
        b_start = wx.Button(self, label="Start game")
        b_start.SetFont(FONTS.MAIN_MENUE_ITEM)
        b_start.SetMaxSize(btn_max_size)
        b_choose_players = wx.Button(self, label="Settings")
        b_choose_players.SetFont(FONTS.MAIN_MENUE_ITEM)
        b_choose_players.SetMaxSize(btn_max_size)
        b_quit = wx.Button(self, label="Quit game")
        b_quit.SetFont(FONTS.MAIN_MENUE_ITEM)
        b_quit.SetMaxSize(btn_max_size)

        # Set the function bindings for the menue buttons
        b_start.Bind(wx.EVT_BUTTON, lambda x: self.evt_startgame())
        b_choose_players.Bind(wx.EVT_BUTTON, lambda x: self.evt_show_settings())
        b_quit.Bind(wx.EVT_BUTTON, self.quit_btn_click)
        
        # Align buttons vertical
        vert_box = wx.BoxSizer(wx.VERTICAL)

        vert_box.AddSpacer(25)
        vert_box.Add(b_start, 0, wx.ALIGN_CENTER | wx.EXPAND | wx.ALL, 5)
        vert_box.Add(b_choose_players, 0, wx.ALIGN_CENTER | wx.EXPAND | wx.ALL, 5)
        vert_box.Add(b_quit, 0, wx.EXPAND | wx.ALIGN_CENTER | wx.EXPAND | wx.ALL, 5)
        vert_box.AddStretchSpacer(1)
        
        self.SetSizer(vert_box)

    def quit_btn_click(self, event):
        exit()