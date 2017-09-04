#program that compares two lists and prints a message depending on if the inputs are identical or not

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

list2_one = [1,2,5,6,5]
list2_two = [1,2,5,6,5,3]

list3_one = ['celery','carrots','bread','milk']
list3_two = ['celery','carrots','bread','cream']

def compare(list1, list2):
    if list1 == list2:
        print "The lists are the same"
    else:
        print "The lists are not the same"

compare(list_one, list_two)
compare(list2_one, list2_two)
compare(list3_one, list3_two)