import builtins
from .Constants import *
from tkinter import *
from tkinter import filedialog, messagebox
from util.Cards import *

def CloseCards():
    winCard.destroy()
    del builtins.winCard

#Create Window Cards
def CreateWindowCards():
    global save
    if save.data==None:
        labelMessage.config(fg='red', text='No save data.')
        return
    
    try:
        builtins.winCard
    except:
        builtins.winCard = Toplevel()
        winCard.protocol("WM_DELETE_WINDOW", CloseCards)
        winCard.geometry("500x600")
        winCard.resizable(width=True, height=True)
        winCard.title("Ham-Ham Games Save Editor - Cards")
        builtins.labelMessageCard = Label(winCard, text = "Cards.", font=FONT)
        labelMessageCard.pack(side=TOP, fill=X)
        
        frameLst = Frame(winCard)
        frameLst.pack(side=LEFT, fill=Y)
        
        builtins.cardType = StringVar()
        cardType.set("Player")
        builtins.radioPlayer = Radiobutton(frameLst, variable=cardType, text="Player Card", command=SwitchPlayerCard, value="Player", font=FONT, bd=0, anchor='w', width=30)
        radioPlayer.pack(side=TOP, fill=X)
        builtins.radioFriends = Radiobutton(frameLst, variable=cardType, text="Friend Cards", command=SwitchFriendCard, value="Friends", font=FONT, bd=0, anchor='w', width=30)
        radioFriends.pack(side=TOP, fill=X)
        
        builtins.labelCountCard = Label(frameLst, text = "0 card(s).", font=FONT)
        labelCountCard.pack(side=TOP, fill=X)

        
        frameButtonsLst = Frame(frameLst)
        frameButtonsLst.pack(side=BOTTOM, fill=X)
        builtins.buttonAddCard = Button(frameButtonsLst, text="Add", command=AddEmptyCard, font=FONT)
        buttonAddCard.pack(side=LEFT, fill=X, expand=1)
        builtins.buttonImpCard = Button(frameButtonsLst, text="Import", command=ImportCard, font=FONT)
        buttonImpCard.pack(side=LEFT, fill=X, expand=1)
        builtins.buttonDelCard = Button(frameButtonsLst, text="Delete", command=DeleteCard, font=FONT)
        buttonDelCard.pack(side=LEFT, fill=X, expand=1)
        
        
        builtins.lstCards = Listbox(frameLst, selectmode=SINGLE)
        scrollbar = Scrollbar(lstCards, orient="vertical")
        scrollbar.pack(side=RIGHT, fill=BOTH)
        lstCards.pack(side=TOP, fill=BOTH, expand=1)
        scrollbar.config(command=lstCards.yview)
        lstCards.config(yscrollcommand=scrollbar.set)
        lstCards.bind('<<ListboxSelect>>', RefreshCardValues)

        frameCard = Frame(winCard)
        frameCard.pack(side=RIGHT, fill=BOTH, expand=1)
        
        Label(frameCard, text="Name: ", anchor='w', font=FONT).pack(side=TOP, fill=X)
        builtins.entryName = Entry(frameCard, font=FONT)
        entryName.pack(side=TOP, fill=X)
        
        Label(frameCard, text="Date of birth (YYYY/MM/DD): ", anchor='w', font=FONT).pack(side=TOP, fill=X)
        frameBirth = Frame(frameCard)
        frameBirth.pack(side=TOP, fill=X)
        builtins.entryBirthY = Entry(frameBirth, font=FONT, width=6, justify='right')
        entryBirthY.pack(side=LEFT, fill=X)
        Label(frameBirth, text="/", anchor='w').pack(side=LEFT, fill=X)
        builtins.entryBirthM = Entry(frameBirth, font=FONT, width=3, justify='right')
        entryBirthM.pack(side=LEFT, fill=X)
        Label(frameBirth, text="/", anchor='w').pack(side=LEFT, fill=X)
        builtins.entryBirthD = Entry(frameBirth, font=FONT, width=3, justify='right')
        entryBirthD.pack(side=LEFT, fill=X)
        
        Label(frameCard, text="Gender: ", anchor='w', font=FONT).pack(side=TOP, fill=X)
        builtins.gender = StringVar()
        gender.set("M")
        builtins.radioMale = Radiobutton(frameCard, variable=gender, text="Male", value="M", font=FONT, bd=0, anchor='w')
        radioMale.pack(side=TOP, fill=X)
        builtins.radioFemale = Radiobutton(frameCard, variable=gender, text="Female", value="F", font=FONT, bd=0, anchor='w')
        radioFemale.pack(side=TOP, fill=X)
        builtins.radioSecret = Radiobutton(frameCard, variable=gender, text="Secret", value="S", font=FONT, bd=0, anchor='w')
        radioSecret.pack(side=TOP, fill=X)
        
        Label(frameCard, text="Message: ", anchor='w', font=FONT).pack(side=TOP, fill=X)
        builtins.entryDesc1 = Entry(frameCard, font=FONT)
        entryDesc1.pack(side=TOP, fill=X)
        builtins.entryDesc2 = Entry(frameCard, font=FONT)
        entryDesc2.pack(side=TOP, fill=X)

        frameCC = Frame(frameCard)
        frameCC.pack(side=TOP, fill=X)
        frameCC.columnconfigure(0, weight=1)
        frameCC.columnconfigure(1, weight=1)
        Label(frameCC, text="Color: ", font=FONT).grid(row=0, column=0, sticky='w')
        builtins.entryColor = Entry(frameCC, font=FONT, width=4)
        entryColor.grid(row=1, column=0, sticky='w')
        Label(frameCC, text="Costume: ", font=FONT).grid(row=0, column=1, sticky='w')
        builtins.entryCost = Entry(frameCC, font=FONT, width=4)
        entryCost.grid(row=1, column=1, sticky='w')
        Label(frameCC, text="Count: ", font=FONT).grid(row=2, column=0, sticky='w')
        builtins.entryCnt = Entry(frameCC, font=FONT, width=4)
        entryCnt.grid(row=3, column=0, sticky='w')
        Label(frameCC, text="Friend LV: ", font=FONT).grid(row=2, column=1, sticky='w')
        builtins.entryLV = Entry(frameCC, font=FONT, width=4)
        entryLV.grid(row=3, column=1, sticky='w')

        builtins.varEvt = BooleanVar()
        builtins.chkEvt = Checkbutton(frameCC, text="EU Mode", font=FONT, bd=0, variable=varEvt)
        chkEvt.grid(row=4, column=0, sticky="w")

        builtins.varSeen = BooleanVar()
        builtins.chkSeen = Checkbutton(frameCC, text="Seen", font=FONT, bd=0, variable=varSeen)
        chkSeen.grid(row=4, column=1, sticky="w")

        Label(frameCC, text="Card Type: ", font=FONT).grid(row=5, column=0, sticky='w')
        builtins.entryCT = Entry(frameCC, font=FONT, width=4)
        entryCT.grid(row=6, column=0, sticky='w')

        
        frameButtonsCard = Frame(frameCard)
        frameButtonsCard.pack(side=BOTTOM, fill=X)
        
        builtins.buttonExpCard = Button(frameButtonsCard, text="Export", command=ExportCard, font=FONT)
        buttonExpCard.pack(side=LEFT, fill=X, expand=1)
        builtins.buttonSaveCard = Button(frameButtonsCard, text="Save Changes", command=SaveCard, font=FONT)
        buttonSaveCard.pack(side=LEFT, fill=X, expand=1)
        SwitchPlayerCard()

