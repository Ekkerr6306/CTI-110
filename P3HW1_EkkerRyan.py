# The objective of this program is to take a grade inputted from a user and display
# the appropriate letter grade to go with it.
# March 7,2021
#CTI-110 P3HW1 Debugging
#Ryan Ekker

#Set A_score = 90
#Set B_score = 80
#Set C_score = 70
#Set D_score = 60
#Set score equal to user input
#Define if score is greater than or equal to A score print 'Your grade is: A'
#Define if score is greater than or equal to B score print 'Your grade is: B'
#Define if score is greater than or equal to C score print 'Your grade is: C'
#Define if score is greater than or equal to D score print 'Your grade is: D'
#Define if none of the criteria is met print 'Your grade is: F'

def mainNested():
    # system uses 10-point grading scale
    A_score = 90
    B_score=80
    C_score=70
    D_score=60
    #F_score=50

    #input for letter grade
    score = float(input('Enter grade: '))

#IF-else statement to print letter grade
    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score:
            print('Your grade is: B')
        else:
            if score >= C_score:
                print('Your grade is: C')
            else:
                if score >= D_score:
                    print('Your grade is: D')
    
                else:
                    print('Your grade is: F') 

#This is the nested elif example of how to do this assignment.
'''
def mainElif():
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    score = float(input('Enter grade: '))
    
    if score >= A_score:
        print("Your grade is A")
    elif score >= B_score:
        print("Your grade is B")
    elif score >= C_score:
        print("Your grade is C")
    elif score >= D_score:
        print("Your grade is D")
    else:
        print("Your grade is F")
'''
mainNested()
mainNested()
mainNested()
mainNested()
mainNested()
