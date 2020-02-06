import builtins
from .Constants import *
from tkinter import *
from util.Medals import *

def CloseRanking():
    winRank.destroy()
    del builtins.winRank

#Create Window Ranking
def CreateWindowRanking():
    global save
    if save.data==None:
        labelMessage.config(fg='red', text='No save data.')
        return
    
    try:
        builtins.winRank
    except:
        builtins.winRank = Toplevel()
        winRank.protocol("WM_DELETE_WINDOW", CloseRanking)
        winRank.geometry("400x200")
        winRank.resizable(width=True, height=True)
        winRank.title("Ham-Ham Games Save Editor - Ranking")
        builtins.labelMessageRank = Label(winRank, text = "Ranking.", font=FONT)
        labelMessageRank.pack(side=TOP, fill=X)
        frameRank = Frame(winRank)
        frameRank.pack(side=TOP, fill=BOTH, expand = 1)
        builtins.lstMedalRank = []

        for i in range(6):
            frameRank.columnconfigure(i, weight=1)
        Label(frameRank, text = "Gold", font=FONT).grid(row=0, column=1)
        Label(frameRank, text = "Silver", font=FONT).grid(row=0, column=2)
        Label(frameRank, text = "Bronze", font=FONT).grid(row=0, column=3)
        Label(frameRank, text = "Rank", font=FONT).grid(row=0, column=5)
        
        for j, name in enumerate(teamnames):
            lstMedalRank.append([])
            Label(frameRank, text = name[1], font=FONT).grid(row=j+1, column=0, sticky='w')
            for i in range(3):
                entry = Entry(frameRank, font=FONT, width=3, justify='right')
                entry.grid(row=j+1, column=i+1)
                lstMedalRank[-1].append(entry)
            
            entry = Entry(frameRank, font=FONT, width=3, justify='right')
            entry.grid(row=j+1, column=5)
            lstMedalRank[-1].append(entry)
            
        builtins.varAutoRank = BooleanVar()
        varAutoRank.set(True)
        builtins.buttonSaveRank = Button(winRank, text="Save", command=SaveWindowRanking, font=FONT)
        buttonSaveRank.pack(side=BOTTOM, fill=X)
        builtins.chkAutoRank = Checkbutton(winRank, text="Auto Rank", command=SwitchAutoRank, font=FONT, bd=0, variable=varAutoRank)
        chkAutoRank.pack(side=BOTTOM, fill=X)
        for i, l in enumerate(lstMedalRank):
            for m in range(3):
                l[m].delete(0, END)
                l[m].insert(0, str(GetNbMedals(save.data, i, m)))
            l[-1].delete(0, END)
            l[-1].insert(0, str(GetRank(save.data, i)))
        SwitchAutoRank()

def SwitchAutoRank():
    for l in lstMedalRank:
        if varAutoRank.get():
            l[-1].config(state='disabled')
        else:
            l[-1].config(state='normal')

def SaveWindowRanking():
    global save
    save_tmp = save.data
    try:
        l_medals = []
        
        l_rank = []
        for i, l in enumerate(lstMedalRank):
            l_medals.append([])
            for m in range(3):
                v = int(l[m].get())
                l_medals[-1].append(v)
                save.data = SetNbMedals(save.data, i, m, v)
            l_rank.append(int(l[-1].get()))
        l_medals_sorted = sorted(l_medals)[::-1]
        if varAutoRank.get():
            l_rank = [l_medals_sorted.index(l_medals[i])+1 for i in range(len(l_rank))]
            for i, l in enumerate(lstMedalRank):
                l[-1].config(state='normal')
                l[-1].delete(0, END)
                l[-1].insert(0, str(l_rank[i]))
                l[-1].config(state='disabled')
        save.data = SetRanks(save.data, l_rank)
        labelMessageRank.config(text="Saved!", fg='black')
    except:
        labelMessageRank.config(text="Invalid Field(s)", fg='red')
        save.data = save_tmp
