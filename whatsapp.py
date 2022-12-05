import wx 
import wx.html2 

class MyBrowser(wx.Dialog): 
  def __init__(self, *args, **kwds): 
    wx.Dialog.__init__(self, *args, **kwds) 
    sizer = wx.BoxSizer(wx.VERTICAL) 
    self.browser = wx.html2.WebView.New(self) 
    sizer.Add(self.browser, 1, wx.EXPAND, 10) 
    self.Bind(wx.html2.EVT_WEBVIEW_LOADED, self.onWebViewLoaded, self.browser)
    self.browser.AddScriptMessageHandler('toPyt')
    self.Bind(wx.html2.EVT_WEBVIEW_SCRIPT_MESSAGE_RECEIVED, self.onMessage, self.browser)
    self.SetSizer(sizer) 
    self.SetSize((900, 700))

    button = wx.Button(self, wx.ID_ANY, 'Test', (10, 10))
    sizer.Add(button, 1, wx.SHAPED, 10)
    button.Bind(wx.EVT_BUTTON, self.onButton)

  def js(self, script):
    success, result = self.browser.RunScript(self.act + '\n' + script)
    if success:
      return result
    else:
      return None
  def jsAsync(self, script):
    self.browser.RunScriptAsync(self.act + '\n' + script)

  def onMessage(self, message):
    print(message.GetString())

  def onWebViewLoaded(self, evt):
    # Actions enabler.
    file = open('whatsappAct.js',mode='r')
    self.act = file.read()
    file.close()
    # Events subscribing.
    #file = open('whatsappEvt.js',mode='r')
    #self.js(file.read())
    #file.close()
    #
    #self.js('sendMessage("ottimo")')
    #self.js('getAllMessages()')
    #self.js('getAllChats()')
    #self.js('selectChat("Io")')
    print("baseSetup")
    self.jsAsync('baseSetup()')

  def onButton(self, evt):
    #self.js('sendMessage("ottimo")')
    #print(self.js('getAllMessages()'))
    #print(self.js('getAllChats()'))
    #self.js('selectChat("Io")')
    #print(self.js('getLastMessage()'))
    self.js('send("ciao", "bella")')

if __name__ == '__main__': 
  app = wx.App() 
  dialog = MyBrowser(None, -1)
  dialog.browser.LoadURL("https://web.whatsapp.com")
  dialog.Show()
  app.MainLoop()