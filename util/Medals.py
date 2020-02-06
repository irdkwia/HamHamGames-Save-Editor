OFF_MEDALS = 0x3b8
TEAM_SIZE = 0x4

OFF_RANK = 0x3b0
OFF_RANK_BACKUP = 0x3c8
RANK_SIZE = 0x4

NB_TEAMS = 4

YELLOW_T = 0
BLUE_T = 1
RED_T = 2
GREEN_T = 3

GOLD_M = 0
SILVER_M = 1
BRONZE_M = 2

def GetNbMedals(data, team, typeM):
    if team>=NB_TEAMS or typeM>=TEAM_SIZE:
        raise Exception("List index out of bounds.")
    return data[OFF_MEDALS+team*TEAM_SIZE+typeM]

def SetNbMedals(data, team, typeM, nb):
    if team>=NB_TEAMS or typeM>=TEAM_SIZE:
        raise Exception("List index out of bounds.")
    data = data[:OFF_MEDALS+team*TEAM_SIZE+typeM]+bytes([nb])+data[OFF_MEDALS+team*TEAM_SIZE+typeM+1:]
    return data

def GetRank(data, team):
    for i in range(RANK_SIZE):
        if data[OFF_RANK+RANK_SIZE+i]==team:
            return data[OFF_RANK+i]+1

def SetRanks(data, teamranks):
    ranklist = [0]*8
    nb_rank = 0
    for r in range(4):
        for i in range(4):
            if r==teamranks[i]-1:
                ranklist[nb_rank] = r
                ranklist[RANK_SIZE+nb_rank] = i
                nb_rank+=1
    data = data[:OFF_RANK]+bytes(ranklist)+data[OFF_RANK+2*RANK_SIZE:]
    data = data[:OFF_RANK_BACKUP]+bytes(ranklist)+data[OFF_RANK_BACKUP+2*RANK_SIZE:]
    return data
