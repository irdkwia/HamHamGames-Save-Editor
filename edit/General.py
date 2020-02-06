import builtins
from .Constants import *
from util.Vars import *
from tkinter import *

def CloseGeneral():
    winGen.destroy()
    del builtins.winGen

#Create Window General
def CreateWindowGeneral():
    global save
    if save.data==None:
        labelMessage.config(fg='red', text='No save data.')
        return
    try:
        builtins.winGen
    except:
        builtins.winGen = Toplevel()
        winGen.protocol("WM_DELETE_WINDOW", CloseGeneral)
        winGen.geometry("300x350")
        winGen.resizable(width=True, height=True)
        winGen.title("Ham-Ham Games Save Editor - General")
        builtins.labelMessageGen = Label(winGen, text = "General.", font=FONT)
        labelMessageGen.pack(side=TOP, fill=X)
        frameGen = Frame(winGen)
        frameGen.pack(side=TOP, fill=X)
        frameGen.columnconfigure(0, weight=1)
        frameGen.columnconfigure(1, weight=3)
        Label(frameGen, text = "Seeds: ", font=FONT).grid(row=0, column=0, sticky='w')
        builtins.entryMoney = Entry(frameGen, font=FONT)
        entryMoney.grid(row=0, column=1, sticky='we')
        Label(frameGen, text = "Location: ", font=FONT).grid(row=1, column=0, sticky='w')
        builtins.entryLoc = Entry(frameGen, font=FONT)
        entryLoc.grid(row=1, column=1, sticky='we')
        Label(frameGen, text = "Language: ", font=FONT).grid(row=2, column=0, sticky='w')
        builtins.entryLang = Entry(frameGen, font=FONT)
        entryLang.grid(row=2, column=1, sticky='we')
        entryMoney.delete(0, END)
        entryMoney.insert(0, str(GetMoney(save.data)))
        entryLoc.delete(0, END)
        entryLoc.insert(0, str(GetLocation(save.data)))
        entryLang.delete(0, END)
        entryLang.insert(0, str(GetLang(save.data)))

        #For testing events
        """
        builtins.varDummy = BooleanVar()
        builtins.chkDummy = Checkbutton(frameGen, text="Dummy", font=FONT, bd=0, variable=varDummy)
        chkDummy.grid(row=4, column=0, sticky="w")
        if HasEvent(save.data, EVT_DUMMY):
            chkDummy.select()
        """
        builtins.varBasketball = BooleanVar()
        builtins.chkBasketball = Checkbutton(frameGen, text="9999 Basketball", font=FONT, bd=0, variable=varBasketball)
        chkBasketball.grid(row=3, column=0, sticky="w")
        if HasEvent(save.data, EVT_9999_BASKETBALL):
            chkBasketball.select()
        builtins.varBalloons = BooleanVar()
        builtins.chkBalloons = Checkbutton(frameGen, text="9999 Balloons", font=FONT, bd=0, variable=varBalloons)
        chkBalloons.grid(row=3, column=1, sticky="w")
        if HasEvent(save.data, EVT_9999_BALLOONS):
            chkBalloons.select()
        
        builtins.buttonSaveGeneral = Button(winGen, text="Save General", command=SaveWindowGeneral, font=FONT)
        buttonSaveGeneral.pack(side=BOTTOM, fill=X)
        
        Label(winGen, text = "Messages", font=FONT).pack(side=TOP, fill=X)

        frameMsg = Frame(winGen)
        frameMsg.pack(side=TOP, fill=X)
        frameMsg.columnconfigure(0, weight=1)
        frameMsg.columnconfigure(1, weight=3)
        Label(frameMsg, text = "Greeting: ", font=FONT).grid(row=0, column=0, sticky='w')
        builtins.entryMsg1 = Entry(frameMsg, font=FONT)
        entryMsg1.grid(row=0, column=1, sticky='we')
        entryMsg1.delete(0, END)
        entryMsg1.insert(0, convertencodable(GetInfo(save.data, 0)))


        Label(frameMsg, text = "Goodbye: ", font=FONT).grid(row=1, column=0, sticky='w')
        builtins.entryMsg2 = Entry(frameMsg, font=FONT)
        entryMsg2.grid(row=1, column=1, sticky='we')
        entryMsg2.delete(0, END)
        entryMsg2.insert(0, convertencodable(GetInfo(save.data, 1)))


        Label(frameMsg, text = "Thanking: ", font=FONT).grid(row=2, column=0, sticky='w')
        builtins.entryMsg3 = Entry(frameMsg, font=FONT)
        entryMsg3.grid(row=2, column=1, sticky='we')
        entryMsg3.delete(0, END)
        entryMsg3.insert(0, convertencodable(GetInfo(save.data, 2)))

        
        Label(frameMsg, text = "Favorite phrase: ", font=FONT).grid(row=3, column=0, sticky='w')
        builtins.entryMsg4 = Entry(frameMsg, font=FONT)
        entryMsg4.grid(row=3, column=1, sticky='we')
        entryMsg4.delete(0, END)
        entryMsg4.insert(0, convertencodable(GetInfo(save.data, 3)))


        Label(frameMsg, text = "Job: ", font=FONT).grid(row=4, column=0, sticky='w')
        builtins.entryMsg5 = Entry(frameMsg, font=FONT)
        entryMsg5.grid(row=4, column=1, sticky='we')
        entryMsg5.delete(0, END)
        entryMsg5.insert(0, convertencodable(GetInfo(save.data, 4)))

        
        Label(frameMsg, text = "Subject: ", font=FONT).grid(row=5, column=0, sticky='w')
        builtins.entryMsg6 = Entry(frameMsg, font=FONT)
        entryMsg6.grid(row=5, column=1, sticky='we')
        entryMsg6.delete(0, END)
        entryMsg6.insert(0, convertencodable(GetInfo(save.data, 5)))

        
        Label(frameMsg, text = "Food: ", font=FONT).grid(row=6, column=0, sticky='w')
        builtins.entryMsg7 = Entry(frameMsg, font=FONT)
        entryMsg7.grid(row=6, column=1, sticky='we')
        entryMsg7.delete(0, END)
        entryMsg7.insert(0, convertencodable(GetInfo(save.data, 6)))

        
        Label(frameMsg, text = "Favorite place: ", font=FONT).grid(row=7, column=0, sticky='w')
        builtins.entryMsg8 = Entry(frameMsg, font=FONT)
        entryMsg8.grid(row=7, column=1, sticky='we')
        entryMsg8.delete(0, END)
        entryMsg8.insert(0, convertencodable(GetInfo(save.data, 7)))

