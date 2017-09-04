#program that prints a multiplication table in your console.

def multiplicationTable(num):
    space = "   "
    for row in range(1, num+1):
        if num > 10:
            space = " "
        elif num > 100:
            space = ""
        print(space.join(str(row*col) for col in range(1, num+1)))
        print num

multiplicationTable(12)