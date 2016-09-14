# some string's method and funtion   
# use len() to get the length of string(or other sequence type like list, tuple)
letters = 'abcdefghijklmnopqrstuvwxyz'
print('len():\nthe variable "letters" is:', letters)
print('len() will show the length of a string:',len(letters), '\n')

# use split() to split a string with specified token and genertae a list
todos = "get gloves,get mask,give cat vitamins,call ambulance"
todos_list = todos.split(",")
print("split():\nthe variable 'todos' is: ", todos)
print("split() can take the ',' as argument to split a string and genertae a list: ", todos_list)
print("split() split string with space, tab, and new line when got no argument: ", todos.split(), '\n')

# use join() to combine a string list and genertae string with specified string 
crysto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crysto_string = ", ".join(crysto_list)
print('join():\nthe variable "crysto_list" is : ', crysto_list)
print('join() will combine them with specified string: ', crysto_string, "\n")

#Example 
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moinst and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis wet that makes it die, not doubt.'''

print(poem[:13])
print(len(poem))
print(poem.startswith('All')) # startswith() will return Bool according to whether the string is begining with assigned string
print(poem.endswith('not doubt.'))
word = 'the'
print(poem.find(word)) #  return the first index of the appearence of word
print(poem.rfind(word))
print(poem.count(word))
print(poem.isalnum())

setup = 'A duck goes into a bar...., and duck duck duck.......'
print(setup.strip('.'))
print(setup.capitalize())#first letter uppercase
print(setup.title())
print(setup.upper())
print(setup.lower())
print(setup.swapcase())
print("typesetting:\n",setup.center(100))
print(setup.ljust((100)))
print(setup.rjust(100)) 
print(setup)

print("replace:\n",setup.replace('duck', 'wilson', 3))
