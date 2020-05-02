#SCOPE EXAMPLE
def create_special_string(special_item):
    return "Our special is " + special_item + "."
	
print("I don't like " + special_item)#we will get a name error as we are trying to access special item outside the function

header_string = "Our special is " 

def create_special_string(special_item):
    return header_string + special_item + "."
print(create_special_string("grapes"))#Our special is grapes.


#EXAMPLE 2
def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age
 
 print(current_year)#NameError: name 'current_year' is not defined
 print(age)#NameError: name 'age' is not defined
 
 #now we defile current_year outside the function. It is globally defined.
 current_year = 2048

def calculate_age(birth_year):
  age = current_year - birth_year
  return age

print (current_year)#2048
print(calculate_age(1970))#78