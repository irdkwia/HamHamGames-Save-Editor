FONT = "arial 10"

with open("res//Teams.txt", encoding="utf-8") as file:
    content = file.read().split("\n")
    file.close()

teamnames = []
for i in range(len(content)):
    if i%8==0:
        teamnames.append([])
    elif i%8<7:
        teamnames[-1].append(content[i])

with open("res//Characters.txt", encoding="utf-8") as file:
    content = file.read().split("\n")
    file.close()

characters = []
for i in range(len(content)):
    if i%8==0:
        characters.append([])
    elif i%8<7:
        characters[-1].append(content[i])

with open("res//Costumes.txt", encoding="utf-8") as file:
    content = file.read().split("\n")
    file.close()

costumes = []
for i in range(len(content)):
    if i%8==0:
        costumes.append([])
    elif i%8<7:
        costumes[-1].append(content[i])


with open("res//Events.txt", encoding="utf-8") as file:
    content = file.read().split("\n")
    file.close()

events = []
for i in range(len(content)):
    if i%8==0:
        info = content[i].split("/")
        info[1] = int(info[1])
        events.append([info,[]])
    elif i%8<7:
        events[-1][1].append(content[i])

