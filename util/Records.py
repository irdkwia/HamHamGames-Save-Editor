
def SetPB(data, **events):
    for e, v in events.items():
        if e=="dash100hm":
            data = data[:0x310]+bytes([v[2], v[1], v[0]])+data[0x313:]
        elif e=="hurdles":
            data = data[:0x318]+bytes([v[2], v[1], v[0]])+data[0x31b:]
        elif e=="poleVault":
            data = data[:0x344]+bytes([v[1]%256, v[1]//256, v[0]%256, v[0]//256])+data[0x348:]
        elif e=="tripleJump":
            data = data[:0x34c]+bytes([v[1]%256, v[1]//256, v[0]%256, v[0]//256])+data[0x350:]
        elif e=="hammerThrow":
            data = data[:0x33c]+bytes([v[1]%256, v[1]//256, v[0]%256, v[0]//256])+data[0x340:]
        elif e=="marathon":
            data = data[:0x321]+bytes([v[2], v[1], v[0]])+data[0x324:]
        elif e=="tennis":pass
        elif e=="swimming":
            data = data[:0x330]+bytes([v[2], v[1], v[0]])+data[0x333:]
        elif e=="diving":
            data = data[:0x354]+bytes([v[1]%256, v[1]//256, v[0]%256, v[0]//256])+data[0x358:]
        elif e=="synchroSwim":
            data = data[:0x374]+bytes([v[1]%256, v[1]//256, v[0]%256, v[0]//256])+data[0x378:]
        elif e=="beachVolley":pass
        elif e=="sailing":
            data = data[:0x328]+bytes([v[2], v[1], v[0]])+data[0x32b:]
        elif e=="riding":
            data = data[:0x36c]+bytes([v[1]%256, v[1]//256, v[0]%256, v[0]//256])+data[0x370:]
        elif e=="carrotPull":
            data = data[:0x35c]+bytes([v[1]%256, v[1]//256, v[0]%256, v[0]//256])+data[0x360:]
        elif e=="archery":
            data = data[:0x364]+bytes([v[1]%256, v[1]//256, v[0]%256, v[0]//256])+data[0x368:]
    return data

def GetPB(data, e):
    v = None
    if e=="dash100hm":
        v = (data[0x312], data[0x311], data[0x310])
    elif e=="hurdles":
        v = (data[0x31a], data[0x319], data[0x318])
    elif e=="poleVault":
        v = (data[0x346]+data[0x347]*256, data[0x344]+data[0x345]*256)
    elif e=="tripleJump":
        v = (data[0x34e]+data[0x34f]*256, data[0x34c]+data[0x34d]*256)
    elif e=="hammerThrow":
        v = (data[0x33e]+data[0x33f]*256, data[0x33c]+data[0x33d]*256)
    elif e=="marathon":
        v = (data[0x323], data[0x322], data[0x321])
    elif e=="tennis":pass
    elif e=="swimming":
        v = (data[0x332], data[0x331], data[0x330])
    elif e=="diving":
        v = (data[0x356]+data[0x357]*256, data[0x354]+data[0x355]*256)
    elif e=="synchroSwim":
        v = (data[0x376]+data[0x377]*256, data[0x374]+data[0x375]*256)
    elif e=="beachVolley":pass
    elif e=="sailing":
        v = (data[0x32a], data[0x329], data[0x328])
    elif e=="riding":
        v = (data[0x36e]+data[0x36f]*256, data[0x36c]+data[0x36d]*256)
    elif e=="carrotPull":
        v = (data[0x35e]+data[0x35f]*256, data[0x35c]+data[0x35d]*256)
    elif e=="archery":
        v = (data[0x366]+data[0x367]*256, data[0x364]+data[0x365]*256)
    return v

def SetWR(data, **events):
    for e, v in events.items():
        if e=="dash100hm":
            data = data[:0x390]+bytes([v[2], v[1], v[0]])+data[0x393:]
        elif e=="hurdles":
            data = data[:0x394]+bytes([v[2], v[1], v[0]])+data[0x397:]
        elif e=="poleVault":
            data = data[:0x3a4]+bytes([v[1]%256, v[1]//256, v[0]%256, v[0]//256])+data[0x3a8:]
        elif e=="tripleJump":
            data = data[:0x3a8]+bytes([v[1]%256, v[1]//256, v[0]%256, v[0]//256])+data[0x3ac:]
        elif e=="hammerThrow":
            data = data[:0x3a0]+bytes([v[1]%256, v[1]//256, v[0]%256, v[0]//256])+data[0x3a4:]
        elif e=="marathon":
            data = data[:0x399]+bytes([v[2], v[1], v[0]])+data[0x39c:]
        elif e=="tennis":pass
        elif e=="swimming":
            data = data[:0x39c]+bytes([v[2], v[1], v[0]])+data[0x39f:]
        elif e=="diving":pass
        elif e=="synchroSwim":pass
        elif e=="beachVolley":pass
        elif e=="sailing":pass
        elif e=="riding":pass
        elif e=="carrotPull":
            data = data[:0x3ac]+bytes([v[1]%256, v[1]//256, v[0]%256, v[0]//256])+data[0x3b0:]
        elif e=="archery":pass
    return data


def GetWR(data, e):
    v = None
    if e=="dash100hm":
        v = (data[0x392], data[0x391], data[0x390])
    elif e=="hurdles":
        v = (data[0x396], data[0x395], data[0x394])
    elif e=="poleVault":
        v = (data[0x3a6]+data[0x3a7]*256, data[0x3a4]+data[0x3a5]*256)
    elif e=="tripleJump":
        v = (data[0x3aa]+data[0x3ab]*256, data[0x3a8]+data[0x3a9]*256)
    elif e=="hammerThrow":
        v = (data[0x3a2]+data[0x3a3]*256, data[0x3a0]+data[0x3a1]*256)
    elif e=="marathon":
        v = (data[0x39b], data[0x39a], data[0x399])
    elif e=="tennis":pass
    elif e=="swimming":
        v = (data[0x39e], data[0x39d], data[0x39c])
    elif e=="diving":pass
    elif e=="synchroSwim":pass
    elif e=="beachVolley":pass
    elif e=="sailing":pass
    elif e=="riding":pass
    elif e=="carrotPull":
        v = (data[0x3ae]+data[0x3af]*256, data[0x3ac]+data[0x3ad]*256)
    elif e=="archery":pass
    return v
