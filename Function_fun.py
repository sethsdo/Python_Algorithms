#functon called odd_even that counts from 1 to 2000

def odd_even():
    for num in range(1, 10):
        if num % 2 == 0:
            print "even"
        else:
            print "odd"
odd_even()

#iterates through each value in a list (e.g. a = [2, 4, 10, 16]) 
# and returns a list where each value has been multiplied by 5.

a = [2,4,10,16]

def multiply(arr, num):
    for i in range(len(arr)):
        arr[i] *= num
    return arr

# Write a function that takes the multiply function call as an argument. 
# Your new function should return the multiplied list as a two-dimensional list. 
# Each internal list should contain the 1's times the number in the original list. Here's an example:
def layered_multiples(arr):
      # your code here
    print arr
    new_array = []
    for i in range(len(arr)):
        temp = []
        #print i
        for num in range(arr[i]):
            #print j
            temp.append(1)
        new_array.append(temp)
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
# output
#>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

