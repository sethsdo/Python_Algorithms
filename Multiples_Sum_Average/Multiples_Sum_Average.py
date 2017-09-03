#this is a comment
#Multiples
#prints the odd numbers between 1 and 1000
def oddNumCount(num):
    for i in range(1, num, 2):
        print i

oddNumCount(1000)

#prints the multiples of 5
def multOfFive(num):
    for i in range(5, num, 5):
            print i
multOfFive(100)

#print the sum of all the values in a list
a = [1, 2, 5, 10, 255, 3]
def sumOfList(arr):
    count = 0 
    for i in arr:
        count += i
    return count
sumOfList(a)

#finds the average of a list 
a = [1, 2, 5, 10, 255, 3]
def avgOfList(arr):
    count = 0 
    for i in arr:
        count += i
    return count/ len(arr)
avgOfList(a)
