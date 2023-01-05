from shoes import shoes

#Types of shoes and their price
low = shoes("Jordan 1s", 30)
medium =  shoes("Air Force 1s", 120)
High = shoes("Off Whites", 400)

try:
	shoe_budget = float(input("What is your shoe budget?"))
except ValueError:
	exit("Please enter a number.")

for shoes in [high, medium, low]:
	shoes.buy(shoe_budget)
	
