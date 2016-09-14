# named tuple is a sub class of tuple. You can use name( .name) and position ( [offset]) to acess value
from collections import namedtuple # need to import a module
Duck = namedtuple('Duck', 'bill tail') # named tuple takes two arguments: name, and fields(sperated with space)
duck = Duck('wild orange', 'long')
print(duck)
print(duck.bill)

# use dict to build up named tuple
parts = {'bill' : 'wild orange', 'tail' : 'long'}
duck2 = Duck(**parts) # use keyword argument
'''
duck2 = Duck(bill = 'wild orange', tail = 'long')
'''
print(duck2)

# you can change one or more fields, and return another named tuple
duck3 =  duck2._replace(tail = 'magnificent', bill = 'crushing')
print(duck3)

print(duck3[:])

'''
named tuple's merits:

(1) it is like a inmutable object
(2) save storage
(3) you can use dot notation to repale [] to acess attribute
(4) yuo can use it as dict's key
'''