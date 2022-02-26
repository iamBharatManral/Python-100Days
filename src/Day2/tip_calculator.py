print()
print("Welcome to the tip calculator")
print()

bill = float(input("What was the total bill? Rs. "))
percent = int(input("What percentage tip would you like to give? (10, 12, or 15): "))
no_of_people = int(input("How many people to split the bill: "))

each_pays = (bill / no_of_people) * (1 + percent/100)

print()
print(f"Each person should pay: Rs. {round(each_pays,2)}")