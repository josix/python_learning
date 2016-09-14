guess_me = 7
start = 1
while start <= guess_me:
	if guess_me > start:
		print('too low')
	elif guess_me < start:
		print('too large')
		print('oops')
	else:
		print('just right')
		print('found it!')
	start += 1
print()

for i in [3,2,1,0]:
	print(i)

even_list = [number for number in range(0,10,2)]
print(even_list)

squares = {key:key**2 for key in range(10)}
print(squares)

odd_set = {number for number in range(1,10,2)}
print(odd_set)

got_numbers = ('Got ' + str(number) for number in range(10))
for number in got_numbers:
	print(number)

def good():
	return ['Harry', 'Ron', 'Hermione']
x = good()
print(x)

def get_odds():
	for number in range(1,10,2):
		yield number
count = 0
for number in get_odds():
	if count == 2:
		print(number)
	count += 1

def test(func):
	def new_function(*args, **kwargs):
		print('start')
		result = func(*args, **kwargs)
		print('end')
		return result
	return new_function

@test
def add_args(arg1, arg2):
	return arg1 + arg2

x = add_args(1,2)
print(x)

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster','A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movies)