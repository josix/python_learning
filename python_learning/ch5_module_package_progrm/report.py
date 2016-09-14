def description():
	"""Return random weather, just like the pros"""
	from random import choice
	possibility = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
	return choice(possibility)