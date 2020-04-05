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