# use setdefault() and defaultdict() to dealwith missing key
period_table = {'Hydrogen': 1, 'Helium': 2}
print(period_table)
carbon = period_table.setdefault('Carbon', 12) # if key doens't exist, dict will use new value
print(carbon, period_table)
Helium = period_table.setdefault('Helium', 947) # if assign different default value, dict won't change anything
print(Helium, period_table)

print()
from collections import defaultdict
period_table = defaultdict(int) # defaultdict will add assign default value to any new key when a dict is built up. 
# It takes a function as argument and the function will return the value which will be assigned to the missing key. e.g int() will return default 0
'''
int() return 0
list() return []
dict() return {}
if no argument, the default value will be None
'''

period_table['Hydrogen'] = 1
print(period_table['Lead'], period_table)

def no_idea():
	return 'Huh?'

bestiary = defaultdict(no_idea)
'''
bestiary = defaultdict(lambda : 'Huh?')
'''
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['A'], bestiary['B'], bestiary['C'])

# create a counter 
food_counter = defaultdict(int)
foods = ['spam', 'spam', 'eggs', 'spam']
for food in foods:
	food_counter[food] += 1
for food, count in food_counter.items():
	print(food, count)

'''
another way:

food_counter = {}
foods = ['A', 'B', 'A', 'A']
for food in foods:
	if not food in food_counter:
		food_counter[food] = 0
	food_counter += 1

'''

print('<'+'='*130+'>')
print()
# use counter() to count items number
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
print(breakfast_counter.most_common()) # most_common() method will return all elements in desending, and also can return spefic number elements.
print(breakfast_counter.most_common(1))

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)
print('\noperand:\n',breakfast_counter + lunch_counter, '\n',breakfast_counter - lunch_counter, '\n',lunch_counter - breakfast_counter, \
	'\n',breakfast_counter & lunch_counter, '\n',breakfast_counter | lunch_counter)
# use + to combine, - to create difference, & to create intersection, | to create union(it will take large number as item)

print('<'+'='*130+'>')
print()
# use OrderedDict() to build a dict in order
from collections import OrderedDict
quotes = OrderedDict([
	("Moe", 'A wise guy, huh?'),
	('Larry', 'Ow!'),
	('Curly', 'Nyuk nyuk')])
for stooge in quotes:
	print(stooge) # the order won't change

print('<'+'='*130+'>')
print()
# stack + quene == deque
# deque is a double head sequence, it owns the stack and quene property at the same time. 
# Use deque when you want to add or delete from any end of sequence.
def palindrome(word):
	from collections import deque
	dq = deque(word)
	while len(dq) > 1:
		if dq.popleft() != dq.pop(): # popleft() will remove the leftest element and return it. pop() will remove the rightest element and return it.
			return False
	return True
'''
another way:
def palindrome(word):
	return word == word[::-1]

way 2:
lambda word: word == word[::-1]
'''
print(palindrome("A"))
print(palindrome("TEST"))
print(palindrome("TESET"))

print('<'+'='*130+'>')
print()
# use itertools to iterate progran struct

import itertools 
for item in itertools.chain([1, 2], ['a', 'b']): # chain() will iterate every element in the arguments as the argument is a sequence.
	print(item)

count = 0
for item in itertools.cycle([1,2]): # cycle() will iterate its argument forever
	if count == 20:
		break
	print(item)
	count += 1

print()
for item in itertools.accumulate([1,2,3,4]): # accumulate() will calculate the accumulative value 
	print(item)

print()
def multiply(a, b):
	return a**b
for item in itertools.accumulate([2,2,2,2,2], multiply): 
# the second argument is a func which will replace add operation,it required two arguments and return one output
	print(item)


print('<'+'='*130+'>')
print()
# use pprint() to print good-lookinf outcome
from pprint import pprint
quotes = OrderedDict([
	("Moe", 'A wise guy, huh?'),
	('Larry', 'Ow!'),
	('Curly', 'Nyuk nyuk')])
pprint(quotes)