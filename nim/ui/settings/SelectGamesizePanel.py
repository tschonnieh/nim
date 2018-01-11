import wx
import pickle

from Event import *
import ui.res.values.colors as COLORS
import ui.res.values.fonts as FONTS


class SelectGamesizePanel(wx.Panel):
    """
    The panel allows the user to select the size of the game
    """

    def __init__(self, parent):
        super(SelectGamesizePanel, self).__init__(parent)

        self.SetBackgroundColour(COLORS.SETTINGS_DETAILS_BG)
        self.SetSize(parent.Size)

        self.button_sizes = [[3, 3, 3], [3, 2, 1], [4, 3, 2], [5, 4, 3], [6, 5, 4], [7, 6, 5]]
        self.selected_rbutton_id = 0

        # Restore last config if set
        self.config = wx.Config("NimGame")
        cur_size_str = self.config.Read("gamesize", "[3, 2, 1]")
        cur_size = cur_size_str.strip('[]').split(', ')
        cur_size = list(map(int, cur_size))

        for (i, btn_size) in enumerate(self.button_sizes):
            if btn_size == cur_size:
                self.selected_rbutton_id = i
                break

        # The events
        self.evt_back = Event()

        # Init the ui elements
        self.build_ui()

    def build_ui(self):
        """
        Creates all UI elements of the panel
        :return: None
        """
        content_panel = wx.Panel(self)
        content_box = wx.StaticBox(content_panel, label='Select the gamesize')
        content_box.SetFont(FONTS.SUB_MENUE_ITEM)
        content_vbox_sizer = wx.StaticBoxSizer(content_box, orient=wx.VERTICAL)

        # Create radio buttons
        self.radio_buttons = []
        for btn_size in self.button_sizes:
            radio_btn = wx.RadioButton(content_panel, label=str(btn_size))
            radio_btn.SetFont(FONTS.TXT_NORMAL)
            self.radio_buttons.append(radio_btn)

        # Add radio buttons to content_box_sizer
        for radio_btn in self.radio_buttons:
            content_vbox_sizer.Add(radio_btn, 0, wx.LEFT, 5)
            content_vbox_sizer.AddSpacer(3)
        content_panel.SetSizer(content_vbox_sizer)

        # Create the radio button for a custom gamesize
        #custom_button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        #radio_btn_custom = wx.RadioButton(content_panel, label='Custom')
        #radio_btn_custom.SetFont(FONTS.TXT_NORMAL)
        #self.radio_buttons.append(radio_btn_custom)
        #txt_ctrl_custom = wx.TextCtrl(content_panel)
        #txt_ctrl_custom.SetFont(FONTS.TXT_NORMAL)
        #custom_button_sizer.Add(radio_btn_custom)
        #custom_button_sizer.Add(txt_ctrl_custom, flag=wx.LEFT, border=5)
        #content_vbox_sizer.Add(custom_button_sizer, 0, wx.LEFT, 5)

        # Aligns butttons horizontal
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        saveButton = wx.Button(self, label='Save')
        saveButton.Bind(wx.EVT_BUTTON, self.save_button_clicked)
        cancelButton = wx.Button(self, label='Cancel')
        cancelButton.Bind(wx.EVT_BUTTON, self.cancel_button_clicked)
        button_sizer.Add(cancelButton, flag=wx.RIGHT)
        button_sizer.Add(saveButton, flag=wx.LEFT, border=5)

        # Place content on the top and buttons at bottom
        vertical_box = wx.BoxSizer(wx.VERTICAL)
        vertical_box.AddSpacer(3)
        vertical_box.Add(content_panel, proportion=2, flag=wx.EXPAND | wx.RIGHT, border=5)
        vertical_box.AddStretchSpacer(1)
        vertical_box.Add(button_sizer, 0, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        self.radio_buttons[self.selected_rbutton_id].SetValue(True)

        self.SetSizerAndFit(vertical_box)

    def save_button_clicked(self, evt):
        """
        Action when the 'save' button is clicked
        :param evt: The wx event object
        :return:
        """
        # If custom size button is clicked
        if self.radio_buttons[len(self.radio_buttons) - 1].GetValue() == True:
            print("Custom size not implemented")
            wx.MessageBox('Custom size not implemented', 'Error', wx.OK | wx.ICON_ERROR)
            return

        # If button with predefined size is clicked
        for (i, btn) in enumerate(self.radio_buttons):
            if btn.GetValue() == True:
                selected_size = self.button_sizes[i]
                saving_message = "game size: {}".format(selected_size)
                print(saving_message)
                wx.MessageBox(saving_message, 'Successfully saved changes', wx.OK | wx.ICON_INFORMATION)
                self.config.Write("gamesize", str(selected_size))
                self.config.Flush()

    def cancel_button_clicked(selfself, evt):
        """
        Action when the 'cancel' button is clicked
        :param evt: The wx event object
        :return:
        """
        print("Cancel clicked")
