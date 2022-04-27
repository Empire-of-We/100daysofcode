#Tip Calculator
print('Welcome to the tip calculator!')
bill =float(input("What was the total bill?\n"))
tip =input("What percentage tip do you want to give? 10, 12, or 15?\n")
peeps =int(input("How many people to split the bill?\n"))
new_tip = int(tip)/100+1
split = float(bill*((new_tip)/peeps))
new_split =round(split,2)
new_split = "{:.2f}".format(new_split)
print(f"Each person should pay: ${new_split}")