import builtins
from util.Saves import *
from tkinter import filedialog, messagebox

#Save file
def SaveAs():
    global save
    if save.data!=None:
        FileName = filedialog.asksaveasfilename(title="Save file",filetypes=[('Save files','.sav'), ('All files','.*')])
        if FileName != "" and FileName != None and FileName != ():
            with open(FileName, 'wb') as file:
                file.write(CreateSave(save.data))
                file.close()
            save.filename = FileName
            labelMessage.config(fg='black', text='Saved data!')

#Save file
def Save():
    global save
    FileName = save.filename
    if save.data!=None and FileName != "" and FileName != None and FileName != ():
        with open(FileName, 'wb') as file:
            file.write(CreateSave(save.data))
            file.close()
        save.filename = FileName
        labelMessage.config(fg='black', text='Saved data!')
#Open file
def Open():
    global save
    FileName = filedialog.askopenfilename(title="Open file",filetypes=[('Save files','.sav'), ('All files','.*')])
    if FileName != "" and FileName != None and FileName != ():
        save_tmp = save.data
        with open(FileName, 'rb') as file:
            data = file.read()
            file.close()
        try:
            save.data = GetSave(data)
            save.filename = FileName
            labelMessage.config(fg='black', text='Save opened.')
        except:
            labelMessage.config(fg='red', text='Could not open the save.')
            save.data = save_tmp
