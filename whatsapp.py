import wx
import wx.html2

class WhatsappBOT(wx.Dialog):
  def __init__(self):
    wx.Dialog.__init__(self, None, -1)
    sizer = wx.BoxSizer(wx.VERTICAL) # GUI
    self.__browser = wx.html2.WebView.New(self)
    sizer.Add(self.__browser, 1, wx.EXPAND, 10) # GUI
    self.Bind(wx.html2.EVT_WEBVIEW_LOADED, self.__onWebViewLoaded, self.__browser)
    self.__browser.AddScriptMessageHandler('toPyt')
    #self.Bind(wx.html2.EVT_WEBVIEW_SCRIPT_MESSAGE_RECEIVED, self.__onMessage, self.__browser)
    self.SetSizer(sizer)  # GUI
    self.SetSize((900, 700)) # GUI

    button = wx.Button(self, wx.ID_ANY, 'Test', (10, 10)) # GUI
    sizer.Add(button, 1, wx.SHAPED, 10) # GUI
    button.Bind(wx.EVT_BUTTON, self.__onButton) # GUI

  def __js(self, script):
    success, result = self.__browser.RunScript(self.__act + '\n' + script)
    return result if success else None
  def __jsAsync(self, script):
    self.__browser.RunScriptAsync(self.__act + '\n' + script)

  def __onMessage(self, message):
    print(message.GetString())

  def __onWebViewLoaded(self, evt):
    # Actions enabler.
    file = open('whatsappAct.js',mode='r')
    self.__act = file.read()
    file.close()
    self.__jsAsync('baseSetup()')

  def __onButton(self, evt):  # GUI
    #self.js('sendMessage("ottimo")')
    #print(self.js('getAllMessages()'))
    #print(self.js('getAllChats()'))
    #self.js('selectChat("Io")')
    #print(self.js('getLastMessage()'))
    self.__js('send("ciao", "bella")')

  def bindTopic(self, callback):
    self.Bind(wx.html2.EVT_WEBVIEW_SCRIPT_MESSAGE_RECEIVED, callback, self.__browser)

  def loadWhatsapp(self):
    self.__browser.LoadURL("https://web.whatsapp.com")

if __name__ == '__main__':
  app = wx.App()
  whats = WhatsappBOT()
  whats.loadWhatsapp()
  whats.Show() # GUI
  app.MainLoop()