def DeleteCard():
    global save
    current = lstCards.index(ACTIVE)
    save.data = DelFC(save.data, current, wipe=True)
    SwitchFriendCard()
    lstCards.select_clear(0, END)
    lstCards.select_set(min(current, GetTopList(save.data)-1))
    lstCards.activate(min(current, GetTopList(save.data)-1))
    lstCards.see(min(current, GetTopList(save.data)-1))
    RefreshCardValues()
    labelMessageCard.config(text="Deleted card!", fg='black')
    
def ImportCard():
    global save
    if GetTopList(save.data)==FC_MAX:
        labelMessageCard.config(text="Can't add a card!", fg='red')
    else:
        FileName = filedialog.askopenfilename(title="Import card",filetypes=[('Card files','.crd'), ('All files','.*')])
        if FileName != "" and FileName != None and FileName != ():
            with open(FileName, 'rb') as file:
                card = file.read()
                file.close()
            if len(card)==FC_SIZE:
                save.data = AddFC(save.data, card)
                labelMessageCard.config(text="Added card!", fg='black')
                RefreshListCard()
                lstCards.select_clear(0, END)
                lstCards.select_set(GetTopList(save.data)-1)
                lstCards.activate(GetTopList(save.data)-1)
                lstCards.see(GetTopList(save.data)-1)
                RefreshCardValues()
            else:
                labelMessageCard.config(text="Invalid card!", fg='red')

