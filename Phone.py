# inheritance -- you can take all of the attributes from a class and create a 'sub class', which is like a parent-child relationship
# polymorphism -- all parent class methods and properties should work for a child class

# Parent class of phone
class Phone:
	def __init__(self, phone_number):
		self.number = phone_number
	
	def __str__(self):
		return f'{self.number}'

	def call(self, other_number):
		'''
			make a call to another phone's number
		'''
		print(f'calling {other_number} from {self.number}. ring ring ☎️')

	def text(self, other_number, message):
		'''
			send a message to another phone's number
		'''
		print(f'sending text from {self.number} to {other_number}')
		print(message)

# inheritance in python -- pass parent class into child class params
class IPhone(Phone): # inheritance part 1
	# make the child class's constructor
	def __init__(self, phone_number, generation, color):
		# pass data to the parent's constructor
		super().__init__(phone_number)
		self.generation = generation
		self.color = color
	
	def __str__(self):
		return f'{self.number} gen {self.generation} color {self.color} IPhone'

junes_iphone = IPhone('777-777-7777', '12s', 'gold')
print(junes_iphone)
westons_phone = Phone('661-618-4542')
aprils_phone = Phone('555-555-5555')
junes_iphone.call(aprils_phone.number)

westons_phone.call(aprils_phone.number)
aprils_phone.text(westons_phone.number, 'I am on the phone with June, I will call you back in a few')