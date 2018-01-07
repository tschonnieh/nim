import wx

from Event import *
from player.PlayerDict import ALL_PLAYERS
import ui.res.values.colors as COLORS
import ui.res.values.fonts as FONTS


class SelectPlayerPanel(wx.Panel):
    """
    The panel allows the user to select the two players, which shall play the game
    """

    def __init__(self, parent, player_number):
        """
        Constructor
        :param parent: The parent ui element
        :param player_number: The number of the player to select e.G. [0, 1]
        """
        super(SelectPlayerPanel, self).__init__(parent)
        self.SetBackgroundColour(COLORS.SETTINGS_DETAILS_BG)
        self.SetSize(parent.Size)

        self.player_number = player_number

        self.config = wx.Config("NimGame")
        self.cur_ptype_selection = self.config.ReadInt("player" + str(player_number), 0)

        # The events
        self.evt_back = Event()

        # Get the playertype data for the list box
        self.player_texts = [player.name for player in ALL_PLAYERS]
        self.info_text = [player.description for player in ALL_PLAYERS]

        # Init the ui elements
        self.build_ui(parent)

    def build_ui(self, parent):
        """
        Creates all UI elements of the panel
        :return: None
        """
        content_panel = wx.Panel(self)

        # Create the ListBox, which shows all possible players
        self.player_list_box = wx.ListBox(content_panel, size=(-1, -1), choices=self.player_texts, style=wx.LB_SINGLE)
        self.player_list_box.SetFont(FONTS.TXT_NORMAL)
        self.player_list_box.SetSelection(self.cur_ptype_selection)

        self.player_list_box.Bind(wx.EVT_LISTBOX, self.list_box_selected)
        self.player_list_box.Bind(wx.EVT_LISTBOX_DCLICK, self.list_box_selected)

        # Create a panel on the right which sows detailed information about the player
        details_panel = wx.Panel(content_panel)
        details_box = wx.StaticBox(details_panel, label='Details')
        details_box.SetFont(FONTS.TXT_BIG)
        details_bsizer = wx.StaticBoxSizer(details_box, orient=wx.VERTICAL)
        self.detail_text = wx.StaticText(details_box, label=ALL_PLAYERS[self.cur_ptype_selection].description, style=wx.TE_MULTILINE)
        self.detail_text.SetFont(FONTS.TXT_NORMAL)
        details_bsizer.Add(self.detail_text)
        details_panel.SetSizer(details_bsizer)

        # Place 'listBox' on the left and 'details_panel' on the right
        sizer_2cols = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2cols.Add(self.player_list_box, 0, wx.ALIGN_LEFT | wx.ALL, 5)
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
        Action when user selects a item on the player select box
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
        player_selection_id = self.player_list_box.GetSelection()
        save_message = "Player type for player {}: '{}'".format(self.player_number, ALL_PLAYERS[player_selection_id].name)
        print(save_message)
        wx.MessageBox(save_message, 'Successfully saved changes', wx.OK | wx.ICON_INFORMATION)
        self.config.WriteInt("player" + str(self.player_number), player_selection_id)
        self.config.Flush()

    def cancel_button_clicked(selfself, evt):
        """
        Action when the 'cancel' button is clicked
        :param evt: The wx event object
        :return:
        """
        print("Cancel clicked")
