#Assignment: Making Dictionaries
#Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. 
# Assume the lists will be of equal length.

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "wild"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    new_dict = dict(zip(arr1, arr2))
    return new_dict
make_dict(name, favorite_animal)


