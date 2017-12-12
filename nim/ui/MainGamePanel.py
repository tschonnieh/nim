import wx
from wx.lib.agw.shapedbutton import SButton, SBitmapButton

import ui.res.values.colors as col


class MainGamePanel(wx.Panel):

    def __init__(self, parent, **args):
        super(MainGamePanel, self).__init__(parent)

        # Set MainMenuePanel color and to fullscreen
        self.SetBackgroundColour(col.MAIN_MENUE_BG)
        self.SetSize(parent.Size)

        # Init the ui elements
        self.build_ui()
        self.Layout()

    def build_ui(self):

        pearls_panel = self.create_pearls_panel([3, 2, 1])

        pearls_panel.Bind(wx.EVT_BUTTON, self.btn_clicked)

        # Create bottom area
        buttons_panel = wx.Panel(self)
        btn_turn = wx.Button(buttons_panel, label='make turn')
        btn_reset = wx.Button(buttons_panel, label='reset')

        # Adjust buttons horizontal
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(btn_reset, 1, wx.CENTER, 10)
        btn_sizer.AddSpacer(10)
        btn_sizer.Add(btn_turn, 1, wx.CENTER, 10)
        buttons_panel.SetSizer(btn_sizer)

        # Set the positions of the 'pearls'- and 'buttons'-panel
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(pearls_panel, wx.EXPAND)
        main_sizer.Add(buttons_panel, 0, wx.ALL | wx.CENTER, 10)
        self.SetSizer(main_sizer)

    def create_pearls_panel(self, row_sizes):
        """
        Creates the panel, which contains the pearls
        :return: The panel containing the pearls
        """
        pearls_panel = wx.Panel(self)
        btn_size = (35, 35)

        # First row
        pearl11 = SButton(pearls_panel, label="", size=btn_size)
        pearl12 = SButton(pearls_panel, label="", size=btn_size)
        pearl13 = SButton(pearls_panel, label="", size=btn_size)

        pearls_row1 = wx.BoxSizer(wx.HORIZONTAL)
        pearls_row1.Add(pearl11, proportion=0, flag=wx.ALIGN_LEFT, border=0)
        pearls_row1.AddSpacer(5)
        pearls_row1.Add(pearl12, proportion=0, flag=wx.ALIGN_LEFT, border=0)
        pearls_row1.AddSpacer(5)
        pearls_row1.Add(pearl13, proportion=0, flag=wx.ALIGN_LEFT, border=0)

        # Second row
        pearl21 = SButton(pearls_panel, label="", size=btn_size)
        pearl22 = SButton(pearls_panel, label="", size=btn_size)

        pearls_row2 = wx.BoxSizer(wx.HORIZONTAL)
        pearls_row2.Add(pearl21, proportion=0, flag=wx.ALIGN_LEFT, border=0)
        pearls_row2.AddSpacer(5)
        pearls_row2.Add(pearl22, proportion=0, flag=wx.ALIGN_LEFT, border=0)

        # Third row
        pearl31 = SButton(pearls_panel, label="", size=btn_size)

        pearls_row3 = wx.BoxSizer(wx.HORIZONTAL)
        pearls_row3.Add(pearl31, proportion=0, flag=wx.ALIGN_LEFT, border=0)

        # Align all pearl rows vertical
        rows_sizer = wx.BoxSizer(wx.VERTICAL)
        rows_sizer.Add(pearls_row1)
        rows_sizer.AddSpacer(3)
        rows_sizer.Add(pearls_row2)
        rows_sizer.AddSpacer(3)
        rows_sizer.Add(pearls_row3)
        pearls_panel.SetSizer(rows_sizer)

        return pearls_panel

    def btn_clicked(self, evt):
        print(evt)