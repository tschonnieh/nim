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
        self.build_ui(parent)
        self.Layout()

    def build_ui(self, parent):

        pearls_panel = wx.Panel(self, size=(300, 300), pos=(100, 100))

        pearl1 = SButton(pearls_panel, label="O", size=(30, 30))
        pearl2 = SButton(pearls_panel, label="O", size=(30, 30))
        pearl3 = SButton(pearls_panel, label="O", size=(30, 30))

        grid_sizer = wx.GridSizer(rows=3, cols=3, hgap=5, vgap=5)

        grid_sizer.Add(pearl1)
        grid_sizer.Add(pearl2)
        grid_sizer.Add(pearl3)

        #vsizer = wx.BoxSizer(wx.VERTICAL)
        #vsizer.Add(demo_btn, 0)
        #vsizer.Add(draw_panel, 1, wx.EXPAND)
        pearls_panel.SetSizer(grid_sizer)
