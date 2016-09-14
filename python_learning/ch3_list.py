#lsit is common used to trace something in order and usually changed.

# generate a list
empyt_list = []
weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael'] 
another_empty_list = list()
print(weekdays, first_names, empyt_list, another_empty_list)

# create a list from other types
print()
print(list('list'))
a_tuple = ('ready', 'fire', 'aim')
print(list((a_tuple)))
birthday = "2016/08/03"
print(birthday.split("/"))

# use index to access a element
print()
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes, marxes[0], marxes[1], marxes[-1])# when index is out of range, it will lead to the exception
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'Fench hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
print(all_birds)
print(all_birds[0])
print(all_birds[0][1])

# use index to change element
print()
marxes[2] = 'Wanda'
print(marxes)

# use slice to access elements
print()
print(marxes[0:2], marxes[::2])
print(marxes[::-2], '\nreverse: ',marxes[::-1])

# use append() to add a element in the end of a list
print()
marxes.append('Zeppo') # no need to assign the value
print(marxes)

# use extend() or += to combine two list
print()
others = ['Gummo', 'Karl']
marxes.extend(others) # no need to assign value
print("raw + ", others, 'is : ', marxes)
marxes += others
print(marxes)
marxes.append(others)
print(marxes)

# use insert() and index to insert a element
print()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes)
marxes.insert(3, 'Gummo') # no need to assign value
print(marxes)
marxes.insert(10000, 'Karl')
print(marxes)

# use del,a statement, and index to delete a element
print()
del marxes[-1]
print(marxes)
del marxes[2]
print(marxes, len(marxes))

# use remove() and value to delete a element
print()
marxes.insert(2, 'Harpo')
print(marxes)
marxes.remove('Gummo')
print(marxes)

# use pop() and index to access a element then delete it
print()
temp = marxes.pop()
print('remove: ',temp,'\nmarxes:', marxes)
temp = marxes.pop(1)
print('remove:', temp, '\nmarxes', marxes)

# use index() and value to find a index of a element
print()
marxes.insert(1, 'Chico')
marxes.insert(100, 'Zeppo')
print(marxes)
index = marxes.index('Chico')
print(index)

# use in statement to test if element is in list
print()
print('Chico' in marxes)
print('bob' in marxes)

# use count() to count the number that a value show up in a list
print()
del marxes[-1]
print(marxes)
print(marxes.count('Harpo'))
print(marxes.count('Bob'))

# use join() to covert a list into string
print()
print(", ".join(marxes))

# use sort() and sorted() to sort elements
print()
sorted_marxer = sorted(marxes) # sorted() is gernal function to sort and return duplicate
print('marxes: ', marxes,'sorted_marxer: ', sorted_marxer)
marxes.sort()
print(marxes)
number = [1,2,2,3,5.0, 1.4, 3.2]
number.sort() # sort() is list function to sort a list although elements are not the same type
print(number)
number.sort(reverse = True)
print(number)

# use = to assign, copy() slicd[:] list() to copy 
print()
a = [1,2,3,4]
b = a 
print("a is: ", a,"\tb is: ", b)
b[3] = 'change b[3]'
print("a is: ",a,"\tb is: ", b)# a b change at the same time because they refer to the same object

a = [1,2,3,4]
c = list(a)
d = a[:]
e = a.copy()
print("a is: ", a, "\tc is:", c, "\td is" ,d, "\t e is: ", e)
a[0] = 'change a'
print("a is: ", a, "\tc is:", c, "\td is" ,d, "\t e is: ", e)
