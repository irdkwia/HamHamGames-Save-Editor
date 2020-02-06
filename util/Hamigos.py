NB_HAMIGO = 51
HAMIGO_START = 2
HAMIGO_OFF = 0x56
HAMIGO2_START = 6
HAMIGO2_OFF = 0x5c

def GetAllHamigos(data):
    for i in range(NB_HAMIGO):
        data = GetHamigo(data, i)
    return data

def DelAllHamigos(data):
    for i in range(NB_HAMIGO):
        data = DelHamigo(data, i)
    return data

def GetHamigo(data, num):
    if num>=NB_HAMIGO:
        raise Exception("List index out of bounds.")
    num += HAMIGO_START
    data = data[:HAMIGO_OFF+num//8]+bytes([data[HAMIGO_OFF+num//8] | 2**(num%8)])+data[HAMIGO_OFF+num//8+1:]
    num += HAMIGO2_START-HAMIGO_START
    data = data[:HAMIGO2_OFF+num//8]+bytes([data[HAMIGO2_OFF+num//8] | 2**(num%8)])+data[HAMIGO2_OFF+num//8+1:]

    return data

def DelHamigo(data, num):
    if num>=NB_HAMIGO:
        raise Exception("List index out of bounds.")
    num += HAMIGO_START
    data = data[:HAMIGO_OFF+num//8]+bytes([data[HAMIGO_OFF+num//8] & ~(2**(num%8))])+data[HAMIGO_OFF+num//8+1:]
    num += HAMIGO2_START-HAMIGO_START
    data = data[:HAMIGO2_OFF+num//8]+bytes([data[HAMIGO2_OFF+num//8] & ~(2**(num%8))])+data[HAMIGO2_OFF+num//8+1:]

    return data

def HasHamigo(data, num):
    if num>=NB_HAMIGO:
        raise Exception("List index out of bounds.")
    num += HAMIGO2_START

    return bool(data[HAMIGO2_OFF+num//8] & 2**(num%8))
