#!/bin/python3 

#define the shoeclass
class shoes:
	
	def __init__(self, name, price):
		self.name = name
		self.price = float(price)
	
	def budget_check(self,budget): #function that checks the budget whether it is an integer or float and also rejects if it is not while asking you 
		if not isinstance(budget, (int,float)):
			print("Invalid entry.Please enter a number.")
			exit()
	
	def change(self, budget): #Function to calculate money left.
		return(budget - self.price)
	
	def buy(self, budget): #Function that checks the budget, compares whether the budget is able to buy a shoe , checker whether you have the exact amount or you will have change left and also thank the user for using the app.
		self.budget_check(budget)
		
		if budget >= self.price:
			print(f" You can purchasesome sneakers {self.name}")
			if budget == self.price:
				print("You have exactly enough money for these shoes.")
			else:
				print (f " You can buy these shoes and have ${self.change(budget)} left over ")
			exit("Thanks for using our shoe budget app")	
