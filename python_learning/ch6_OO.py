# object symbolize a example of something concrete, it owns its own attribute(variable) and method(function)
# e.g a int object which is assigned value 7, this kind of object coult use add and multiply methods.
# 8 is another object, but both of them belong to the same integer calss
# when you want to build a new object, you must build a class to declare what things are there.

# use 'class' to define class 
# use class to build a object. For instance, string ia a class, which is used to build object like 'car', 'test'.....

class Person(): # a empty class, it is the simplest class
	pass

someone = Person() # call a class to build a object. In this example, 'someone' could do nothing because of the empty class

class Person():
	def __init__(self):# it is a method which it will use its class definiton to initalize a object. 
		pass
# Argument 'self' means to refer to the class itself. Use 'self' to be the first argument is a habit to tell everyone include youself the meaning more clearlly.

class Person():
	def __init__(self, name):  
		self.name = name

hunter = Person('Elmer Fudd')
# first, it will call Person class and look up the defination
# second, it will instantiate(build) a ojbect in memory
# third, it will call the __init__ method passing the new object to self and 'Elmer Fudd' to name
# forth, store the value of name in object
# fifth, return object
# sisth, assign hunter to the object

print('the mighty hunter:', hunter.name) # the vaule passing to the name will be a attribute, storing with the object in memory

# __init__() isn't necessary, it help us distinguish objects came from the same class

print('<'+'='*130+'>')
print()
# inheritence could inherit the inherent class and add or change something to build a new class
# the inherent class is named parent(or superclass, base class) and the new class is named child(or subclass, derived class)

class Car():
	def exclaim(self): # self is a argument which is used to search the correct object's attribute and method.
		print("I'm a Car!")
	def say(self):
		print('hello!')
	pass
class Yugo(Car): # inherit from Car
	def say(self):
		print("hello! I'm Yogo!") # override the parent 
		pass
	def need_a_push(self): # add a new method
		print("A little help here!") 
	pass
give_me_a_car = Car()
give_me_a_yugo = Yugo() # child is a special case of parent, and give_me_a_yugo is a special case of Yugo but it also inherit from Car.

give_me_a_yugo.exclaim()
give_me_a_car.exclaim() 

give_me_a_car.say()
give_me_a_yugo.say()

try:
	give_me_a_car.need_a_push()
except AttributeError as err:
	print(err)
give_me_a_yugo.need_a_push()


print()
class Person():
	def __init__(self, name):
		self.name = name

class MDPerson(Person):
	def __init__(self, name):
		self.name = 'Doctor ' + name

class JDPerson(Person):
	def __init__(self, name):
		self.name = name + ", Esquire"

class EmailPerson(Person):
	def __init__(self, name, email):# it will override the parent, so it won't call parent;s method automatically. We need to use a spefic way to call it.
		super().__init__(name)
		# super() will get the defination of parent 'Person'
		#__init__() will call Person.__init__() method, it will passing self to the parent so we only need to pass othr arguments
		self.email = email

person = Person('Fudd')		
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(person.name, doctor.name, lawyer.name)
print(bob.name, bob.email)

print('<'+'='*130+'>')
print()
# what is 'self' 
class dog():
	def run(self): # self is a argument which is used to search the correct object's attribute and method.
		print("this dog ran away")

bulldog = dog()
bulldog.run() # python will do : (1) check the class of bulldog (2) take object bulldog as a self and pass it to the run() method of class dog 

