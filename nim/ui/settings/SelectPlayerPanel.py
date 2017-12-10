import wx
from nim.Event import *

import nim.ui.res.values.colors as COLORS
import nim.ui.res.values.fonts as FONTS


class SelectPlayerPanel(wx.Panel):

    def __init__(self, parent):
        super(SelectPlayerPanel, self).__init__(parent)

        self.SetBackgroundColour(COLORS.SETTINGS_DETAILS_BG)
        self.SetSize(parent.Size)

        # The events
        self.evt_back = Event()

        # The data for the list box
        self.players = ['Person', 'Q-Learning', 'Random KI', 'Perfect Player (Logic)']
        self.info_text = ['A person is manually playing', 'A KI using the Q-Learning algorithm for learning',
                          'A KI playing with random actions',
                          'A KI, which always makes the best possible action. The KI uses a mathematical model']

        # Init the ui elements
        self.build_ui(parent)

    def build_ui(self, parent):
        """
        Creates all UI elements of the panel
        :return: None
        """
        content_panel = wx.Panel(self)

        # Create the ListBox, which shows all possible players
        player_list_box = wx.ListBox(content_panel, size=(-1, -1), choices=self.players, style=wx.LB_SINGLE)
        player_list_box.SetFont(FONTS.TXT_NORMAL)

        player_list_box.Bind(wx.EVT_LISTBOX, self.list_box_selected)
        player_list_box.Bind(wx.EVT_LISTBOX_DCLICK, self.list_box_selected)

        # Create a panel on the right which sows detailed information about the player
        details_panel = wx.Panel(content_panel)
        details_box = wx.StaticBox(details_panel, label='Details')
        details_box.SetFont(FONTS.TXT_BIG)
        details_bsizer = wx.StaticBoxSizer(details_box, orient=wx.VERTICAL)
        self.detail_text = wx.StaticText(details_box, label="Description of the player ...", style=wx.TE_MULTILINE)
        self.detail_text.SetFont(FONTS.TXT_NORMAL)
        details_bsizer.Add(self.detail_text)
        details_panel.SetSizer(details_bsizer)

        # Place 'listBox' on the left and 'details_panel' on the right
        sizer_2cols = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2cols.Add(player_list_box, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        sizer_2cols.Add(details_panel, 1, wx.ALIGN_LEFT | wx.ALL | wx.EXPAND, 5)

        # Wrap the content in a box
        content_box = wx.StaticBox(content_panel, label='Select a player')
        content_box.SetFont(FONTS.SUB_MENUE_ITEM)
        content_bsizer = wx.StaticBoxSizer(content_box, orient=wx.VERTICAL)
        content_bsizer.Add(sizer_2cols)
        content_panel.SetSizer(content_bsizer)

        # Cancel and save button
        hsizer_buttons = wx.BoxSizer(wx.HORIZONTAL)
        saveButton = wx.Button(self, label='Save')
        saveButton.Bind(wx.EVT_BUTTON, self.save_button_clicked)
        cancelButton = wx.Button(self, label='Cancel')
        cancelButton.Bind(wx.EVT_BUTTON, self.cancel_button_clicked)
        hsizer_buttons.Add(saveButton, flag=wx.RIGHT)
        hsizer_buttons.Add(cancelButton, flag=wx.LEFT, border=5)

        # Set the content box at top and buttons at the bottom
        vertical_box = wx.BoxSizer(wx.VERTICAL)
        vertical_box.Add(content_panel, 2, wx.EXPAND | wx.RIGHT, border=5)
        vertical_box.AddStretchSpacer(1)
        vertical_box.Add(hsizer_buttons, 0, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        self.SetSizerAndFit(vertical_box)

    def list_box_selected(self, evt):
        """
        Action when user selects a item on the player seelct box
        :param evt: The wx event object
        :return:
        """
        player_id = evt.Int
        new_details_txt = self.info_text[player_id]
        self.detail_text.SetLabel(new_details_txt)
        self.Layout()

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