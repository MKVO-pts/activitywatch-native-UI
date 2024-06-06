import wx
import wx.adv
import datetime

class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)

        self.InitUI()
        
    def InitUI(self):
        self.panel = wx.Panel(self)

        self.navbar = wx.Panel(self.panel, size=(-1, 50), style=wx.BORDER_SIMPLE)
        self.navbar.SetBackgroundColour('#333333')

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.navbar_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.content_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Navbar buttons (left)
        self.activity_btn = wx.Button(self.navbar, label="Activity")
        self.timeline_btn = wx.Button(self.navbar, label="Timeline")
        self.stopwatch_btn = wx.Button(self.navbar, label="StopWatch")
        
        self.navbar_sizer.Add(self.activity_btn, flag=wx.ALL, border=5)
        self.navbar_sizer.Add(self.timeline_btn, flag=wx.ALL, border=5)
        self.navbar_sizer.Add(self.stopwatch_btn, flag=wx.ALL, border=5)
        
        # Center label
        center_label = wx.StaticText(self.navbar, label="Center")
        center_label.SetForegroundColour(wx.WHITE)
        self.navbar_sizer.Add(center_label, proportion=1, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL)
        
        # Navbar buttons (right)
        tools_btn = wx.Button(self.navbar, label="Tools")
        tools_menu = wx.Menu()
        tools_menu.Append(wx.ID_ANY, "Search")
        tools_menu.Append(wx.ID_ANY, "Query")
        tools_btn.Bind(wx.EVT_BUTTON, self.OnToolsMenu)
        
        self.navbar_sizer.Add(tools_btn, flag=wx.ALL, border=5)
        
        self.rawdata_btn = wx.Button(self.navbar, label="Raw Data")
        self.settings_btn = wx.Button(self.navbar, label="Settings")
        
        self.navbar_sizer.Add(self.rawdata_btn, flag=wx.ALL, border=5)
        self.navbar_sizer.Add(self.settings_btn, flag=wx.ALL, border=5)

        self.navbar.SetSizer(self.navbar_sizer)
        self.sizer.Add(self.navbar, flag=wx.EXPAND)
        
        # Content area
        self.content_panel = wx.Panel(self.panel)
        self.content_panel.SetBackgroundColour('#D3D3D3')
        
        self.white_box = wx.Panel(self.content_panel, size=(1100, 700), style=wx.BORDER_SIMPLE)
        self.white_box.SetBackgroundColour(wx.WHITE)
        self.white_box_sizer = wx.BoxSizer(wx.VERTICAL)
        self.white_box.SetSizer(self.white_box_sizer)
        
        self.content_sizer.AddStretchSpacer(1)
        self.content_sizer.Add(self.white_box, flag=wx.ALIGN_CENTER_VERTICAL)
        self.content_sizer.AddStretchSpacer(1)
        
        self.content_panel.SetSizer(self.content_sizer)
        self.sizer.Add(self.content_panel, proportion=1, flag=wx.EXPAND)

        self.panel.SetSizer(self.sizer)

        # Event bindings
        self.Bind(wx.EVT_BUTTON, self.OnActivity, self.activity_btn)
        self.Bind(wx.EVT_BUTTON, self.OnTimeline, self.timeline_btn)
        self.Bind(wx.EVT_BUTTON, self.OnStopWatch, self.stopwatch_btn)
        self.Bind(wx.EVT_BUTTON, self.OnRawData, self.rawdata_btn)
        self.Bind(wx.EVT_BUTTON, self.OnSettings, self.settings_btn)
        
        self.SetSize((1200, 800))
        self.Centre()
        self.Show(True)
        
    def ClearContent(self):
        for child in self.white_box.GetChildren():
            child.Destroy()

    def OnActivity(self, event):
        self.ClearContent()
        
        today = datetime.date.today().strftime('%Y-%m-%d')
        title = wx.StaticText(self.white_box, label=f"Activity for {today}")
        self.white_box_sizer.Add(title, flag=wx.ALL|wx.ALIGN_CENTER, border=10)
        
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        left_btn = wx.Button(self.white_box, label="-1")
        center_btn = wx.ComboBox(self.white_box, choices=["Day", "Week", "Month"])
        right_btn = wx.Button(self.white_box, label="+1")
        
        button_sizer.Add(left_btn, flag=wx.ALL, border=5)
        button_sizer.Add(center_btn, flag=wx.ALL, border=5)
        button_sizer.Add(right_btn, flag=wx.ALL, border=5)
        
        self.white_box_sizer.Add(button_sizer, flag=wx.ALIGN_CENTER)
        
        calendar = wx.adv.CalendarCtrl(self.white_box)
        self.white_box_sizer.Add(calendar, flag=wx.ALL|wx.ALIGN_CENTER, border=10)
        
        yellow_box = wx.Panel(self.white_box, size=(-1, 50), style=wx.BORDER_SIMPLE)
        yellow_box.SetBackgroundColour('#FFFFE0')
        self.white_box_sizer.Add(yellow_box, flag=wx.EXPAND|wx.ALL, border=10)
        
        buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
        summary_btn = wx.Button(self.white_box, label="Summary")
        window_btn = wx.Button(self.white_box, label="Window")
        browser_btn = wx.Button(self.white_box, label="Browser")
        editor_btn = wx.Button(self.white_box, label="Editor")
        
        buttons_sizer.Add(summary_btn, flag=wx.ALL, border=5)
        buttons_sizer.Add(window_btn, flag=wx.ALL, border=5)
        buttons_sizer.Add(browser_btn, flag=wx.ALL, border=5)
        buttons_sizer.Add(editor_btn, flag=wx.ALL, border=5)
        
        self.white_box_sizer.Add(buttons_sizer, flag=wx.ALIGN_CENTER)
        
        grid_sizer = wx.GridSizer(2, 3, 10, 10)
        
        grid_sizer.Add(wx.StaticText(self.white_box, label="Top Applications"), flag=wx.ALL, border=5)
        grid_sizer.Add(wx.StaticText(self.white_box, label="Top Window Title"), flag=wx.ALL, border=5)
        grid_sizer.Add(wx.StaticText(self.white_box, label="Timeline (barchart)"), flag=wx.ALL, border=5)
        grid_sizer.Add(wx.StaticText(self.white_box, label="Top Categories"), flag=wx.ALL, border=5)
        grid_sizer.Add(wx.StaticText(self.white_box, label="Category Tree"), flag=wx.ALL, border=5)
        grid_sizer.Add(wx.StaticText(self.white_box, label="Category Sunburst"), flag=wx.ALL, border=5)
        
        self.white_box_sizer.Add(grid_sizer, flag=wx.ALIGN_CENTER|wx.ALL, border=10)
        
        self.white_box.Layout()

    def OnTimeline(self, event):
        self.ClearContent()
        
        title = wx.StaticText(self.white_box, label="Timeline")
        self.white_box_sizer.Add(title, flag=wx.ALL|wx.ALIGN_CENTER, border=10)
        
        interval_mode_label = wx.StaticText(self.white_box, label="Interval mode : ")
        interval_mode = wx.ComboBox(self.white_box, choices=["Last durations", "Range"])
        show_last_label = wx.StaticText(self.white_box, label="Show Last : ")
        show_last = wx.ComboBox(self.white_box, choices=["15min", "30min", "1h", "2h", "3h", "4h", "6h", "12h", "24h"])
        
        self.white_box_sizer.Add(interval_mode_label, flag=wx.ALL, border=5)
        self.white_box_sizer.Add(interval_mode, flag=wx.ALL|wx.EXPAND, border=5)
        self.white_box_sizer.Add(show_last_label, flag=wx.ALL, border=5)
        self.white_box_sizer.Add(show_last, flag=wx.ALL|wx.EXPAND, border=5)
        
        events_shown_label = wx.StaticText(self.white_box, label="Events shown")
        self.white_box_sizer.Add(events_shown_label, flag=wx.ALL, border=10)
        
        grid_sizer = wx.GridSizer(2, 2, 10, 10)
        
        for i in range(4):
            grid_sizer.Add(wx.Panel(self.white_box, size=(200, 100), style=wx.BORDER_SIMPLE), flag=wx.ALL, border=5)
        
        self.white_box_sizer.Add(grid_sizer, flag=wx.ALIGN_CENTER|wx.ALL, border=10)
        
        self.white_box.Layout()

    def OnStopWatch(self, event):
        self.ClearContent()
        
        title = wx.StaticText(self.white_box, label="StopWatch")
        self.white_box_sizer.Add(title, flag=wx.ALL|wx.ALIGN_CENTER, border=10)
        
        self.time_display = wx.StaticText(self.white_box, label="00:00:00", style=wx.ALIGN_CENTER)
        font = self.time_display.GetFont()
        font.PointSize += 20
        self.time_display.SetFont(font)
        self.white_box_sizer.Add(self.time_display, flag=wx.ALL|wx.ALIGN_CENTER, border=10)
        
        buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.start_btn = wx.Button(self.white_box, label="Start")
        self.stop_btn = wx.Button(self.white_box, label="Stop")
        
        buttons_sizer.Add(self.start_btn, flag=wx.ALL, border=5)
        buttons_sizer.Add(self.stop_btn, flag=wx.ALL, border=5)
        
        self.white_box_sizer.Add(buttons_sizer, flag=wx.ALIGN_CENTER)
        
        self.start_btn.Bind(wx.EVT_BUTTON, self.OnStart)
        self.stop_btn.Bind(wx.EVT_BUTTON, self.OnStop)
        
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        
        self.start_time = None
        
        self.white_box.Layout()

    def OnStart(self, event):
        self.start_time = datetime.datetime.now()
        self.timer.Start(1000)

    def OnStop(self, event):
        self.timer.Stop()

    def OnTimer(self, event):
        if self.start_time:
            elapsed = datetime.datetime.now() - self.start_time
            self.time_display.SetLabel(str(elapsed).split('.')[0])

    def OnToolsMenu(self, event):
        tools_menu = wx.Menu()
        tools_menu.Append(wx.ID_ANY, "Search")
        tools_menu.Append(wx.ID_ANY, "Query")
        self.PopupMenu(tools_menu)

    def OnRawData(self, event):
        self.ClearContent()
        
        title = wx.StaticText(self.white_box, label="Buckets")
        self.white_box_sizer.Add(title, flag=wx.ALL|wx.ALIGN_CENTER, border=10)
        
        grid_sizer = wx.GridSizer(4, 8, 10, 10)
        
        columns = ["Bucket ID", "Hostname", "Updated", "Files"]
        
        for col in columns:
            grid_sizer.Add(wx.StaticText(self.white_box, label=col), flag=wx.ALL, border=5)
        
        for _ in range(32):
            grid_sizer.Add(wx.Panel(self.white_box, size=(100, 50), style=wx.BORDER_SIMPLE), flag=wx.ALL, border=5)
        
        self.white_box_sizer.Add(grid_sizer, flag=wx.ALIGN_CENTER|wx.ALL, border=10)
        
        label = wx.StaticText(self.white_box, label="Import and export buckets")
        self.white_box_sizer.Add(label, flag=wx.ALL, border=10)
        
        table_sizer = wx.GridSizer(2, 2, 10, 10)
        
        table_sizer.Add(wx.StaticText(self.white_box, label="Import buckets"), flag=wx.ALL, border=5)
        table_sizer.Add(wx.StaticText(self.white_box, label="Export buckets"), flag=wx.ALL, border=5)
        table_sizer.Add(wx.Panel(self.white_box, size=(200, 100), style=wx.BORDER_SIMPLE), flag=wx.ALL, border=5)
        table_sizer.Add(wx.Panel(self.white_box, size=(200, 100), style=wx.BORDER_SIMPLE), flag=wx.ALL, border=5)
        
        self.white_box_sizer.Add(table_sizer, flag=wx.ALIGN_CENTER|wx.ALL, border=10)
        
        self.white_box.Layout()

    def OnSettings(self, event):
        self.ClearContent()
        
        title = wx.StaticText(self.white_box, label="Settings")
        self.white_box_sizer.Add(title, flag=wx.ALL|wx.ALIGN_CENTER, border=10)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        start_of_day_sizer = wx.BoxSizer(wx.HORIZONTAL)
        start_of_day_label = wx.StaticText(self.white_box, label="Start of day")
        start_of_day_dropdown = wx.ComboBox(self.white_box, choices=["Yes", "No"])
        
        start_of_day_sizer.Add(start_of_day_label, flag=wx.ALL, border=5)
        start_of_day_sizer.Add(start_of_day_dropdown, flag=wx.ALL|wx.EXPAND, border=5)
        
        sizer.Add(start_of_day_sizer, flag=wx.ALL|wx.EXPAND, border=5)
        
        theme_sizer = wx.BoxSizer(wx.HORIZONTAL)
        theme_label = wx.StaticText(self.white_box, label="Theme")
        theme_dropdown = wx.ComboBox(self.white_box, choices=["Light", "Dark"])
        
        theme_sizer.Add(theme_label, flag=wx.ALL, border=5)
        theme_sizer.Add(theme_dropdown, flag=wx.ALL|wx.EXPAND, border=5)
        
        sizer.Add(theme_sizer, flag=wx.ALL|wx.EXPAND, border=5)
        
        self.white_box_sizer.Add(sizer, flag=wx.ALIGN_CENTER|wx.ALL, border=10)
        
        self.white_box.Layout()

app = wx.App(False)
frame = MainFrame(None, title="ActivityWatch")
app.MainLoop()
