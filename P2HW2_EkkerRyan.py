#CTI-110
#P2HW2_Score Avg
#Ryan Ekker
#March 14, 2022

#Display "Enter Score #1: "
#Input grade_1
#Display "Enter score #2: "
#Input grade_2
#Display "Enter score #3: "
#Input grade_3
#Display "Enter score #4: "
#Input grade_4
#Display "Enter score #5: "
#Input grade_5
#Display "Enter score #6: "
#Input grade_6
#Display "Enter score #7:
#Input grade_7
#Set grades 1-7 into list named grades
#Set low_grade = minimum in list grades
#Remove low_grade from list grades
#Set total = sum of modified list grades
#Set Average = total/6
#Display '-------Results-------'
#Display 'Lowest Score :',low_grade
#Display 'Modified list :',grades
#Display 'Scores average:', f'{average:.2f}'
#Display '---------------------'

grade_1 = float(input("Enter score #1: "))
grade_2 = float(input("Enter score #2: "))
grade_3 = float(input("Enter score #3: "))
grade_4 = float(input("Enter score #4: "))
grade_5 = float(input("Enter score #5: "))
grade_6 = float(input("Enter score #6: "))
grade_7 = float(input("Enter score #7: "))

grades = [grade_1, grade_2, grade_3, grade_4, grade_5, grade_6, grade_7]

low_grade = min(grades)
grades.remove(low_grade)


total = sum(grades)
average = total/6

print('-------Results-------')
print('Lowest Score :',low_grade)
print('Modified list :',grades)
print('Scores average:', f'{average:.2f}')
print('---------------------')
