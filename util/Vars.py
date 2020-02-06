from .Text import *

OFF_MONEY = 0xd4
MONEY_SIZE = 0x2

OFF_LOC = 0xd8
LOC_SIZE = 0x2

OFF_INFO = 0x3ba8
INFO_LENGTH = 0xc
INFO_SIZE = 0x42
INFO_MAX = 0x8

OFF_LANG = 0xcc
LANG_JAP = 0
LANG_ENG = 1
LANG_SPA = 2
LANG_FRE = 3
LANG_GER = 4
LANG_ITA = 5

OFF_EVT = 0x3dbc
NB_EVT = 16
EVT_DUMMY = 0 #For testing
EVT_NEW_FRIEND = 0
EVT_GIFT = 1
EVT_FREE_PLAY = 2
EVT_FLAG = 3
EVT_TROPHY = 4
EVT_CLOSE_FRIEND = 6
EVT_RECEIVED_HUMANS = 7
EVT_RECEIVED_TRAVIS = 8
EVT_9999_BASKETBALL = 11
EVT_9999_BALLOONS = 12
EVT_50_FRIENDS = 14

def SetMoney(data, money):
    data = data[:OFF_MONEY]+bytes([money%256, money//256])+data[OFF_MONEY+MONEY_SIZE:]
    return data

def GetMoney(data):
    return data[OFF_MONEY]+data[OFF_MONEY+1]*256


def SetLocation(data, loc):
    data = data[:OFF_LOC]+bytes([loc%256, loc//256])+data[OFF_LOC+LOC_SIZE:]
    return data

def GetLocation(data):
    return data[OFF_LOC]+data[OFF_LOC+1]*256



def SetLang(data, lang):
    data = data[:OFF_LANG]+bytes([lang])+data[OFF_LANG+1:]
    return data

def GetLang(data):
    return data[OFF_LANG]

def SetInfo(data, num, v):
    if num>=INFO_MAX:
        raise Exception("List index out of bounds")
    if len(v)>INFO_LENGTH:
        raise Exception("Too long value")
    off = OFF_INFO+INFO_SIZE*num
    data = data[:off] + bytes([len(v) * 2, len(v)]) + encodeNative(v) + bytes(INFO_SIZE-0x2-len(encodeNative(v))) + data[off+INFO_SIZE:]
    return data

def GetInfo(data, num):
    if num>=INFO_MAX:
        raise Exception("List index out of bounds")
    off = OFF_INFO+INFO_SIZE*num
    length = data[off+0x1]
    return decodeNative(data[off+0x2:off+0x2+length*4])


def GetEvent(data, num):
    if num>=NB_EVT:
        raise Exception("List index out of bounds.")
    data = data[:OFF_EVT+num//8]+bytes([data[OFF_EVT+num//8] | 2**(num%8)])+data[OFF_EVT+num//8+1:]

    return data

def DelEvent(data, num):
    if num>=NB_EVT:
        raise Exception("List index out of bounds.")
    data = data[:OFF_EVT+num//8]+bytes([data[OFF_EVT+num//8] & ~(2**(num%8))])+data[OFF_EVT+num//8+1:]

    return data

def HasEvent(data, num):
    if num>=NB_EVT:
        raise Exception("List index out of bounds.")
    return bool(data[OFF_EVT+num//8] & 2**(num%8))
