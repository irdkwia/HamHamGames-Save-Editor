import builtins
from .Constants import *
from tkinter import *
from util.Records import *

def CloseRecords():
    winRec.destroy()
    del builtins.winRec

#Create Window Records
def CreateWindowRecords():
    global save
    if save.data==None:
        labelMessage.config(fg='red', text='No save data.')
        return
    
    try:
        builtins.winRec
    except:
        builtins.winRec = Toplevel()
        winRec.protocol("WM_DELETE_WINDOW", CloseRecords)
        winRec.geometry("400x450")
        winRec.resizable(width=True, height=True)
        winRec.title("Ham-Ham Games Save Editor - Records")
        builtins.labelMessageRec = Label(winRec, text = "Records.", font=FONT)
        labelMessageRec.pack(side=TOP, fill=X)
        frameRec = Frame(winRec)
        frameRec.columnconfigure(0, weight=1)
        frameRec.pack(side=TOP, fill=BOTH, expand = 1)
        builtins.lstEvents = []
        for i, e in enumerate(events):
            lstEvents.append([])
            for j in range(e[0][1]):
                entry = Entry(frameRec, font=FONT, width=5, justify='right')
                entry.grid(row=i, column=j*2+1, sticky='we')
                lstEvents[-1].append(entry)
            Label(frameRec, text = e[1][1], font=FONT).grid(row=i, column=0, sticky='w')
            Label(frameRec, text = e[0][2], font=FONT).grid(row=i, column=2, sticky='w')
            Label(frameRec, text = e[0][3], font=FONT).grid(row=i, column=4, sticky='w')
        builtins.buttonSaveRec = Button(winRec, text="Save", command=SaveWindowRecords, font=FONT)
        buttonSaveRec.pack(side=BOTTOM, fill=X)
        frameRadioRec = Frame(winRec)
        frameRadioRec.pack(side=BOTTOM, fill=X)
        GetPBs()
        builtins.recordType = StringVar()
        recordType.set("PB")
        builtins.radioPB = Radiobutton(frameRadioRec, variable=recordType, text="Personal Best", value="PB", command=GetPBs, font=FONT, bd=0)
        radioPB.pack(side=LEFT, fill=BOTH, expand = 1)
        builtins.radioWR = Radiobutton(frameRadioRec, variable=recordType, text="World Record", value="WR", command=GetWRs, font=FONT, bd=0)
        radioWR.pack(side=LEFT, fill=BOTH, expand = 1)


            
def SaveWindowRecords():
    global save
    save_tmp = save.data
    try:
        for i, e in enumerate(events):
            v = []
            for j, ent in enumerate(lstEvents[i]):
                if ent.get()=="":
                    v.append(0)
                else:
                    v.append(int(ent.get()))
            save.data = eval("Set"+recordType.get()+"(save.data, "+e[0][0]+"="+str(v)+")")
        labelMessageRec.config(text="Saved!", fg='black')
    except:
        labelMessageRec.config(text="Invalid Field(s)", fg='red')
        save.data = save_tmp
            
def GetPBs():
    global save
    labelMessageRec.config(text="Personal Best.", fg='black')
    buttonSaveRec.config(text="Save PB")
    for i, e in enumerate(events):
        v = GetPB(save.data, e[0][0])
        for j, ent in enumerate(lstEvents[i]):
            ent.delete(0, END)
            if v==None:
                ent.config(state='disabled')
            else:
                ent.config(state='normal')
                ent.insert(0, str(v[j]))
def GetWRs():
    global save
    labelMessageRec.config(text="World Record.", fg='black')
    buttonSaveRec.config(text="Save WR")
    for i, e in enumerate(events):
        v = GetWR(save.data, e[0][0])
        for j, ent in enumerate(lstEvents[i]):
            ent.delete(0, END)
            if v==None:
                ent.config(state='disabled')
            else:
                ent.config(state='normal')
                ent.insert(0, str(v[j]))