def ExportCard():
    global save
    if SaveCard():
        FileName = filedialog.asksaveasfilename(title="Export card",filetypes=[('Card files','.crd'), ('All files','.*')])
        if FileName != "" and FileName != None and FileName != ():
            if cardType.get()=="Player":
                card = GetPC(save.data)
                card += bytes(FC_SIZE-PC_SIZE)
                card = SetPropertiesFC(card, status=1, cardtype=0, eumode=0, timecount=0, friendlv=100)
            else:
                card = GetFC(save.data, lstCards.index(ACTIVE))
            with open(FileName, 'wb') as file:
                file.write(card)
                file.close()
            labelMessageCard.config(text="Exported card!", fg='black')
        
def AddEmptyCard():
    global save
    if GetTopList(save.data)==FC_MAX:
        labelMessageCard.config(text="Can't add a card!", fg='red')
    else:
        with open("res//empty.crd", 'rb') as file:
            card = file.read()
            file.close()
        if len(card)==FC_SIZE:
            save.data = AddFC(save.data, card)
            labelMessageCard.config(text="Added card!", fg='black')
            RefreshListCard()
            lstCards.select_clear(0, END)
            lstCards.select_set(GetTopList(save.data)-1)
            lstCards.activate(GetTopList(save.data)-1)
            lstCards.see(GetTopList(save.data)-1)
            RefreshCardValues()
        else:
            labelMessageCard.config(text="Invalid card!", fg='red')

def SaveCard():
    global save
    if cardType.get()=="Player":
        card = GetPC(save.data)
    else:
        card = GetFC(save.data, lstCards.index(ACTIVE))
    
    try:
        card = SetPropertiesFC(card, name=convertunencodable(entryName.get()),
                    description=(convertunencodable(entryDesc1.get()), convertunencodable(entryDesc2.get())))
        card = SetPropertiesFC(card, birthdate=(int(entryBirthY.get()), int(entryBirthM.get()), int(entryBirthD.get())))
        if gender.get()=="M":
            card = SetPropertiesFC(card, gender=0)
        elif gender.get()=="F":
            card = SetPropertiesFC(card, gender=1)
        else:
            card = SetPropertiesFC(card, gender=2)
        
        card = SetPropertiesFC(card, costume=int(entryCost.get()), color=int(entryColor.get()))
        
        if cardType.get()!="Player":
            card = SetPropertiesFC(card, timecount=int(entryCnt.get()), friendlv=int(entryLV.get()))

            if varEvt.get():
                card = SetPropertiesFC(card, eumode=1)
            else:
                card = SetPropertiesFC(card, eumode=0)

            if varSeen.get():
                card = SetPropertiesFC(card, status=0)
            else:
                card = SetPropertiesFC(card, status=1)
            
            card = SetPropertiesFC(card, cardtype=int(entryCT.get()))
        labelMessageCard.config(text="Saved!", fg='black')
        if cardType.get()=="Player":
            save.data = SetPC(save.data, card)
        else:
            current = 0
            try:
                current = lstCards.curselection()[0]
                save.data = SetFC(save.data, card, lstCards.curselection()[0])
            except:
                current = lstCards.index(ACTIVE)
                save.data = SetFC(save.data, card, lstCards.index(ACTIVE))
            RefreshListCard()
            lstCards.select_clear(0, END)
            lstCards.select_set(current)
            lstCards.activate(current)
        return True
    except:
        labelMessageCard.config(text="Invalid field(s).", fg='red')
        return False

