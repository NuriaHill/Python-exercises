#PYTHON CLASSES
class Facade:
  pass
#class instanciating
facade_1 = Facade()#this makes Facade an object

facade_1_type = type(facade_1)#this makes the object a class
print(facade_1_type)

#class variables
class Grade :
  minimum_passing = 65
  
#METHODS
 class Rules : 
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."


class Circle:
  pi = 3.14
  
  def area(self, radius):
    return Circle.pi * radius ** 2
  
circle = Circle()
pizza_area = circle.area(6)
teaching_table_area = circle.area(18)
round_room_area = circle.area(5730)

print(pizza_area)#113.04
print(teaching_table_area)#1017.36
print(round_room_area) #103095306.0

#CONSTRUCTORS
#dundermethods(double underscore)
#__init__
class Shouter:
  def __init__(self):
    print("HELLO?!")
shout1 = Shouter()
# prints "HELLO?!"
shout2 = Shouter()
# prints "HELLO?!"
class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:
	# then shout it out
      print(phrase.upper())

shout1 = Shouter("shout")
# prints "SHOUT"

shout2 = Shouter("shout")
# prints "SHOUT"

shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"

class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))
    
teaching_table = Circle(36)

#INSTANCE VARIABLES
fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"

# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# prints "This works! This too!"

class Store:
  pass

alternative_rocks = Store() #this is an object for class Store
isabelles_ices = Store() #this is another object for class Store
alternative_rocks.store_name = "Alternative Rocks" #this object has an atribute that is store_name
isabelles_ices.store_name = "Isabelle's Ices" #this object has an atribute that is store_name

how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element, "count"):
    print(element.count("s")) #returns 5 and 2
	
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter/2
  def circumference (self):
    return 2 *self.pi *self.radius
    
    
    
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference()) #37.68
print(teaching_table.circumference())#113.04
print(round_room.circumference())#35984.4

#HOW TO GET A LIST OF ATRIBUTES-DIR
dir(5)
print (dir(5))
"""result is ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']"""

def this_function_is_an_object(self):
  pass
print(dir(this_function_is_an_object))
""" result is ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']"""

#DUNDER METHOD __repr__
class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
    return "Circle with radius {radius}".format(radius = self.radius)
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)
print(medium_pizza)
print(teaching_table)
print(round_room)