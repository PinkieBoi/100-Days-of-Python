total_bill = float(input("What was the total bill?\n$"))
tip_percentage = float(input("What percentage tip would you like to give?\n")) / 100
bill_inc_tip = (total_bill * tip_percentage) + total_bill
split_bill = int(input("How many people to split the bill?\n"))
print("Each person should pay: $" + str(round(bill_inc_tip / split_bill, 2)))
