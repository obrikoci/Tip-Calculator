print ("Welcome to the tip calculator!")
print ("What was the total bill?")
bill = input()
new_bill = float(bill)
print ("What percentage tip would you like to give? 10, 12 or 15?")
tip = input()
new_tip = int(tip)
print ("How many people to split the bill?")
people = input()
new_people = int(people)
bill_per_each = round((new_bill + new_bill * (new_tip / 100)) / new_people, 2)
print (f"Each person should pay: ${bill_per_each}.")