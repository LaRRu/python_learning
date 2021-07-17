'''Build a counter app.
Take your first steps into the world of UI
by building a very simple app
that counts up by one each time a user clicks a button.
'''
import wx


class CounterApp(wx.Frame):
    def __init__(self):
        super().__init__(
            None,
            wx.ID_ANY,
            title='Clicks counter app',
            style=wx.DEFAULT_FRAME_STYLE &
            ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),
            size=wx.Size(200, 100))

        self.click_count = 0
        self.InitUI()
        self.Center()

    def InitUI(self):
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.BtnSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.clickBtn = wx.Button(self, label='Click Me!')
        self.clickBtn.Bind(wx.EVT_BUTTON, self.OnClick, self.clickBtn)
        self.BtnSizer.Add(self.clickBtn, 0, wx.ALL | wx.CENTER, 5)

        self.label = wx.StaticText(self, label=f'Clicks: {self.click_count}')
        self.main_sizer.Add(self.label, 0, wx.ALL | wx.CENTER, 5)

        self.clearBtn = wx.Button(self, label='Clear count')
        self.clearBtn.Bind(wx.EVT_BUTTON, self.OnClick, self.clearBtn)
        self.BtnSizer.Add(self.clearBtn, 0, wx.ALL | wx.CENTER, 5)

        self.main_sizer.Add(self.BtnSizer, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(self.main_sizer)
        self.Show()

    def OnClick(self, event):
        event_id = event.GetId()
        if event_id == self.clickBtn.GetId():
            self.click_count += 1
        if event_id == self.clearBtn.GetId():
            self.click_count = 0
        self.label.SetLabel(f'Clicks: {self.click_count}')


if __name__ == '__main__':
    app = wx.App()
    CounterApp()
    app.MainLoop()
