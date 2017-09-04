#program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.
word_list = ['hello','world','my','name','is','Anna']
char = 'o'

def findChar(arr, ch):
    newArr = []
    for i in arr:
        if ch in i:
            newArr.append(i)
    return newArr

findChar(word_list, char)