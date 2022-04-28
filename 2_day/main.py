#converting primitive data types 
num_char = len(input("What is your name?"))
new_num_char =str(num_char)
print("Your name has " + new_num_char + " characters.") 

#challenge #1 - Converting Data Types
two_digit_number = input("Type a two digit number: ")
a = int(two_digit_number[0])
b = int(two_digit_number[1])
print(a + b)

#challenge #2 - Mathmatical Operations - BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
print(int(int(weight)/float(height)**2.0))
print(float(int(weight)/float(height)**2.0))
print(round(int(weight)/float(height)**2.0,2))

#challenge #3 - F-Strings - Your Life in Weeks
age = input("What is your current age?")
n_age =int(age)
years_remaining = 90 - n_age
days_remain = years_remaining * 365
weeks_remain = years_remaining * 52
months_remaining = years_remaining * 12
print(f"You have {days_remain} days, {weeks_remain} weeks, {months_remaining} months left.")

