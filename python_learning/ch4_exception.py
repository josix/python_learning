# when erro happends, python uses exception to execute programs about it.
# use 'try' to encase the statement and use 'except' to deal with the error
short_list = [0,1,2,3]
position = 6
try:
	print(short_list[position]) #  if the statements in try won't cause error, python will skip the except
except: # it will catch any exceprion type.
	print("need a position between 0 and", len(short_list)-1, 'but got', position)
# when there are more than one error, you can also use any number certain exceptions 

# when you want to get other details about the exception, you can use 'except EXCEPTIONTYPE as NAME' to get complete object about the exception in  variable NAME
print()
short_list = [1,2,3]
while True:
	value = input('Position [q to quit]?')
	if value == 'q':
		break
	try:
		position = int(value)
		print(short_list[position])
	except IndexError as err:
		print('Bad index', position)
	except Exception as other:
		print("Something else broke:", other)


# create your own exception
print()
# need to learn class first