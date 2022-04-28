#Control Flow with if / else and Condtitional Operators
print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?\n"))
if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you are too small to ride this ride.")

#challenge #1 - Odd or Even. Intro to the Modulo - is written as a percentage sign (%) 
number = int(input("Which whole number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#challenge #2 - BMI Calulator 2.0
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight/(height**2))
if bmi <18.5:
    print(f"Your BMI is {bmi}. You are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}. You have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}. You are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}. You are obese.")   
else:
    print(f"Your BMI is {bmi}. You are clinically obese.")

#challenge #3 - Leap Year Checker
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year & 400 == 0:
             print(f"The {year} is a leap year.")
        else:
            print(f"{year} is not leap year.")
    else: 
        print(f"The {year} is a leap year.")
else:
    print(f"{year} is not leap year.")

#challenge #4 - Pizza Order 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
