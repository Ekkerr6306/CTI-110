## CTI-110 P1HW2
## This assignment/program calculates the amount of pizzas someone wants to order
##February 21, 2022
##Ryan Ekker

#Input Statement
print("Welcome to Freddy Fazbear's Online Pizza Service!")
print("How many pizzas are you going to be ordering today?")

#Math required for program to function
numStudents = int(input())
numSlices = numStudents * 3
numPizzas = numStudents/2

#Final Output statement
print("Number of students: ",numStudents)
print("Pizza Slices needed: ", numSlices)
print("Pizzas needed: ", numPizzas)
