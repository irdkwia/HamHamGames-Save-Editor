NB_COST = 80
COST_START = 6
COST_OFF = 0x44

def GetAllCostumes(data):
    for i in range(NB_COST):
        data = GetCostume(data, i)
    return data

def DelAllCostumes(data):
    for i in range(NB_COST):
        data = DelCostume(data, i)
    return data

def GetCostume(data, num):
    if num>=NB_COST:
        raise Exception("List index out of bounds.")
    num += COST_START
    data = data[:COST_OFF+num//8]+bytes([data[COST_OFF+num//8] | 2**(num%8)])+data[COST_OFF+num//8+1:]

    return data

def DelCostume(data, num):
    if num>=NB_COST:
        raise Exception("List index out of bounds.")
    num += COST_START
    data = data[:COST_OFF+num//8]+bytes([data[COST_OFF+num//8] & ~(2**(num%8))])+data[COST_OFF+num//8+1:]

    return data

def HasCostume(data, num):
    if num>=NB_COST:
        raise Exception("List index out of bounds.")
    num += COST_START

    return bool(data[COST_OFF+num//8] & 2**(num%8))
