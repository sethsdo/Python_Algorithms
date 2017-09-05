#Assignment: Names
#Part 1

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]


# def names(obj):
#     for x in obj:
#         name = " "
#         for val in x.itervalues():
#             name += val
#             name+= " "
#         print name
# names(students)


#part 2


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def names(obj):
    for key, data in obj.items():
        print key
         #print data
        count = 1
        for value in data:
            temp = value["first_name"] + " " + value["last_name"]
            length = len(temp)
            print str(count) + " - " + temp + " - " + str(length)
            count += 1
            
names(users)