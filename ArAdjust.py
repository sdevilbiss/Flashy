# """
# Adjust Arabic module?. 3 functions:
# Reverser takes the arabic string and reverses its order.
# Reshaper makes sure each letter is in its correct form by labeling its
# location in a word and selecting the correct form from the nexted list.
# isArabic tests if a character exists in the Arabic block of utf8.
# """

def Reverser(text):
    # Reverses order of characters in string text
    holder = ''
    for i in range(0, len(text)):
        holder = text[i] + holder
    return holder


def Reshaper(text):
    holder = ''
    AlifBa = [['\uFE8D', '\uFE8E', '\uFE8E', '\uFE8D', '\u0627'],  # 2ali
              ['\uFE91', '\uFE92', '\uFE90', '\uFE8F', '\u0628'],  # baa
              ['\uFE97', '\uFE98', '\uFE96', '\uFE95', '\u062A'],  # taa
              ['\uFE9B', '\uFE9C', '\uFE9A', '\uFE99', '\u062B'],  # thaa
              ['\uFE9F', '\uFEA0', '\uFE9E', '\uFE9D', '\u062C'],  # jiim
              ['\uFEA3', '\uFEA4', '\uFEA2', '\uFEA1', '\u062D'],  # Haa
              ['\uFEA7', '\uFEA8', '\uFEA6', '\uFEA5', '\u062E'],  # khaa
              ['\uFEA9', '\uFEAA', '\uFEAA', '\uFEA9', '\u062F'],  # dal
              ['\uFEAB', '\uFEAC', '\uFEAC', '\uFEAB', '\u0630'],  # dhal
              ['\uFEAD', '\uFEAE', '\uFEAE', '\uFEAD', '\u0631'],  # raa
              ['\uFEAF', '\uFEB0', '\uFEB0', '\uFEAF', '\u0632'],  # zayn
              ['\uFEB3', '\uFEB4', '\uFEB2', '\uFEB1', '\u0633'],  # siin
              ['\uFEB7', '\uFEB8', '\uFEB6', '\uFEB5', '\u0634'],  # shii
              ['\uFEBB', '\uFEBC', '\uFEBA', '\uFEB9', '\u0635'],  # Saad
              ['\uFEBF', '\uFEC0', '\uFEBE', '\uFEBD', '\u0636'],  # Daad
              ['\uFEC3', '\uFEC4', '\uFEC2', '\uFEC1', '\u0637'],  # Taa
              ['\uFEC7', '\uFEC8', '\uFEC6', '\uFEC5', '\u0638'],  # Zaa
              ['\uFECB', '\uFECC', '\uFECA', '\uFEC9', '\u0639'],  # 2ayn
              ['\uFECF', '\uFED0', '\uFECE', '\uFECD', '\u063A'],  # ghayn
              ['\uFED3', '\uFED4', '\uFED2', '\uFED1', '\u0641'],  # faa
              ['\uFED7', '\uFED8', '\uFED6', '\uFED5', '\u0642'],  # qaaf
              ['\uFEDB', '\uFEDC', '\uFEDA', '\uFED9', '\u0643'],  # kaaf
              ['\uFEDF', '\uFEE0', '\uFEDE', '\uFEDD', '\u0644'],  # laam
              ['\uFEE3', '\uFEE4', '\uFEE2', '\uFEE1', '\u0645'],  # miim
              ['\uFEE7', '\uFEE8', '\uFEE6', '\uFEE5', '\u0646'],  # nuun
              ['\uFEEB', '\uFEEC', '\uFEEA', '\uFEE9', '\u0647'],  # haa
              ['\uFEED', '\uFEEE', '\uFEEE', '\uFEED', '\u0648'],  # waaw
              ['\uFEF3', '\uFEF4', '\uFEF2', '\uFEF1', '\u064A'],  # yaa
              ['\uFE81', '\uFE82', '\uFE82', '\uFE81', '\u0622'],  # 2alif madda
              ['\uFE93', '\uFE94', '\uFE94', '\uFE93', '\u0629'],  # taa marbuuTah
              ['\uFEEF', '\uFEF0', '\uFEF0', '\uFEEF', '\u0649'],  # 2alif maqSuura
              ]
    # A list of each of the standard Arabic letters that does not connect
    # to the following letter.
    selfish = ['\uFE8D', '\uFE8E', '\uFEA9', '\uFEAA', '\uFEAB',
               '\uFEAC', '\uFEAD', '\uFEAE', '\uFEAF', '\uFEB0',
               '\uFE81', '\uFE82', '\uFE93', '\uFE94', '\uFEEF',
               '\uFEF0', '\u0627', '\u062F', '\u0630', '\u0631',
               '\u0632', '\u0632', '\u0621', '\u061F', ' ']
    # character with only one form
    loners = [' ', '؟', 'ء']
    # keys for the index in the s.AlifBa list for the specific letter forms
    ArBeg = 0
    ArMid = 1
    ArEnd = 2
    ArIso = 3
    # contexts that trigger each form
    context = {ArIso: [['Nothing', 'Nothing'], ['Nothing', 'Selfish'],
                       ['Nothing', 'Space'], ['Space', 'Nothing'],
                       ['Space', 'Selfish'], ['Space, Space']],
               ArBeg: [['Connect', 'Selfish'], ['Connect', 'Space'],
                       ['Connect', 'Nothing']],
               ArMid: [['Connect', 'Connect']],
               ArEnd: [['Space', 'Connect'], ['Nothing', 'Connect']]}
    for i in range(0, len(text)):
        # list to be compared with the context dictionary for specific char
        charContext = []
        if text[i] not in loners:
            # What comes before the char?
            if i is 0:                          # first in string
                charContext.append('Nothing')
            elif text[i-1] is ' ':              # follows a space
                charContext.append('Space')
            else:                               # follows another char
                charContext.append('Connect')
            # What comes after the char?
            if i is len(text)-1:                # last in string
                charContext.append('Nothing')
            elif text[i+1] in selfish:          # precedes non-connect char
                charContext.append('Selfish')
            elif text[i+1] is ' ':              # precedes a space
                charContext.append('Space')
            else:                               # precedes a  nice char
                charContext.append('Connect')
            # loops through context for the right condition
            for k, v in context.items():
                for flanks in v:
                    # test condition. might have to check both indices for equivalency
                    if flanks == charContext:
                        form = k
            # applies correct form to the list from full Arabic alphabet
            for each in AlifBa:
                if text[i] in each:
                    holder = holder + each[form]
        # adds any char that has only one form.
        else:
            holder = holder + text[i]
    return holder


def isArabic(char):
    if 1536 < ord(char) < 2303 or 65136 < ord(char) < 65279:
        return True
    else:
        return False
