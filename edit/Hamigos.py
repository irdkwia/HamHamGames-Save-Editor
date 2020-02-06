import builtins
from .Constants import *
from tkinter import *
from util.Hamigos import *

def CloseHamigos():
    winHam.destroy()
    del builtins.winHam

#Create Window Hamigos
def CreateWindowHamigos():
    global save
    if save.data==None:
        labelMessage.config(fg='red', text='No save data.')
        return
    
    try:
        builtins.winHam
    except:
        builtins.winHam = Toplevel()
        winHam.protocol("WM_DELETE_WINDOW", CloseHamigos)
        winHam.geometry("700x500")
        winHam.resizable(width=True, height=True)
        winHam.title("Ham-Ham Games Save Editor - Hamigos")
        builtins.lstHamigos = []
        frameButtonHam = Frame(winHam)
        frameButtonHam.pack(side=BOTTOM, fill=X)
        builtins.buttonChkAllHam = Button(frameButtonHam, text="Select All", command=SelectAllHamigos, font=FONT)
        buttonChkAllHam.pack(side=LEFT, fill=BOTH, expand=1)
        builtins.buttonUnchkAllHam = Button(frameButtonHam, text="Deselect All", command=DeselectAllHamigos, font=FONT)
        buttonUnchkAllHam.pack(side=LEFT, fill=BOTH, expand=1)
        builtins.buttonSaveHam = Button(frameButtonHam, text="Save Hamigos", command=SaveWindowHamigos, font=FONT)
        buttonSaveHam.pack(side=RIGHT, fill=BOTH, expand=1)
        
        frameHam = Frame(winHam)
        frameHam.pack(side=TOP, fill=BOTH, expand = 1)
        for i in range(4):
            frameHam.columnconfigure(i, weight=1)
        for i in range(NB_HAMIGO//4+1):
            frameHam.rowconfigure(i, weight=1)
        for i in range(NB_HAMIGO):
            b = BooleanVar()
            chk = Checkbutton(frameHam, text=("%02d - "%(i))+characters[i][1], font=FONT, bd=0, variable=b)
            chk.grid(row=i//4, column=i%4, sticky="w")
            if HasHamigo(save.data, i):
                chk.select()
            lstHamigos.append((chk, b))

def SelectAllHamigos():
    for i in range(NB_HAMIGO):
        lstHamigos[i][0].select()
        
def DeselectAllHamigos():
    for i in range(NB_HAMIGO):
        lstHamigos[i][0].deselect()
            
def SaveWindowHamigos():
    global save
    for i in range(NB_HAMIGO):
        if lstHamigos[i][1].get():
            save.data = GetHamigo(save.data, i)
        else:
            save.data = DelHamigo(save.data, i)
