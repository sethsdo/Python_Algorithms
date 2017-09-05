#Write a function that simulates tossing a coin 5,000 times. 
# Your function should print how many times the head/tail appears.
import random

def coin_toss(num):
    count = 0
    heads = 0
    tales = 0
    print "Starting the program..."
    for count in range(1, num + 1):
        toss = round(random.random())
        if toss == 1:
            heads+=1
            last =  "Attempt # " + str(count) + ": Throwing a coin... It's a head! ... Got " + str(heads) + " head(s) so far and " +  str(tales) + " tail(s) so far"
        elif toss == 0:
            tales+=1
            last = "Attempt # " + str(count) + ": Throwing a coin... It's a tail! ... Got " + str(tales) + " head(s) so far and " +  str(heads) + " heads(s) so far"
        if count < 6:
            print last
            count += 1
    print "..."
    print last   

coin_toss(5000)