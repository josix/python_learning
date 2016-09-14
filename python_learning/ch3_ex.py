years_list = [ 1996, 1997, 1998, 1999, 2000, 2001 ] 
print(years_list[3], years_list[-1])
things = ["mozzarella", "cin derella", "salmonella"]
things[0] = things[0].title()
things[1] = things[1].title()
things[2] = things[2].title()
print(things)
things.remove('Cin Derella')
things.append('Nobel Prize')
print(things)
surperise = ["Groucho", "Chico", "Harpo"]
e2f = {"dog" : "chien",
		"cat" : "chat",
		"walrus" : "morse"}
print(e2f["walrus"])
f2e = {}
for key, value in e2f.items():
	f2e[value] = key
print(f2e)
print(f2e['chien'])
e2f_set = set(e2f)
print(e2f_set)
life = {
		'animals' : {
			'cats' : ['Henri', 'Grumpy', 'Lucy'],
			'octopi':{},
			'emus':{}},
		'plants':{},
		'others':{}}
print(life)
print(life['animals'])
print(life['animals']['cats'])
