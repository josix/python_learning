# use property to get/set attribute value
class Duck():
	def __init__(self, input_name):
		self.hidden_name = input_name
	def get_name(self): 
		print('inside the getter')
		return self.hidden_name
	def set_name(self, input_name):
		print('inside the setter')
		self.hidden_name = input_name
	# get_name is getter and set_name is setter. 
	name = property(get_name, set_name) # use set_name() and get_name() to define the properity of name
	# when you want to refer to name, it will call get_name() (you can also use get_name() directly just like getter)
	# on the other side, if you want to assign value to name, it will call set_name() (you can also use get_name() directly just like setter)
fowl = Duck('Allen')
print(fowl.name)
fowl.name = 'Tony'
print(fowl.name)

print()

# another way to define properity is using decorator.
class Duck():
	def __init__(self, input_name):
		self.hidden_name = input_name

	@property
	def name(self):
		print('inside the getter')
		return self.hidden_name

	@name.setter # use function's name to (FUNC.setter)
	def name(self, input_name):
		print('inside the setter')
		self.hidden_name = input_name

fowl = Duck('Howard')
print(fowl.name)	
fowl.name = 'Donald'
print(fowl.name)

print()
# property can also refer to a value which is after computing
class Circle():
	def __init__(self, radius):
		self.radius = radius
	@property
	def diameter(self):
		return 2*self.radius
c = Circle(5)
print(c.diameter)

c.radius = 3
print(c.diameter)
try:
	c.diameter = 10 # it will cause error because of no setter properity. It is usful for a read-only attribute.
except AttributeError as err:
	print(err) # can't set attribute

# for the private field attribute(can't see by other classes except defination class), python use __ to name a variable at the begining to protect them
print()
class Duck():
	def __init__(self, input_name):
		self.__name = input_name
	@property
	def name(self):
		print('In the getter')
		return self.__name
	@name.setter
	def name(self, input_name):
		print('In the setter')
		self.__name = input_name

fowl = Duck('Howard')
print(fowl.name)

fowl.name = 'Tony'
print(fowl.name)

try:
	print(fowl.__name) # cause a error because of python will mess up a the name and let external program couln't use it. (__name will become _Duck__name)
except AttributeError as err:
	print(err)
print(fowl._Duck__name)

# method types 

# some attributes and methods are parts of class. And also some attributes and methods are parts of objects which you want to build up. 
# when you see the self argument in the defination. It is a instance method. When you call it, python will pass the object to it.
# In contrast, class method will influences all class, and infuences all its objects inderictly.
 
# use @classmethod to declare the following function is class method
print()
class A():
	count = 0
	def __init__(self):
		A.count += 1
	def exclaim(self):
		print("I'm an A!")
	@classmethod
	def kids(cls): # use cls to be the first argument 
		print("A has", A.count, 'little objects.') # A.count is a class attribute(cls.conut) not object instance attribute (self.count)

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()

# the third method type is static method. It won't influence class and its object, it is build up only for convenience

class CoyoteWeapon():
	
	@staticmethod
	def commerical():
		print('This CoyoteWeapon has been brought to you by Acme')

CoyoteWeapon.commerical()# we could access this method although without this object's object 


# Duck typing ("If it looks like a duck and quacks like a duck, it must be a duck.")
# python's polymorphism is loose, you can use the same method on the different objects no matter what classes they belong to (no matter with inheritence)
print()
class Quote():
	def __init__(self, person, words):
		self.person = person
		self.words = words
	def who(self):
		return self.person
	def say(self):
		return self.words +'.'

class QuestionQuote(Quote):
	def say(self):
		return self.words + "?"
class ExclamationQuote(Quote):
	def say(self):
		return self.words + '!'

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), "says:", hunter.say())

hunted1 = QuestionQuote("Bugs Bunny", "What's up, doc")
print(hunted1.who(), 'says:', hunted1.say())

hunted2 = ExclamationQuote('Daffy Duck', "It is rabbit season")
print(hunted2.who(), 'says:', hunted2.say())
# All of the three say() method will show the different output, it is so called polymorphism
# Python can do more by making you execute any object's say() and who() (if therer is defination in its class) 
print()
class BabblingBrook():
	def who(self):
		return 'Brook'
	def say(self):
		return 'Babble'

def who_says(obj):
	print(obj.who(), 'says:', obj.say())

book = BabblingBrook()
who_says(book)
who_says(hunted2)
who_says(hunter)
who_says(hunted1)
