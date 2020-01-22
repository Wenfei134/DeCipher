import enchant
d = enchant.Dict("en_US")
def isword(a):
    word = a.capitalize()
    return d.check(str(word))

def strtolist(str):
    line = str
    return line.split()

def ignrpunct(str):
    char = list(map(chr, range(97, 123)))
    acceptedchar = char.append(chr(39))
    words = str.lower()
    for i in words:
        if i not in char:
            words = words.replace(i, "")
    return words

def cipher(str):
    char = list(map(chr, range(97, 123)))
    newstr = ""
    words = str.lower()
    for i in words:
        if i in char:
            newstr += (chr ((ord(i) - 18) % 26 + 97))
        else: newstr += i
    return newstr

def count(lst):
    count = 0
    for i in lst:
        if isword(i):
            count += 1
    return count

def allpos(str):
    dictofcount = {}
    listofstrings = []
    listofwords = strtolist(str)
    string = map(cipher, listofwords)
    cstring = map(cipher, string)
    while cstring != string:
        strc = " ".join(cstring)
        dictofcount[strc] = count(cstring)
        cstring = map(cipher, cstring)
    return dictofcount

def maxofdict(a):
    wordDict = a
    listofcount = []
    cmax = 0
    for key in wordDict:
        if wordDict[key] > cmax:
            cmax = wordDict[key]
    maxValue = cmax
    for key in wordDict:
        if wordDict[key] == maxValue:
            return key
            break

def decipher(str):
    dictofwords = allpos(str)
    return maxofdict(dictofwords)

x = input('Enter your message to decode: ')
print decipher(str(x))