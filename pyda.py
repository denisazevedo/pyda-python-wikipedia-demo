# https://github.com/KhanradCoder/PyDa-Course-Code

import wx
import wikipedia
import wolframalpha

# http://developer.wolframalpha.com/portal/myapps/
app_id = "YOUR APP ID"
client = wolframalpha.Client(app_id)

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am Pyda the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        try:
            # wolframalpha
            res = client.query(input)
            answer = next(res.results).text
            print("From Wolfram|Alpha:\n{}".format(answer))
        except:
            # wikipedia
            try:
                # Remove the 2 initial words like "Who is", "What is", "How are"
                # input = input.split(' ')
                # input = " ".join(input[2])
                wikipedia.set_lang("pt")
                answer = wikipedia.summary(input, sentences=2)
                print("From Wikipedia:\n{}".format(answer))
            except:
                print("I don't know")
        
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
