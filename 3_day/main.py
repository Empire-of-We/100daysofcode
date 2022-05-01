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
        if year % 400 == 0:
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
bill = 0
bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
        
print(f"Your bill is ${bill}.")

#Logical Operators (and / or / not)
print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0
if height >= 120:
    age = int(input("What is your age.\n"))
    if age < 12 :
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18: 
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok.  Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    photos =input("Do you want photos for an additional $3? Y or N\n")
    if photos == "Y":
        bill +=3
        print(f"Your bill is ${bill}.")
else: 
    print("You are too small to ride this ride.")

#challenge #5 Love calculator 
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
both_names = name1.lower() + name2.lower()

t = both_names.count("t")
r = both_names.count("r")
u = both_names.count("u")
e = both_names.count("e")

true = (t + r + u+ e)

l = both_names.count("l")
o = both_names.count("o")
v = both_names.count("v")
e = both_names.count("e")

love = (l + o + v + e)

love_score =(int(str(true) + str(love)))

if (love_score) < 10 or (love_score) > 90:
    print(f"Your score is {love_score}. You go together like Coke and Mentos.")
elif (love_score) >= 40 or (love_score) <=50:
    print(f"Your score is {love_score}. You are alright together.")
else: 
    print(f"Your love score is {love_score}.")
