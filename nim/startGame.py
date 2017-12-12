import wx


print("Starting nim game ...")
app = wx.App()

from ui.MainWindow import MainWindow
ui = MainWindow()

app.MainLoop()
