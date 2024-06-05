import wx
import wx.adv
import datetime

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        self.current_date = datetime.datetime.today()
        self.InitUI()
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_timer, self.timer)
        self.start_time = None

    def InitUI(self):
        self.SetTitle('Navigation Example')
        self.Maximize(True)

        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Create a dark grey navbar
        navbar = wx.Panel(panel, size=(-1, 50))
        navbar.SetBackgroundColour(wx.Colour(50, 50, 50))
        nav_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Left buttons
        self.create_nav_button(navbar, nav_sizer, "Activity", self.OnActivity)
        self.create_nav_button(navbar, nav_sizer, "Timeline", self.OnTimeline)
        self.create_nav_button(navbar, nav_sizer, "StopWatch", self.OnStopWatch)

        # Center label
        nav_sizer.AddStretchSpacer()
        center_label = wx.StaticText(navbar, label="Center")
        center_label.SetForegroundColour(wx.Colour(255, 255, 255))
        nav_sizer.Add(center_label, 0, wx.ALIGN_CENTER_VERTICAL)
        nav_sizer.AddStretchSpacer()

        # Right buttons
        tools_button = wx.Button(navbar, label="Tools")
        tools_menu = wx.Menu()
        tools_menu.Append(wx.ID_ANY, 'Search')
        tools_menu.Append(wx.ID_ANY, 'Query')
        tools_button.Bind(wx.EVT_BUTTON, lambda event: self.PopupMenu(tools_menu, tools_button.GetPosition()))
        nav_sizer.Add(tools_button, 0, wx.ALL, 5)

        self.create_nav_button(navbar, nav_sizer, "Raw Data", self.OnRawData)
        self.create_nav_button(navbar, nav_sizer, "Settings", self.OnSettings)

        navbar.SetSizer(nav_sizer)
        main_sizer.Add(navbar, 0, wx.EXPAND)

        # Main content area
        content_panel = wx.Panel(panel)
        content_panel.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.content_sizer = wx.BoxSizer(wx.VERTICAL)

        self.content_box = wx.Panel(content_panel, size=(800, 600))
        self.content_box.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.content_box.SetWindowStyle(wx.BORDER_RAISED)
        self.content_sizer.AddStretchSpacer()
        self.content_sizer.Add(self.content_box, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.content_sizer.AddStretchSpacer()
        content_panel.SetSizer(self.content_sizer)
        main_sizer.Add(content_panel, 1, wx.EXPAND)

        panel.SetSizer(main_sizer)

        # Initialize with the Activity page
        self.OnActivity(None)

    def create_nav_button(self, parent, sizer, label, handler):
        btn = wx.Button(parent, label=label)
        btn.Bind(wx.EVT_BUTTON, handler)
        sizer.Add(btn, 0, wx.ALL, 5)

    def clear_content(self):
        for child in self.content_box.GetChildren():
            child.Destroy()
        self.content_box.Layout()

    def OnActivity(self, event):
        self.clear_content()
        vbox = wx.BoxSizer(wx.VERTICAL)
        date_str = self.current_date.strftime('%Y-%m-%d')
        title = wx.StaticText(self.content_box, label=f"Activity for {date_str}")
        title.SetFont(wx.Font(36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        vbox.Add(title, 0, wx.ALIGN_CENTER | wx.TOP, 20)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        subtract_btn = wx.Button(self.content_box, label="-1")
        subtract_btn.Bind(wx.EVT_BUTTON, self.OnSubtract)
        hbox.Add(subtract_btn, 0, wx.ALL, 5)

        self.dropdown = wx.Choice(self.content_box, choices=["Day", "Week", "Month"])
        self.dropdown.SetSelection(0)
        hbox.Add(self.dropdown, 0, wx.ALL, 5)

        add_btn = wx.Button(self.content_box, label="+1")
        add_btn.Bind(wx.EVT_BUTTON, self.OnAdd)
        hbox.Add(add_btn, 0, wx.ALL, 5)

        vbox.Add(hbox, 0, wx.ALIGN_CENTER | wx.TOP, 20)

        self.calendar = wx.adv.CalendarCtrl(self.content_box, style=wx.adv.CAL_SHOW_HOLIDAYS)
        self.calendar.Bind(wx.adv.EVT_CALENDAR, self.OnCalendar)
        vbox.Add(self.calendar, 0, wx.ALIGN_CENTER | wx.TOP, 20)

        self.content_box.SetSizer(vbox)

    def OnSubtract(self, event):
        selection = self.dropdown.GetStringSelection()
        if selection == "Day":
            self.current_date -= datetime.timedelta(days=1)
        elif selection == "Week":
            self.current_date -= datetime.timedelta(weeks=1)
        elif selection == "Month":
            self.current_date -= datetime.timedelta(days=30)  # Approximation
        self.OnActivity(None)

    def OnAdd(self, event):
        selection = self.dropdown.GetStringSelection()
        if selection == "Day":
            self.current_date += datetime.timedelta(days=1)
        elif selection == "Week":
            self.current_date += datetime.timedelta(weeks=1)
        elif selection == "Month":
            self.current_date += datetime.timedelta(days=30)  # Approximation
        self.OnActivity(None)

    def OnCalendar(self, event):
        self.current_date = self.calendar.GetDate().GetTm()
        self.OnActivity(None)

    def OnTimeline(self, event):
        self.clear_content()
        vbox = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(self.content_box, label="Timeline")
        title.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        vbox.Add(title, 0, wx.ALIGN_CENTER | wx.TOP, 20)
        self.content_box.SetSizer(vbox)

    def OnStopWatch(self, event):
        self.clear_content()
        vbox = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(self.content_box, label="StopWatch")
        title.SetFont(wx.Font(36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        vbox.Add(title, 0, wx.ALIGN_CENTER | wx.TOP, 20)

        self.timer_display = wx.StaticText(self.content_box, label="00:00:00")
        self.timer_display.SetFont(wx.Font(48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        vbox.Add(self.timer_display, 0, wx.ALIGN_CENTER | wx.TOP, 50)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        start_button = wx.Button(self.content_box, label="Start")
        start_button.Bind(wx.EVT_BUTTON, self.OnStartTimer)
        hbox.Add(start_button, 0, wx.ALL, 5)

        stop_button = wx.Button(self.content_box, label="Stop")
        stop_button.Bind(wx.EVT_BUTTON, self.OnStopTimer)
        hbox.Add(stop_button, 0, wx.ALL, 5)

        vbox.Add(hbox, 0, wx.ALIGN_CENTER | wx.TOP, 20)
        self.content_box.SetSizer(vbox)

    def update_timer(self, event):
        elapsed_time = datetime.datetime.now() - self.start_time
        elapsed_str = str(elapsed_time).split('.')[0]
        self.timer_display.SetLabel(elapsed_str)

    def OnStartTimer(self, event):
        self.start_time = datetime.datetime.now()
        self.timer.Start(1000)

    def OnStopTimer(self, event):
        self.timer.Stop()

    def OnRawData(self, event):
        self.clear_content()
        vbox = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(self.content_box, label="Raw Data")
        title.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        vbox.Add(title, 0, wx.ALIGN_CENTER | wx.TOP, 20)
        self.content_box.SetSizer(vbox)

    def OnSettings(self, event):
        self.clear_content()
        vbox = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(self.content_box, label="Settings")
        title.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        vbox.Add(title, 0, wx.ALIGN_CENTER | wx.TOP, 20)
        self.content_box.SetSizer(vbox)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None)
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
