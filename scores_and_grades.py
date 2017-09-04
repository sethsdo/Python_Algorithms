#Write a function that generates ten scores between 60 and 100. 
# Each time a score is generated, your function should display 
# what the grade is for a particular score. Here is the grade table:
import random
def grade_tracker(num):
    print "Scores and Grades"
    for i in range(num):
        random_num = random.randint(60, 100)
        if random_num < 70:
            grade = "D"
        elif random_num < 80:
            grade = "c"
        elif random_num < 90:
            grade = "B"
        else:
            grade = "A"
        print "Score: " + str(random_num) + "; Your grade is " + str(grade)
    print "End of the program. Bye!"

grade_tracker(10)