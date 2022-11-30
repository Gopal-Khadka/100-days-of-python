# tip and bill calculator
print("Welcome the tip calculator:")
bill = float(input("How much is your bill ?\n"))

tip_percent = float(input("What percent would you like to tip?\n"))
finalAmt= bill* ( 1 + tip_percent/100)

People = int(input("How many people to split the bill?\n"))
splitAmt = finalAmt /(People)
message = f"The final bill amount is {round(finalAmt,2)} and split amount for {People} people is {round(splitAmt,2)}"
print(message) 
print("HAPPY SPLITTING!!!") 