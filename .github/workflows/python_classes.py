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