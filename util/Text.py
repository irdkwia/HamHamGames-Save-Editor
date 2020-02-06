Chars = [None, None, None, None]

Chars[0] = u"\U0001f610\U0001f642\U0001f641\U0001f62d\U0001f61c\U0001f44a\U0001f44d♥\U0001f494\U0001f4a4      \U0001f322\U0001f4a1☄☀☁☂⚡☃⚘☘      ✉☎⏰\U0001f381\U0001f37d☆\U0001f43e@⦻♡      太郎ⓁⓇⒶⒷ+⇧⇩⇨      ⇦⇑⇓⇒⇐♪©"
Chars[1] = "ァアィイゥウェエォオ力ガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプへべぺホボポマミ ムメモャヤュユョヨラリルレロ ワ  ヲンヴ  ~ー…「」、。 ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらリるれろ わ  をんす『』★○△☐✕♪↑↓→← ♥"
Chars[2] = [chr(i) for i in range(248)]+[chr(i+249) for i in range(4)]
Chars[2][0x92]="’"
Chars[2][0x84]="“"
Chars[2][0x93]="”"
Chars[2][0x94]="”"

magicNumber = b'\x21\xff'

def decodeNative(ListBytes):
    StrDec = ""
    for i in range(len(ListBytes)//4):
        char = ListBytes[i*4+2]
        code = ListBytes[i*4+3]
        StrDec += Chars[code-3][char]
    return StrDec

def encodeNative(Str):
    ListBytes = b''
    for c in Str:
        for code, charList in enumerate(reversed(Chars)):
            code = len(Chars)-1-code
            try:
                num = charList.index(c)
                ListBytes += magicNumber + bytes([num, code+3])
                break
            except:pass
    return ListBytes


def convertencodable(Str):
    new_str = ""
    for c in Str:
        if ord(c)>=0x10000:
            new_str += ("\\U%08x" % ord(c)).upper()
        else:
            new_str += c
    return new_str

def convertunencodable(Str):
    new_str = ""
    i = 0
    while i<len(Str):
        if Str[i]=="\\":
            new_str += chr(int(Str[i+2:i+10], 16))
            i+=9
        else:
            new_str += Str[i]
        i+=1
    return new_str
