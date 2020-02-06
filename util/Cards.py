from .Text import *

CARD_COUNT = 0x3e0
PC_SIZE = 0x110
PC_OFF = 0x3e4
FC_SIZE = 0x118
FC_OFF = 0x4f4
FC_MAX = 50

def GetPC(data):
    card = data[PC_OFF:PC_OFF+PC_SIZE]
    return card

def SetPC(data, card):
    data = data[:PC_OFF]+card+data[PC_OFF+PC_SIZE:]
    return data

def GetTopList(data):
    return data[CARD_COUNT]
    
def AddFC(data, card):
    if GetTopList(data)>=FC_MAX:
        raise Exception("List index out of bounds")
    num = GetTopList(data)
    data = data[:CARD_COUNT]+bytes([num+1])+data[0x3e1:]
    return SetFC(data, card, num)

def DelFC(data, num, wipe=False):
    if GetTopList(data)<=0 or GetTopList(data)<=num:
        raise Exception("List index out of bounds")
    for i in range(num,  GetTopList(data)-1):
        data = SetFC(data, GetFC(data, i+1), i)
    
    data = data[:CARD_COUNT]+bytes([GetTopList(data)-1])+data[CARD_COUNT+1:]
    if wipe:
        data = data[:FC_OFF+GetTopList(data)*FC_SIZE]+bytes(FC_SIZE)+data[FC_OFF+(GetTopList(data)+1)*FC_SIZE:]
    return data

def WipeAllFC(data):
    data = data[:CARD_COUNT]+bytes([0])+data[0x3e1:]
    data = data[:FC_OFF]+bytes(FC_MAX*FC_SIZE)+data[FC_OFF+FC_MAX*FC_SIZE:]
    return data

def GetFC(data, num):
    if GetTopList(data)<=num:
        raise Exception("List index out of bounds")
    card = data[FC_OFF+FC_SIZE*num:FC_OFF+FC_SIZE*(num+1)]
    return card

def SetFC(data, card, num):
    if GetTopList(data)<=num:
        raise Exception("List index out of bounds")
    data = data[:FC_OFF+FC_SIZE*num]+card+data[FC_OFF+FC_SIZE*(num+1):]
    return data

def GetPropertyFC(card, p):
    if p == "name":
        length = card[0x5]
        return decodeNative(card[0x6:0x6+length*4])
    elif p == "birthdate":
        year = card[0x46]+1900
        month = card[0x47]
        day = card[0x48]
        return (year, month, day)
    elif p == "gender":
        return card[0x49]
    elif p == "description":
        length = card[0x4d]
        text = decodeNative(card[0x4e:0x4e+length*4])
        return (text[:0x18].rstrip(), text[0x18:])
    elif p == "costume":
        return card[0x10e]
    elif p == "color":
        return card[0x10f]
    elif p == "timecount":
        return card[0x110]
    elif p == "friendlv":
        return card[0x111]
    elif p == "eumode":
        return card[0x113]
    elif p == "cardtype":
        return card[0x114]
    elif p == "status":
        return card[0x115]
    return None

def SetPropertiesFC(card, **args):
    for p, v in args.items():
        if p == "name":
            if len(v)>0x10:
                raise Exception("Too long name")
            card = card[:0x4] + bytes([len(v) * 2, len(v)]) + encodeNative(v) + bytes(0x40-len(encodeNative(v))) + card[0x46:]
        elif p == "birthdate":
            if len(v)==2:
                card = card[:0x46]+bytes([0, v[0], v[1]]) + card[0x49:]
            else:
                card = card[:0x46]+bytes([v[0]-1900, v[1], v[2]]) + card[0x49:]
        elif p == "gender":
            card = card[:0x49] + bytes([v]) + card[0x4a:]
        elif p == "description":
            if len(v[0])>0x18 or len(v[1])>0x18:
                raise Exception("Too long description")
            v = v[0]+" "*(0x18-len(v[0]))+v[1]
            card = card[:0x4c] + bytes([len(v) * 2, len(v)]) + encodeNative(v) + bytes(0xc0-len(encodeNative(v))) + card[0x10e:]
        elif p == "costume":
            card = card[:0x10e] + bytes([v]) + card[0x10f:]
        elif p == "color":
            card = card[:0x10f] + bytes([v]) + card[0x110:]
        elif p == "timecount":
            card = card[:0x110] + bytes([v]) + card[0x111:]
        elif p == "friendlv":
            card = card[:0x111] + bytes([v]) + card[0x112:]
        elif p == "eumode":
            card = card[:0x113] + bytes([v]) + card[0x114:]
        elif p == "cardtype":
            card = card[:0x114] + bytes([v]) + card[0x115:]
        elif p == "status":
            card = card[:0x115] + bytes([v]) + card[0x116:]
    return card
