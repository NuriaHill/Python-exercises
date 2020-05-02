#FUNCTIONS RETURN
""" return is used to store the result of a function ina variable"""
def divide_by_four(input_number):
    return input_number/4

result = divide_by_four(16) #4
print("16 divided by 4 is " + str(result) + "!") #16 divided by 4 is 4!
result2 = divide_by_four(result)
print(str(result) + " divided by 4 is " + str(result2) + "!")#4 divided by 4 is 1!


def create_special_string(special_item):
    return "Our special is " + special_item + "."

special_string = create_special_string("banana yogurt")

print(special_string) #Our special is banana yogurt.

def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age

my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)
print ("I am "+ str(my_age)+ " years old  and my dad is "+  str(dads_age)+ " years old") #I am 56 years old  and my dad is 96 years old

#MULTIPLE RETURN VALUES
"""We can return several values by separating them with a coma"""

def square_point(x_value, y_value):
  x_2 = x_value * x_value
  y_2 = y_value * y_value
  return x_2, y_2
  
x_squared, y_squared = square_point(1, 3)
print(x_squared) #1
print(y_squared) #9

def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = margin + target 
  return low_limit , high_limit

low , high =  get_boundaries(100, 20)
print(low)#80
print(high)#120
