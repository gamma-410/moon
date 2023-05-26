import wx
import wx.html2

app = wx.App()

frame = wx.Frame(None, title="moon", size=(1300, 800))
browser = wx.html2.WebView.New(frame)
browser.LoadURL("https://gamma-410.github.io/moon/web/")


# メニュー機能
menubar = wx.MenuBar()
file = wx.Menu()
file.Append(1, 'Home')
file.Append(2, 'New Window')
file.Append(3, 'Exit')

help = wx.Menu()
help.Append(4, 'README.md')
help.Append(5, 'GitHub Repository')


menubar.Append(file, '&File')
menubar.Append(help, '&Help')
frame.SetMenuBar(menubar)


def selectMenu(event):
    if event.GetId() == 1:
        browser.LoadURL("https://gamma-410.github.io/moon/web/")

    elif event.GetId() == 2:    
        newFrame = wx.Frame(None, title="moon", size=(1300, 800))
        newBrowser = wx.html2.WebView.New(newFrame)
        newBrowser.LoadURL("https://gamma-410.github.io/moon/web/")
        newFrame.Show()

    elif event.GetId() == 3:
        exit()

    elif event.GetId() == 4:
        newFrame = wx.Frame(None, title="moon", size=(1300, 800))
        newBrowser = wx.html2.WebView.New(newFrame)
        newBrowser.LoadURL("https://gamma-410.github.io/moon/")
        newFrame.Show()

    elif event.GetId() == 5:
        newFrame = wx.Frame(None, title="moon", size=(1300, 800))
        newBrowser = wx.html2.WebView.New(newFrame)
        newBrowser.LoadURL("https://github.com/gamma-410/moon/")
        newFrame.Show()

frame.Bind(wx.EVT_MENU, selectMenu)



# 大事なやつら
frame.Show()
app.MainLoop()
