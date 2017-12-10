from wx import *

import nim.ui.res.values.colors as col


class MainGamePanel(Panel):

    def __init__(self, parent, **args):
        super(MainGamePanel, self).__init__(parent)

        # Set MainMenuePanel color and to fullscreen
        self.SetBackgroundColour(col.MAIN_MENUE_BG)
        self.SetSize(parent.Size)

        # Init the ui elements
        self.build_ui(parent)

    def build_ui(self, parent):
        p_demo = StaticText(parent=self, style=ALIGN_CENTRE)
        p_demo.SetLabel("Implementation of 'MainGamePanel' is missing ;)")
        p_demo.SetSize((300, -1))
        p_demo.SetPosition((10, 10))
