# None is a special value, it is not False. It symbolize a missing value however it is different from empty value like '', [], {}, set()
# all of above is False but not None.

# setting default parameters value
def menu(wine, entree, dessert = 'pudding'):
	return {'wine' : wine,
			'entree' : entree,
			'dessert' : dessert}
print(menu('chardonnay', 'chicken'))
print(menu('chardonnay', 'chicken', 'doughnut'))

# another bad example
print()
def buggy(arg, result = []): 
	result.append(arg)
	print(result)
buggy('a')
buggy('b') # should be ['b']. Because the default parameter is calculated at defination,the value won't change
'''
fixed:

def buggy(arg, result = None):
	if result == None:
		result = []
	result.append(arg)
	print(result)
'''

# use * to collect the positional arguments
print()
def print_arg(*args): # star will turn several posioional parameters into tuple value (modularized)
	print("Positional argument tuple:", args)

print_arg()
print_arg("This", 'is', 'test', 1, 2, 3, ["list", 'is', 'also'], {'cake' : 1}, {'banan' : 2})

def print_more(required1, required2, *args):
	print("Need this one:", required1)
	print("Need this one:", required2)
	print("All the rest:", args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

# use ** to  collect the keyword arguments
print()
def print_kwargs(**kwargs): # double star will turn several keyword parameters into dict value (modularized)
	print("Keyword arguments:", kwargs)

print_kwargs(wine = 'merlot', entree = ' mutton', dessert = 'macaroon')

# docstring is a piece of message explaining the usage of function (increase readability)
print()
def echo(anything):
	"echo returns its  input argument" # this is docstring
	return anything
def print_if_true(thing, check):
	# this is long docstring
	''' 
	prints the first argument if a second argument is true.
	The operation is:
		1. Check whether the *second* is true
		2. If is, print the *first* argument
	'''
	if check:
		print(thing)
help(echo)
print(print_if_true.__doc__)

# funcion is also a object, you also can take it as argument or assign value to it, even return it.
# funcrion is inmutable.
print()
def answer():
	print(42)

def run_something(func):
	func()
run_something(answer) # without the () behind 'answer'. Because we take answer as a object and we are not going to call it.
def add_args(arg1, arg2):
	print(arg1 + arg2)

def run_some_with_args(func, arg1, arg2):
	func(arg1, arg2)

run_some_with_args(add_args, 5, 9)

def sum_args(*args):
	return sum(args)
def run_with_positional_arguments(func, *args):
	return func(*args) # missing star will lead to error because args is a tuple but we need iterative value
print(run_with_positional_arguments(sum_args, 1, 2, 3, 4))

# inner functoin is used to execute many times complex jobs in a function and avioid repeativly using loop
print()
def outter(a,b):
	def inner(c,d):
		return c+d
	return inner(a,b)

print(outter(1,4))

def knight(saying):
	def inner(quote):
		return "We are the knights who say '%s'" %quote
	return inner(saying)

print(knight("HI"))


def outter():
	print('A')
	def inner():
		print('B')
		return 'c'
	return inner()
test = outter()
print(test)

# Inner function could be closure.
# Closure is a function made up by other function in dynamic way, and we could change or remember value in the variable outside the closure
def knight2(saying):
	def inner2():
		return "We are the knights who say '%s'" %saying
	return inner2 # return a duplication of inner2 fuction which have stored a value in variable saying
a = knight2('Duck')
b = knight2('Hasenpfefer')
print(type(a), type(b))
print(a, b)
print(a(),'\n',b())

# lambda() function is using a one line statement to representat a function(anonymous) . It could replace small function.
print()
def edit_story(words, func):
	for word in words:
		print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):
	return word.capitalize() + '!'

edit_story(stairs, enliven)
print()
edit_story(stairs, lambda word: word.capitalize() + '!') 
# lambda function : (1)take one argument "word" (2)between colon and bracket is the defination of the function
# using lambda function when you need to define lots of small function, and even must remember their names

# generator is a object to produce python sequence. It don't need to consume memory when iterating sequence and it only execute once forever.
# the data input of iterator often comes from generator. e.g range()
print()
print(sum(range(1,101)))
def my_range(first = 0, last = 10, step = 1):
	number = first
	while number < last: 
		yield number # The only difference betessn generator function and general function def is that generator uses yield to replace return.# it won't interupt execution
		number += step

print(my_range, my_range())  
for x in my_range(): # when you iterate a generator, the generator function won't stop until the sequence has been over, and it will remember the place where it yield and continue when called next time
	print(x)

# generator comprehesion
number_things = ( number for number in range(1, 11))
print(number_things, type(number_things))
number_list = list(number_things)
print(number_list)
try_again = list(number_things) # the generator only can execute once. It won't store these sequence value in memery so we can't restart or backup them.
print(try_again) # it will be empty


# decorator is a function, it will receive a function and return another function. 
# It uses these elements: (1) inner function (2) *args **kwargs  (3) function which is regarded as argument
print()
def document_it(func):
	def new_function(*args, **kwargs):
		print("Running function:", func.__name__)
		print("Positional arguments:", args)
		print("keywards arguments:", kwargs)
		result = func(*args, **kwargs)
		print("result:", result)
		return result
	return new_function

def square_it(func):
	def new_function(*arg, **kwargs):
		result = func(*arg, **kwargs)
		return result * result
	return new_function

@square_it
@document_it # decorator (the closest execute first and so on)
def add_ints(a, b):
	return a+b

test = add_ints(1,4)
print(test)

'''
cooler_add_ints = document_it(add_ints) # manual decorator assignment
test = cooler_add_ints(3,5) 
print(test)
'''

# In function, we could't assign the golbal variable although we use the key word "global". 
# use id() to see every object's unique value.
# use locals() to see the local variables and value in dict
# use globals() to see the global variables and value in dict
print()
print()
animal = 'ftruitbat'

def chang_and_print_globals():
	global animal
	animal = 'wombat'
	print('inside change_and_print_global:', animal, id(animal))

print("ouside global:", animal, id(animal))
chang_and_print_globals()
print("ouside global:", animal, id(animal))

# In python, the variable names begin and end with _ or __ means this variable name is reserved. 
# Like a function name is stored at system variable function.__name__ and docstring is stored at function.__doc__