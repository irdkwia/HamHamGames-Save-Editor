from .CheckSum import *
from .Text import *
from binascii import hexlify

INIT_CHECK = 0x1cd
HEADER_SIZE = 0x8

def GetCheck(data):
    return Sum(data[0xc:0xcd])+Sum(data[0xcf:0xd6])+Sum(data[0xd8:])+INIT_CHECK

def ReupdateSave(data):
    diff = GetCheck(data)
    first = diff % 0x10000
    last = 0xffff - first
    data = data[:8]+bytes([first%256, first//256, last%256, last//256])+data[12:]
    return data

def GetSave(data, skipError = False):
    saves = [data[0x200:0x3fc4], data[0x4000:0x7dc4]]
    for save in saves:
        diff = GetCheck(save)
        first = diff % 0x10000
        last = 0xffff - first
        if first == save[8]+save[9]*256 and last == save[10]+save[11]*256:
            return save
    if not skipError:
        raise Exception("Save corrupted.")
    else:
        return saves[0]

def CreateSave(save, skipError = False):
    save = ReupdateSave(save)
    save = b'Hamtaro\x00'+save[HEADER_SIZE:]
    
    return bytes([0xff]*0x200)+save+bytes([0xff]*(0x4000-0x3fc4))+save+bytes([0xff]*(0x8000-0x7dc4))
