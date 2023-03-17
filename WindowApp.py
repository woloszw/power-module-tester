import wx


class WindowApp(wx.Frame):
    def __init__(self, parent, title):
        super(WindowApp, self).__init__(parent, title=title, size=(1000, 1000))
        self.st2 = None
        self.st1 = None
        self.col = None
        self.InitUI()
        self.Centre()
    def InitUI(self):
        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        font = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.DEFAULT)

        self.st1 = wx.StaticText(pnl, label="connected", style=wx.ALIGN_CENTER, pos=(12, 12))
        self.st2 = wx.StaticText(pnl, label="not connected", style=wx.ALIGN_CENTER, pos=(12, 12))
        self.st1.Hide()
        text_boxes=[]

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        for i in range(0,10):
            text_boxes.append(wx.TextCtrl(pnl, size=(60,20), pos=(12+63*i, 50)))
            hbox1.Add(text_boxes[i], flag=wx.RIGHT)

        self.col = wx.Colour(0, 0, 0)


        connect_button = wx.ToggleButton(pnl, label='Connect', pos=(120, 12))

        self.st1.SetFont(font)
        self.st2.SetFont(font)

        vbox.Add(self.st1, flag=wx.ALL, border=15)

        pnl.SetSizer(vbox)

        connect_button.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_connect)

        self.SetTitle('Toggle buttons')
        self.Centre()

        dlg = wx.TextEntryDialog(self, 'Enter Your Name', 'Text Entry Dialog')
        dlg.Show()
        print(dlg.GetValue())

    def toggle_connect(self, e):

        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        if isPressed:
            self.st2.Hide()
            self.st1.Show()

        else:
            self.st2.Show()
            self.st1.Hide()
