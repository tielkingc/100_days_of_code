print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = float(input("What percentage of tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))
ind_share = bill / people

total = round((ind_share + (ind_share*(tip/100))), 2)

print(f"Each person should pay: ${total}")