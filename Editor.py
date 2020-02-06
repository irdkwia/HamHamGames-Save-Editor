import builtins
from edit.Constants import *
from tkinter import *
from edit.Cards import *
from edit.Costumes import *
from edit.General import *
from edit.Hamigos import *
from edit.Main import *
from edit.Records import *
from edit.Ranking import *

class SaveData():
    def __init__(self):
        self.data = None
        self.filename = None

builtins.save = SaveData()

builtins.win = Tk()
win.geometry("300x200")
win.title("Ham-Ham Games Save Editor")
win.resizable(width=False, height=False)

builtins.labelMessage = Label(text = "No save.", font=FONT)
labelMessage.pack(side=TOP, fill=X)

frameGeneral = Frame()
frameGeneral.pack(side=TOP, fill=X)
builtins.buttonOpen = Button(frameGeneral, text="Open", command=Open, font=FONT)
buttonOpen.pack(side=LEFT, fill=BOTH, expand = 1)
builtins.buttonSave = Button(frameGeneral, text="Save", command=Save, font=FONT)
buttonSave.pack(side=LEFT, fill=BOTH, expand = 1)
builtins.buttonSave = Button(frameGeneral, text="Save As", command=SaveAs, font=FONT)
buttonSave.pack(side=RIGHT, fill=BOTH, expand = 1)
frameModules = Frame()
frameModules.pack(side=BOTTOM, fill=BOTH, expand=1)
for i in range(3):
    frameModules.columnconfigure(i, weight=1)
for i in range(2):
    frameModules.rowconfigure(i, weight=1)
            
builtins.buttonGeneral = Button(frameModules, text="General", command=CreateWindowGeneral, font=FONT)
buttonGeneral.grid(row=0, column=0, sticky='nswe')
builtins.buttonRecords = Button(frameModules, text="Records", command=CreateWindowRecords, font=FONT)
buttonRecords.grid(row=0, column=1, sticky='nswe')
builtins.buttonRanks = Button(frameModules, text="Ranking", command=CreateWindowRanking, font=FONT)
buttonRanks.grid(row=0, column=2, sticky='nswe')
builtins.buttonCostumes = Button(frameModules, text="Costumes", command=CreateWindowCostumes, font=FONT)
buttonCostumes.grid(row=1, column=0, sticky='nswe')
builtins.buttonCostumes = Button(frameModules, text="Hamigos", command=CreateWindowHamigos, font=FONT)
buttonCostumes.grid(row=1, column=1, sticky='nswe')
builtins.buttonCards = Button(frameModules, text="Cards", command=CreateWindowCards, font=FONT)
buttonCards.grid(row=1, column=2, sticky='nswe')

win.mainloop()