#Save general
def SaveWindowGeneral():
    global save
    labelMessageGen.config(fg='black', text='Saved general!')
    try:
        save.data = SetMoney(save.data, int(entryMoney.get()))
    except:
        labelMessageGen.config(fg='red', text='Invalid seed count.')
    try:
        save.data = SetLang(save.data, int(entryLang.get()))
    except:
        labelMessageGen.config(fg='red', text='Invalid language.')
    try:
        save.data = SetLocation(save.data, int(entryLoc.get()))
    except:
        labelMessageGen.config(fg='red', text='Invalid location.')
    
    #For testing events
    """
    if varDummy.get():
        save.data = GetEvent(save.data, EVT_DUMMY)
    else:
        save.data = DelEvent(save.data, EVT_DUMMY)
    """ 
    if varBasketball.get():
        save.data = GetEvent(save.data, EVT_9999_BASKETBALL)
    else:
        save.data = DelEvent(save.data, EVT_9999_BASKETBALL)
    if varBalloons.get():
        save.data = GetEvent(save.data, EVT_9999_BALLOONS)
    else:
        save.data = DelEvent(save.data, EVT_9999_BALLOONS)
    
    try:
        save.data = SetInfo(save.data, 0, convertunencodable(entryMsg1.get()))
    except:
        labelMessageGen.config(fg='red', text='Too long greeting.')
    try:
        save.data = SetInfo(save.data, 1, convertunencodable(entryMsg2.get()))
    except:
        labelMessageGen.config(fg='red', text='Too long bye.')
    try:
        save.data = SetInfo(save.data, 2, convertunencodable(entryMsg3.get()))
    except:
        labelMessageGen.config(fg='red', text='Too long thanking.')
    try:
        save.data = SetInfo(save.data, 3, convertunencodable(entryMsg4.get()))
    except:
        labelMessageGen.config(fg='red', text='Too long catchphrase.')
    try:
        save.data = SetInfo(save.data, 4, convertunencodable(entryMsg5.get()))
    except:
        labelMessageGen.config(fg='red', text='Too long job.')
    try:
        save.data = SetInfo(save.data, 5, convertunencodable(entryMsg6.get()))
    except:
        labelMessageGen.config(fg='red', text='Too long course.')
    try:
        save.data = SetInfo(save.data, 6, convertunencodable(entryMsg7.get()))
    except:
        labelMessageGen.config(fg='red', text='Too long food.')
    try:
        save.data = SetInfo(save.data, 7, convertunencodable(entryMsg8.get()))
    except:
        labelMessageGen.config(fg='red', text='Too long favorite loc.')
