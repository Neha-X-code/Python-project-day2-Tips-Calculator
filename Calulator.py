print("Calculate Tips Fast!\nWelcome to my tip calculator")
bill = float(input("Enter your total bill $"))
percent = int(input("What percentage tip would you like to give 10, 12 or 15?"))
people = int(input("How many people to split the bill"))
tip = (bill+(bill*(percent/100)))/people
tip1 = (round(tip,2))
print(f"Each person should pay: ${tip1}")