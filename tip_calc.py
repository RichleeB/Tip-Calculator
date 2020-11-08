print("Please use this tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("How much % would you like to give? Please enter 10 , 12, or 15. Anything less and you are too cheap to need this calculator.. Enter number:  "))


tip_calc = bill * tip/100

total_bill = bill + tip_calc

patrons = int(input("Number of people splitting the bill: "))

amount_due = total_bill / patrons 

print(f"Each person should pay {amount_due:.2f}")