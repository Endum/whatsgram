import wx 
import wx.html2 

class MyBrowser(wx.Dialog): 
  def __init__(self, *args, **kwds): 
    wx.Dialog.__init__(self, *args, **kwds) 
    sizer = wx.BoxSizer(wx.VERTICAL) # GUI
    self.browser = wx.html2.WebView.New(self) 
    sizer.Add(self.browser, 1, wx.EXPAND, 10) # GUI
    self.Bind(wx.html2.EVT_WEBVIEW_LOADED, self.onWebViewLoaded, self.browser)
    self.browser.AddScriptMessageHandler('toPyt')
    self.Bind(wx.html2.EVT_WEBVIEW_SCRIPT_MESSAGE_RECEIVED, self.onMessage, self.browser)
    self.SetSizer(sizer)  # GUI
    self.SetSize((900, 700)) # GUI

    button = wx.Button(self, wx.ID_ANY, 'Test', (10, 10)) # GUI
    sizer.Add(button, 1, wx.SHAPED, 10) # GUI
    button.Bind(wx.EVT_BUTTON, self.onButton) # GUI

  def js(self, script):
    success, result = self.browser.RunScript(self.act + '\n' + script)
    return result if success else None
  def jsAsync(self, script):
    self.browser.RunScriptAsync(self.act + '\n' + script)

  def onMessage(self, message):
    print(message.GetString())

  def onWebViewLoaded(self, evt):
    # Actions enabler.
    file = open('whatsappAct.js',mode='r')
    self.act = file.read()
    file.close()
    self.jsAsync('baseSetup()')

  def onButton(self, evt):  # GUI
    #self.js('sendMessage("ottimo")')
    #print(self.js('getAllMessages()'))
    #print(self.js('getAllChats()'))
    #self.js('selectChat("Io")')
    #print(self.js('getLastMessage()'))
    #self.js('send("ciao", "bella")')

if __name__ == '__main__': 
  app = wx.App() 
  dialog = MyBrowser(None, -1)
  dialog.browser.LoadURL("https://web.whatsapp.com")
  dialog.Show() # GUI
  app.MainLoop()