# OO Vocab
# Abstraction -- if you need more than one object of the same type (ie same props and methods) then you should make an object factory
# not abstraction! you should make a factory!
my_obj = {}
my_objec_2 = {}
# Encapsulation -- grouping data and the functions that manipulate the data together in an object
my_obj = {
	'prop': 10
	# have function here to change the prop
	# def my_method():
		# ...change the prop
}

# inheritance
# polymorphism

# CoffeeCup
# constructor -- this creates the objcts
	# capacity (how big the cup is)
	# amount (how much coffee is in the cup)
# class methods
	# fill (fill up the cup to the max)
	# empty (dump all the coffee out)
	# drink (drinking som of the coffe that is in the cup)

# class keyword PascalCaseName:
class CoffeeCup: # if you are not inheriting, parans () optional
	"""
		a cup that holds coffee
	"""
	# define the constructor using method override of __init__
	# __init__(self, ...props, ...props, ...)
	def __init__(self, capacity = 16): # default params
		self.capacity = capacity # pass in the size of the cup when you make a new cup
		self.amount = 0 # no coffee at first
	
	# change the string representation of the object
	# mehtod override of __str__
	# method override of __repr__
	# both of these have to return string
	def __str__(self):
		# return a string to see when the object is printed
		return f'This is a {self.capacity}oz CoffeeCup with {self.amount}oz currently in it ☕️'

	def fill(self):
		"""
			fills the cup to the max capacity
		"""
		self.amount = self.capacity
		return self # (optional) allow for method chaining 

	def empty(self):
		"""
			removes all coffee from the cup
		"""
		self.amount = 0
		return self

	def drink(self, size = 2):
		"""
			removes a small amount of coffee from the cup to be drunk
		"""
		self.amount -= size
		if (self.amount <= 0):
			self.amount = 0
		
		return self


junes_cup = CoffeeCup() # will use default param of 16oz capacity
junes_cup.fill().drink()
print(junes_cup)
aprils_cup = CoffeeCup(12) # classes do not return dictionaries
# print(aprils_cup)
# print(aprils_cup.capacity) # access props with dot notation
# print(dir(aprils_cup))
# aprils_cup.fill() # dot notation to invoke methods
# aprils_cup.drink(6)
# aprils_cup.drink(6)
# aprils_cup.drink(6)
# aprils_cup.fill()
aprils_cup.fill().drink(6)
# None.drink()
print(aprils_cup)