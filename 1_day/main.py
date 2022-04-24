# print('Day 1 - String Manipulation')
print("print('this is how you print string in a string')")

# print("String Concatenate is with a '+' sign.") 
print("e.g. print('Hello' + ' Kim')")

# Multiple lines of code can be created using one line of code with a backslash and 'n'. There is no space between the 'n' and next line starting word. 
print("Hello Kim\nHello Kevin\nHello World!")

#input('What is your name?')is different than print because it leaves a curser at the end for "input"
print("Hello " + input("What is your name?") + "!")

#count the length of a string
print(len (input ('What is your name? ')))
        
name = input ('What is your favorite food? ')
length = len(name)
print(length)

# Swap values of variables
a = input("a:")
b = input("b:")

c = a
a = b 
b = c

print("a:" + a)
print("b:" + b)
