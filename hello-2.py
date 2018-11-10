"""

import math
math.asin

#or
from math import asin
asin(.5)

import random
surname = input("What is your surname? :")
first_name = input("What is your first name? :")
middle_names = input("Please enter a maximum of 2 middle names. If you don't have one please enter 9 :")
year_of_birth = input("What year were you born? :")
month_of_birth = input("What month were you born? Please use two digits eg 01 :")
day_of_birth = input("What day were you born? Please use two digits eg 01 :")
a,b = middle_names.split(' ')
print(surname.upper()[:5],year_of_birth[2],month_of_birth,day_of_birth,year_of_birth[3],first_name.upper()[0],a.upper()[0],b.upper()[0],random.randint(0,9),random.randint(0,9),sep="")


#assigning a variable to the input and making it into an integer
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
#assigning variables to the answer of each calculation - calculating the answer
addition_result = number1 + number2
subtraction_result = number1 - number2
multiplication_result = number1 * number2
power_of_result = number1 ** number2
division_result = number1 / number2
#printing the calculation and answer
print()
print(number1,"added to",number2,"is",addition_result)
print(number1,"minus",number2,"is",subtraction_result)
print(number1,"mulitiplied by",number2,"is",multiplication_result)
print(number1,"to the power of",number2,"is",power_of_result)
print(number1,"divided by",number2,"is",division_result)


number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))

division_result = number1 / number2 #without remainders
integer_division_result = number1 // number2 #as an integer
modulus_result = number1 % number2 #remainder

print()
print(number1,"divided by",number2,"is",division_result)
print(number1,"divided by",number2,"is",integer_division_result)
print(number1,"divided by",number2,"has a remainder of",modulus_result)

#Using selection statements to check variables
#Ask user for the number
number = int(input("Enter a number 1-3:"))
#Check the value of the number
if number == 1:
    print("Number one")
if number == 2:
    print("Number two")
if number == 3:
    print("Number three")

#Works out whether a candidate passed or failed
score = int(input("Enter score:"))
if score > 50:
    print("You passed")
else:
    print("You failed")

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

print("You entered",number1,"and",number2)
print("They add up to",number1 + number2)

grade1 = int(input("Enter first grade: "))
grade2 = int(input("Enter second grade: "))
grade3 = int(input("Enter third grade:"))

average = (grade1 + grade2 + grade3) / 3
print(average)

fahrenheit = int(input("What degrees fahrenheit is it? "))
centigrade = (fahrenheit - 32) * (5/9)
print("That is",centigrade,"degrees centigrade")

###
height = int(input("What is your height in inches: "))
weight = int(input("What is your weight in stones: "))

height_in_cm = height * 2.54
weight_in_kg = weight * 6.364

print("Your height in centimetres is",height_in_cm,"and your weight in kilograms is",weight_in_kg)

"""

hours = int(input("How many hours have you worked today? "))
trains = int(input("How many trains have you made today? "))






            
              

    


