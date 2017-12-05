from wx import Panel, Font, Button, BoxSizer
from wx import EXPAND, VERTICAL, DECORATIVE, ITALIC, VERTICAL, NORMAL, EVT_BUTTON
from Event import Event

class MainMenuePanel(Panel):

    def __init__(self, parent, **args):
        super(MainMenuePanel, self).__init__(parent)

        # The events
        self.evt_startgame = Event()
        self.evt_show_settings = Event()

        # Set MainMenuePanel color and to fullscreen
        self.SetBackgroundColour("#e8e2de")
        self.SetSize(parent.Size)

        # Init the ui elements
        self.build_ui()

    def build_ui(self):

        # Default font for menue
        menue_font = Font(18, DECORATIVE, ITALIC, NORMAL)

        # Create menue buttons
        b_start = Button(self, label="Start game")
        b_start.SetFont(menue_font)
        b_choose_players = Button(self, label="Settings")
        b_choose_players.SetFont(menue_font)
        b_quit = Button(self, label="Quit game")
        b_quit.SetFont(menue_font)

        # Set the function bindings for the menue buttons
        b_start.Bind(EVT_BUTTON, lambda x: self.evt_startgame())
        b_choose_players.Bind(EVT_BUTTON, lambda x: self.evt_show_settings())
        b_quit.Bind(EVT_BUTTON, self.quit_btn_click)
        
        # Align buttons vertical
        vert_box = BoxSizer(VERTICAL)
        vert_box.AddStretchSpacer(1)
        vert_box.Add(b_start, 0,  EXPAND, 20)
        vert_box.Add(b_choose_players, 0, EXPAND)
        vert_box.Add(b_quit, 0, EXPAND)
        vert_box.AddStretchSpacer(1)
        
        self.SetSizer(vert_box)

    def quit_btn_click(self, event):
        exit()