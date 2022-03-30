## CTI-110 P1HW2
## This assignment/program calculates the amount of pizzas someone wants to order
## March 30, 2022
##Ryan Ekker
#print("How many students are you going to be ordering pizza for?")
#Input numStudents as int
#Print("Please enter the number of people per pizza.")
#Input SPP(Students per pizza) as float
#Set single_pizza = 5
#set tax = 0.06
#set numPizza 0
#Set if SPP == 1.5, run numPizza =int(numStudents/SPP)
#Set if SPP == 2, run numPizza =int(numStudents/SPP)
#Set if SPP == 3, run numPizza =int(numStudents/SPP)
#Set else to print("INVALID ENTRY! Please enter 1.5, 2, or 3. Please run again")
#Set total_price = (single_pizza + tax) * numPizza
#Print ("Number of students: ",numStudents)
#Print ("Pizza needed: ", numPizza)
#Print ("Price: ", "{:.2f}".format(total_price))



#Input Statement

print("How many students are you going to be ordering pizza for?")
numStudents = int(input())
print("Please enter the number of people per pizza(1.5, 2, or 3).")
SPP = float(input())

#Declared/given variables from assignment
single_pizza = 5
tax = 0.06
numPizza = 0

#If-else statement regarding the nummber of students per pizza(required for assignment)
if SPP == 1.5:
    numPizza =int(numStudents/SPP)
elif SPP == 2:
    numPizza = int(numStudents/SPP)
elif SPP == 3:
    numPizza =int(numStudents/SPP)
else:
    print("INVALID ENTRY! Please enter 1.5, 2, or 3. Please run again")
    exit()

total_price = (single_pizza + tax) * numPizza

#Final Output statement
print("Number of students: ",numStudents)
print("Pizza needed: ", numPizza)
print("Price: ", "{:.2f}".format(total_price))
