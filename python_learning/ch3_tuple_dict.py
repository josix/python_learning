# Tuple is similar to list, th only different thing is that tuple is inmutalbe. Tuple is a constant list

# use () and , to create a tuple 
empty_tuple = ()
print(empty_tuple)
one_marx = 'Groucho', # one element tuple
print(one_marx)
marx_tuple = 'Groucho', 'Chico', "Harpo" # () is optional (more friendly to read)
print(marx_tuple)
a, b, c,  = marx_tuple # this is caled tuple unpacking(when the value isn't enough it will lead to error)
print('a is:', a, 'b is:', b,'c is', c)

# use tuple to exchange the value of elements
print()
one = '0123456789'
another = 'abcdefghijk'
print("original:\none:", one, "another:",another)
one, another = another, one
print("exchange:\none:", one,"another:", another)

# use tuple() to convert other sequence types
print()
print(tuple(['this', 'is', 'list']))
print(tuple("this is string"))

# the merits of tuple (1) less storage (2) constant (means that there is no way to change the element)(3) can be used as the key of dict
# (4) function use tuple as argument to pass data （5) the named tuple could be the simplified object replacement

print("\n<=====================================================================================================================================>\n")

# dictionary is similar to list, the difference between them are dict don't care about order and dict dont use index to access element
# however dict should asign every value to a unique 'key' which could be any imutable types(i.e bool, int, float, str(more often), tuple).
# dict is mutable, it could be changed, removed, added.
# it is also called "associative arry", "hash" or "hashmap" in other language

# use {} to create a dictionary
empty_dict = {}
print(empty_dict)
bierce = {
	"day" : "A period of twenty-four hours, mostly misspent",
	"positive" : "Mistaken at the top if one's voice",
	"misfortune" : "The kind of fortune that ever misses"
	}
print(bierce)

# use dict() to convert some key/value sequence(double elements squence) to dict
print()
lol = [['a', 'b'] , ['c', 'd'], ['e','f']]
print(dict(lol)) # the dict is made up in disorderly
lot = (["a","b"], ["c","d"], ["e", "f"])
print(dict(lot))
los = [("a",'b'), ('c','d'), ('e','f')]
print(dict(los))
tol = ["ab","cd","ef"]
print(dict(tol))
tos = ("ab", "cd", "ef")
print(dict(tos))

# use [key] to add or change a elements in dict
print()
pythons = {
		"Chapman" : "Graham",
		"Cleese" : "John",
		"Idle" : "Eric",
		"Jones" : "Terry",
		"Palin" : "Michael"}
print(pythons, len(pythons))
pythons["Gilliam"] = "Gerry"
print(pythons, len(pythons))
pythons['Gilliam'] = 'Terry'
print(pythons)
# remember the key must be unique otherwise the last one repeative key will replace previous
some_pythons ={
		"Graham" : "Chapman",
		"John" : "Cleese",
		"Eric" : "Idle",
		"Terry" : "Jones",
		"Michael" : "Palin",
		"Terry" : "Gilliam"} # assign "Gilliam" to key "Terry" to replace original one
print(some_pythons)

# use update() to combine dict
others = {
		"Marx" : "Groucho",
		"Howard" : "Moe"
		}
pythons.update(others)
print(pythons)
# when there is the same key in two dict, the second one will be adopted

# use del and [key] to delete element
print()
print(pythons)
del pythons["Marx"]
print(pythons)
del pythons["Howard"]
print(pythons)

# use clear() to clean up the dict
print()
pythons.clear()
print(pythons)

# use in to test whether key in the dict
print()
pythons = {
		"Chapman" : "Graham",
		"Cleese" : "John",
		"Jones" : "Terry",
		"Palin" : "Michael"}
print('Chapman' in pythons)
print('Palin' in pythons)
print('Bob' in pythons)

# use [key] to get a element
print()
print(pythons['Cleese']) # when the key doesn't exist will lead to errror

# use get() dict function to know key/value you want if exists
print()
print(pythons.get('Palin'))
print(pythons.get('Bob'))
print(pythons.get('Bob', "Not in pythons"))

# use keys() to get all keys in dict
print()
print(pythons.keys()) # it will return generator, and you can use list() to convert it to list( also in value() and items()) 
print(list(pythons.keys()))

# use values() to get all vlaues in dict
print()
print(pythons.values())
print(list(pythons.values()))
for value in pythons.values():
	print(value)

# use items() to get all key/value pairs (typing: tuple)
print()
print(pythons.items())
print(list(pythons.items()))

# use = to assign and copy() to duplicate ( tha same as list)
print()
signals = {
		"green" : "go",
		"yellow" : "go faster",
		"red" : "smile for the camera"
		}
saves_signals = signals
saves_signals['blue'] = "confuse everyone"
print(saves_signals, signals)

print()
signals = {
		"green" : "go",
		"yellow" : "go faster",
		"red" : "smile for the camera"
		}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals, original_signals)
