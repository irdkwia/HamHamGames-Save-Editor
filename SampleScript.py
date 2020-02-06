#Import everything
from util.Cards import *
from util.Costumes import *
from util.Hamigos import *
from util.Medals import *
from util.Records import *
from util.Saves import *
from util.Vars import *

#Path to your save
src = ""

#Path to your new save (replace by dst = src if you want to overwrite your save)
dst = ""


#Load file
with open(src, "rb") as file:
    data = file.read()
    file.close()

#Extract save
save = GetSave(data)


#Do anything you want on the save here




#######


#Build the new save data
data = CreateSave(save)

#Save data into the new file
with open(dst, "wb") as file:
    file.write(data)
    file.close()
