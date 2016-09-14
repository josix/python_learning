# when while is done and hasn't call break statement, it will pass control right to a optional else 
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
	number = numbers[position]
	if number % 2 == 0:
		print("find even number", number)
		break
	position += 1
else: # else could be a break checker
	print("No even number found")

# use for to iterate
# iterator help you traversal every elements without knowing how big a data structer is.  
print()
rabbits = ['Flopsy', 'Monpsy', 'Cottontail', 'Peter']
for rabbit in rabbits:
	print(rabbit)
# list, string, tuple, dict, set, and some other elements are able to iterate
# iterate a string will return a character
# list and tuple will return a element 
# dict will return a key(use value() to iterate value) (use items() and tuple to iterate keys and values)

# for loop also have continue, break, else

# use zip() to iterate several sequence in abreast way ( return a iterable object)
print()
days = ['Mon', 'Tue', 'Wed']
fruits = ['banan', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
	print("day:", day, "fruit:", fruit, "drink:", drink, "dessert:", dessert)
	# end up when the shortest sequence is over
# another usage of zip() is using zip() to check each elements and put the same index element in a new tuple then to covert to dict
english = 'Monday', 'Tuesday', "Wednesday"
french = 'Lundi', 'Mardi', 'Mercredi'
combined_list = list(zip(english, french))
print(combined_list)
e2f = dict(combined_list)
print(e2f)

# use range() to produce number sequence [range(START, STOP, STEP)] (will stop at STOP-1)
print()
for x in range(5): # range will return a object which is iterable, like zip()
	print(x)
print(list(range(5)))
print()
for x in range(2,-1,-1):
	print(x)
print(list(range(2,-1,-1)))
print(list(range(0,11, 2)))

# Comprehension is a way to build up python data structer by one or more iterator
# List comprehension  [EXPRESSION for ELEMENT in ELEMENTS(iterative)]
print()
number_list = [number for number in range(1,6)] # the first one number is to get the output and put in list during loop. the second one is a part of for loop
print(number_list)
number_list = [number - 1 for number in range(1, 6)]
print(number_list)
a_list = [number for number in range(1,6) if number % 2 == 1]
print(a_list)
cells = [(row,column) for row in range(1,3) if True for column in range(1,4) if True] 
'''
 new_list = []
 rows = range(1,3)
 cols = range(1,4)
 for row in rows:
 	for col in cols:
		new_list.append(row,col)
'''
print(cells)

# Dictionary comprehension {KEY-EXPRESSION : VALUE-EXPRESSION for ELEMENT in ELEMENTS(iterative)}
print()
word = 'letters'
letter_counts = {letter : word.count(letter) for letter in word}
print(letter_counts)
# more python style
letter_counts_pystyle = {letter : word.count(letter) for letter in set(word)}
print(letter_counts_pystyle)

# Set comprehension {EXPRESSION for ELEMENT in ELEMENTS(iterative)}
print()
a_set = {number for number in range(10) if number % 2 == 0}
print(a_set)

# There is no tuple comprehension but a generator comprehension