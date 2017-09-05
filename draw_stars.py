#Part I
#Create a function called draw_stars() that takes a list of numbers and prints out *.
nl = [4, 6, 1, 3, 5, 7, 25]
def draw_stars(li):
    #print li
    for x in li:
        #print x
        print '*' * x
draw_stars(nl)

#Part II
#Allow a list containing integers and strings to be passed to the draw_stars() function
p = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(nli):
    #print li
    for x in nli:
        #print x
        if type(x) == int:
            print '*' * x
        elif type(x) == str:
            print str.lower(x[0]) * len(x)
draw_stars(p)
