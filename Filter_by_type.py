#given some value, tests that value for its type
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

def filterByType(infoType):
    if type(infoType) == int:
        if infoType >= 100:
            return "that's a big number"
        elif infoType < 100:
            return "thats a small number"
    elif type(infoType) == str:
        if len(infoType) >= 50:
            return "Long Setence"
        else:
            return "Short sentence"
    elif type(infoType) == list:
        if len(infoType) >= 10:
            return "Big list"
        else:
            if infoType < 10:
                return "Short list"
filterByType(lL)