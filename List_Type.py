#takes a list and prints a message for each element in the list, based on that element's data type

l = ['magical unicorns',19,'hello',98.98,'world']
j = [2,3,1,7,4,12,]
d = ['magical unicorns','hello','world']

def typeList(arr):
    newArr = []
    numSum = 0
    for i in arr:
        if type(i) == str:
            newArr.append(i)
        elif type(i) ==  float or int:
            numSum+=i
    if numSum > 0 and newArr != []:
        print "The list you entered is of mixed type"
        print "String: " + " ".join(newArr)
        print "Sum: " + str(numSum)
    elif numSum > 0:
        print "The list you entered is of integer type"
        print "Sum: " + str(numSum)
    elif newArr != []:
        print "The list you entered is of string type"
        print "String: "+ " ".join(newArr)

typeList(l)
