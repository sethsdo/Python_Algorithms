'''find and replace'''
words = "It's thanksgiving day. It's my birthday,too!"
words.replace('day', 'month')


x = [2,54,-2,7,12,98]

def max(x):
    print max(x)
def min(x):
    print min(x)

'''finding the first and last'''

x = ["hello",2,54,-2,7,12,98,"world"]

def firstAndLast(arr):
    newArr = []
    newArr += arr[0]
    newArr += arr[len(arr) - 1]
    return ''.join(newArr)

firstAndLast(x)

'''creating a new list'''

x = [19,2,54,-2,7,12,98,32,10,-3,6]

def newList(arr):
    arr.sort()
    newArr = []
    first = []
    for i in range(len(arr) / 2):
        first.append(arr[i])   
    newArr.append(first)
    j = len(arr) / 2
    for d in range(j, len(arr)):   
        newArr.append(arr[d])
    return newArr

newList(x)









    
