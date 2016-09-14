# magic method(special method)
# In statement a = 3 + 8
# Because of special method, it let the objects 3 and 8 know to do +, and also let 'a' know to use = to get answer 

# special method will be named with __ at begining and ending.
# like __init__, it will use its class's defination and arguments to initialize and build a object.

class Word():
	def __init__(self, text):
		self.text = text

	def equals(self, word2):
		return self.text.lower() == word2.text.lower()

first = Word('HA')
second = Word('ha')
third = Word('eh')

print(first.equals(second), first.equals(third))

# we want to change above into python-style, like "if first == second"

class Word():
	def __init__(self, text):
		self.text = text

	def __eq__(self, word2):
		return self.text.lower() == word2.text.lower()

first = Word('HA')
second = Word('ha')
third = Word('eA')
print(first == second, second == third, first == third)

'''
compare magic method:
__eq__(self, other) self == other
__ne__(self, other) self != other
__gt__(self, other) self > other
__lt__(self, other) self < other
__ge__(self, other) self >= other
__le__(self, other) self <= other

math magic methods:
__add__(self, other) self + other (also in str)
__sub__(self, other) self - other
__mul__(self, other) self * other (also in str)
__floordiv__(self, other) self // other
__truediv__(self, other) self /other
__mod__(self, other) self %  other
__pow__(self, other) self ** other

other magic methods:
__str__(self) str(self)  (often use this method to print the object itself)
__repr__(self) repr(self) (use it to output variable in iterative interpreter)
__len__(self) len(self)
'''

print(first) # it wno't print the content of object due to no __str__() defination 
'''
In iterative mode:
>>> first
<__main__.Word object at 0x01BFEB30> # due to no __repr__() defination
'''
print()
class Word():
	def __init__(self, text):
		self.text = text

	def __str__(self):
		return self.text

	def __repr__(self):
		return self.text

first = Word('ha')
print(first)

print()
# composition and aggregation will more reasonable than using class.
# Duck is-a Bird, but has-a Tail. Tail is not Duck, but it is a part of Duck ( => Duck is object, Bird is class, Tail is object. )

class Bill():
	def __init__(self, description):
		self.description = description

class Tail():
	def __init__(self, length):
		self.length = length

class Duck():
	def __init__(self, bill, tail):
		self.bill = bill
		self.tail = tail
	def about(self):
		print('This duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail' )

tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()
