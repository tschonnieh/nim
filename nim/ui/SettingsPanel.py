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

        # Create two panels (right and left side)
        left_panel = self.build_menue_panel()
        right_panel = wx.Panel(self)
        right_panel.SetBackgroundColour('#b3b3b3')
		
        
        # The ui elements of the right side
        #vbox_right = wx.BoxSizer(wx.VERTICAL)
        #vbox_right.AddStretchSpacer(1)
        #right_panel.SetSizerAndFit(vbox_right)

        # Align left and right panel horizontal
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(left_panel, 0, wx.ALIGN_LEFT|wx.ALL, 10)
        hbox.Add(right_panel, 1, wx.ALIGN_RIGHT|wx.EXPAND|wx.RIGHT|wx.TOP|wx.BOTTOM , 10)
        self.SetSizerAndFit(hbox)
        self.Layout()

    def build_menue_panel(self) -> wx.Panel:
        """Create the menue panel, which is displayed at the left side
        
        Returns:
            wx.Panel -- The menue panel, completly constructed with all child elemnts
        """
        menue_font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)

        left_panel = wx.Panel(self)

        # The ui elements of the left panel
        title = wx.StaticText(left_panel, label = "Settings")
        title.SetFont(menue_font)

        btn_gamesize = wx.Button(left_panel, label='Gamesize')
        btn_gamesize.SetFont(menue_font)

        btn_player1 = wx.Button(left_panel, label='Player 1')
        btn_player1.SetFont(menue_font)

        btn_player2 = wx.Button(left_panel, label='Player 2')
        btn_player2.SetFont(menue_font)
        
        btn_back = wx.Button(left_panel, label='Back')
        btn_back.SetFont(menue_font)

        # Set the function bindings for the menue buttons
        btn_back.Bind(wx.EVT_BUTTON, lambda x: self.evt_back())

        # Align all elements vertical 
        vbox_left = wx.BoxSizer(wx.VERTICAL)
        vbox_left.Add(title, 0,  wx.ALIGN_CENTER|wx.ALL, 20)
        vbox_left.Add(btn_gamesize, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.ALL, 10)
        vbox_left.Add(btn_player1, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.ALL, 10)
        vbox_left.Add(btn_player2, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.ALL, 10)
        vbox_left.Add(btn_back, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.ALL, 10)
        left_panel.SetSizerAndFit(vbox_left)
        return left_panel