def RefreshListCard():
    global save
    labelCountCard.config(text=str(GetTopList(save.data))+" card(s)")
    lstCards.delete(0, END)
    for i in range(GetTopList(save.data)):
        card = GetFC(save.data, i)
        lstCards.insert(END, convertencodable(GetPropertyFC(card, "name")))

def RefreshCardValues(i=None):
    global save
    if cardType.get()=="Player":
        labelMessageCard.config(text="Player card.", fg='black')
        card = GetPC(save.data)
    else:
        labelMessageCard.config(text="Friend cards.", fg='black')
        try:
            card = GetFC(save.data, lstCards.curselection()[0])
            lstCards.activate(lstCards.curselection()[0])
        except:
            return
    entryName.delete(0, END)
    entryName.insert(0, convertencodable(GetPropertyFC(card, "name")))
    desc = GetPropertyFC(card, "description")
    entryDesc1.delete(0, END)
    entryDesc1.insert(0, convertencodable(desc[0]))
    entryDesc2.delete(0, END)
    entryDesc2.insert(0, convertencodable(desc[1]))

    birth = GetPropertyFC(card, "birthdate")
    entryBirthY.delete(0, END)
    entryBirthY.insert(0, str(birth[0]))
    entryBirthM.delete(0, END)
    entryBirthM.insert(0, str(birth[1]))
    entryBirthD.delete(0, END)
    entryBirthD.insert(0, str(birth[2]))

    gen = GetPropertyFC(card, "gender")
    if gen==0:
        gender.set("M")
    elif gen==1:
        gender.set("F")
    else:
        gender.set("S")
    entryCost.delete(0, END)
    entryCost.insert(0, str(GetPropertyFC(card, "costume")))
    
    entryColor.delete(0, END)
    entryColor.insert(0, str(GetPropertyFC(card, "color")))

    entryCnt.delete(0, END)
    entryLV.delete(0, END)
    entryCT.delete(0, END)
    if cardType.get()=="Player":
        entryCnt.config(state='disabled')
        entryLV.config(state='disabled')
        chkEvt.config(state='disabled')
        chkSeen.config(state='disabled')
        entryCT.config(state='disabled')
    else:
        entryCnt.config(state='normal')
        entryCnt.insert(0, str(GetPropertyFC(card, "timecount")))
        
        entryLV.config(state='normal')
        entryLV.insert(0, str(GetPropertyFC(card, "friendlv")))
        
        chkEvt.config(state='normal')
        varEvt.set(GetPropertyFC(card, "eumode")>0)
        
        chkSeen.config(state='normal')
        varSeen.set(GetPropertyFC(card, "status")==0)

        entryCT.config(state='normal')
        entryCT.insert(0, str(GetPropertyFC(card, "cardtype")))

def SwitchPlayerCard():
    global save
    RefreshListCard()
    lstCards.select_set(0)
    RefreshCardValues()
    lstCards.config(state='disabled')
    buttonAddCard.config(state='disabled')
    buttonImpCard.config(state='disabled')
    buttonDelCard.config(state='disabled')
    
def SwitchFriendCard():
    global save
    if GetTopList(save.data)==0:
        cardType.set('Player')
        SwitchPlayerCard()
    else:
        lstCards.config(state='normal')
        buttonAddCard.config(state='normal')
        buttonImpCard.config(state='normal')
        buttonDelCard.config(state='normal')
        RefreshListCard()
        lstCards.select_set(0)
        RefreshCardValues()
