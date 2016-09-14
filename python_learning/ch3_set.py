# set is a dict which only keep key. set is used to store the unique and unorded data. 
# in order -> list, tuple(inmutable, to be key)  unorded and unique -> dict(assign value), set 

# use set(), {} to create a set
empty_set = set()
one_element_set = {"one"}
even_set = {0,2,4,6,8}
odd_set = {1,3,5,7,9}
print(empty_set, one_element_set, even_set, odd_set)

# use set() to convert other types (abort repeative value)
print()
print(set("this is string.")) # only keep one i,s,t when they are repeative
print(set(["this", "is", "list"]))
print(set(("this", "is", "tuple")))
print(set({"this" : 1, "is": 2, "dict" : 3}))

# use statement 'in' to test if value that you want exists
print()
drinks = {
		"martini" : {'vodka', 'vermouth'},
		"black russian" : {'vodka', 'kahlua'},
		"white russian" : {'cream', 'kahlua', 'vodka'},
		"manhattan" : {"rye", "vermouth", "bitters"},
		"screwdriver" : {"orange juice", "vodka"}}
for name, contents in drinks.items():
	if 'vodka' in contents:
		print(name)
	#print(name, contents) 
print()
for name, contents in drinks.items():
	if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
		print(name)

#  set operands
print()
for name, contents in drinks.items():
	if contents & {'vermouth', 'orange juice'}: # & will produce a set which contain two compared sets both have
		print(name)
print()
for name, contents in drinks.items():
	if contents & {'vodka'} and not contents & { 'vermouth','cream' }:
		print(name)
print()
bruss = drinks["black russian"]
wruss = drinks["white russian"]

a = {1,2}
b = {2,3}
print(a, b, bruss, wruss)
print( a & b, a.intersection(b), bruss & wruss) # the intersection of a and b, bruss and wruss
print(a | b, a.union(b), bruss | wruss) # the union of a and b, bruss and wruss
print(a - b,b - a, a.difference(b), bruss - wruss, wruss - bruss) # the difference of a and b, bruss and wruss
print(a ^ b, a.symmetric_difference(b), bruss ^ wruss) # the usage of symmetric_difference() 
print(a <= b , a <= a, b <= b, a.issubset(b) ,bruss <= wruss ) # the usage of issubset()
print(a < b , a < a, b < b, bruss < wruss) # the usage of the proper subset
print(a >= b, a >= a , b >= b , a.issuperset(b), bruss >= wruss) # the usage of issuperset(), superset is opposite to subset
print(a > b, a > b, b > b, wruss > bruss) # the usage of the proper superset
