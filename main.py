import wx
from WindowApp import WindowApp


def main():
    app = wx.App()
    example = WindowApp(None, title="WindowApp")
    example.Show()
    app.MainLoop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
