import builtins
from .Constants import *
from tkinter import *
from util.Costumes import *

def CloseCostumes():
    winCost.destroy()
    del builtins.winCost
    
#Create Window Costumes
def CreateWindowCostumes():
    global save
    if save.data==None:
        labelMessage.config(fg='red', text='No save data.')
        return
    try:
        builtins.winCost
    except:
        builtins.winCost = Toplevel()
        winCost.protocol("WM_DELETE_WINDOW", CloseCostumes)
        winCost.geometry("550x600")
        winCost.resizable(width=True, height=True)
        winCost.title("Ham-Ham Games Save Editor - Costumes")
        builtins.lstCostumes = []

        frameButtonCost = Frame(winCost)
        frameButtonCost.pack(side=BOTTOM, fill=X)
        builtins.buttonChkAllCost = Button(frameButtonCost, text="Select All", command=SelectAllCostumes, font=FONT)
        buttonChkAllCost.pack(side=LEFT, fill=BOTH, expand=1)
        builtins.buttonUnchkAllCost = Button(frameButtonCost, text="Deselect All", command=DeselectAllCostumes, font=FONT)
        buttonUnchkAllCost.pack(side=LEFT, fill=BOTH, expand=1)
        builtins.buttonSaveCost = Button(frameButtonCost, text="Save Costumes", command=SaveWindowCostumes, font=FONT)
        buttonSaveCost.pack(side=RIGHT, fill=BOTH, expand=1)
        
        frameCost = Frame(winCost)
        frameCost.pack(side=TOP, fill=BOTH, expand = 1)
        for i in range(4):
            frameCost.columnconfigure(i, weight=1)
        for i in range(NB_COST//4+1):
            frameCost.rowconfigure(i, weight=1)
        
        for i in range(NB_COST):
            b = BooleanVar()
            chk = Checkbutton(frameCost, text=("%02d - "%(i+1))+costumes[i][1], font=FONT, bd=0, variable=b)
            chk.grid(row=i//4, column=i%4, sticky="w")
            if HasCostume(save.data, i):
                chk.select()
            lstCostumes.append((chk, b))

def SelectAllCostumes():
    for i in range(NB_COST):
        lstCostumes[i][0].select()
        
def DeselectAllCostumes():
    for i in range(NB_COST):
        lstCostumes[i][0].deselect()
            
def SaveWindowCostumes():
    global save
    for i in range(NB_COST):
        if lstCostumes[i][1].get():
            save.data = GetCostume(save.data, i)
        else:
            save.data = DelCostume(save.data, i)
