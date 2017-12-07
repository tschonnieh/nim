import wx


print("Starting nim game ...")
app = wx.App()

from nim.ui.MainWindow import MainWindow
ui = MainWindow()

app.MainLoop()
