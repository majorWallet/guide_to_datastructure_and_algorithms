def findAlphabet(str):
    hashTable = {
    ' ' : False
    ,'a' : False
    ,'b' : False
    ,'c' : False
    ,'d' : False
    ,'e' : False
    ,'f' : False
    ,'g' : False
    ,'h' : False
    ,'i' : False
    ,'j' : False
    ,'k' : False
    ,'l' : False
    ,'m' : False
    ,'n' : False
    ,'o' : False
    ,'p' : False
    ,'q' : False
    ,'r' : False
    ,'s' : False
    ,'t' : False
    ,'u' : False
    ,'v' : False
    ,'w' : False
    ,'x' : False
    ,'y' : False
    ,'z' : False
    }
    for i in str:
        hashTable[i] = True

    for i in hashTable:
        if not hashTable[i]:
            return i

    return "null"

print(findAlphabet("the quick brown box jumps over a lazy dog"))