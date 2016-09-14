class Thing():
	pass

example = Thing()
print(Thing, example)

class Thing3():
	def __init__(self, letters):
		self.letters = letters

example2 = Thing3('xyz')
print(example2.letters)

class Thing2():
	letters = 'abc'

print(Thing2.letters)

class Element():
	def __init__(self, name, symbol, number):
		self.__name = name
		self.__symbol = symbol
		self.__number = number

	@property
	def name(self):
		return self.__name

	@property
	def symbol(self):
		return self.__symbol
	@property
	def number(self):
		return self.__number

	def dump(self):
		print(self.__name, self.number, self.symbol)

	def __str__(self):
		return (self.__name + str(self.number) + self.symbol)

element = Element('Hydrogen', 'H', 1)
print(element.name, element.number, element.symbol)

element_dict = {'name' : 'Hydrogen',
				'symbol' : 'H',
				'number' : 1}

hydrogen = Element(**element_dict)
print(hydrogen.name, hydrogen.number, hydrogen.symbol)
hydrogen.dump()
print(hydrogen)

class Bear():
	def eats(self):
		return 'berries'

class Rabbit():
	def eats(self):
		return 'clover'

class Octothrpe():
	def eats(self):
		return 'campers'
bear = Bear()
rabbit = Rabbit()
octothrpe = Octothrpe()
print(bear.eats(), rabbit.eats(), octothrpe.eats())

class Laser():
	def does(self):
		return 'disintegrate'

class Claw():
	def does(self):
		return 'crush'

class SmartPhone():
	def does(self):
		return 'ring'

class Robot():
	def __init__(self):
		self.laser = Laser()
		self.claw = Claw()
		self.smartPhone = SmartPhone()

	def does(self):
		return self.laser.does() + '\n' + self.claw.does() + '\n' + self.smartPhone.does()

print()
robot = Robot()
print(robot.does())