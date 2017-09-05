#Assignment: Dictionary in, tuples out
#Write a function that takes in a dictionary and returns 
# a list of tuples where the first tuple item is the key and the second is the 

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dictionary_to_tuple(arr):
    return list(arr.items())
dictionary_to_tuple(my_dict)