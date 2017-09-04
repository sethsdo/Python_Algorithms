#program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000

def fooBar(start, end): 
    for p in range(start, end + 1): 
        #checks for perfect square
        if p**0.5 == int(p**0.5):
            print str(p) + " Bar"
        #checks for prime
        else:
            for i in range(start, p):
                if p % i == 0:
                    print str(p) + " FooBar"
                    break
            else:
                print  str(p) + " Foo"
             
fooBar(1, 30)
