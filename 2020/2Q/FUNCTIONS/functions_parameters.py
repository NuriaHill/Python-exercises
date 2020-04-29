#PYTHON FUNCTION PARAMETERS
def greet_customer(special_item):
    print("Welcome to Engrossing Grocers.")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")
	
greet_customer("peanut butter")
"""Welcome to Engrossing Grocers.
Our special is peanut butter.
Have fun shopping!"""

def mult_two_add_three(): #function without a parameter
  number = 5
  print(number*2 + 3)

mult_two_add_three() #13

def mult_two_add_three(number): #fucntion with parameter number
  print(number*2 + 3)
  
mult_two_add_three(1) #5


def greet_customer(grocery_store, special_item): #function with two parameters
    print("Welcome to "+ grocery_store + ".")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")

greet_customer("Stu's Staples", "papayas") 
"""Welcome to Stu's Staples.
Our special is papayas.
Have fun shopping!"""


def mult_x_add_y(number, x, y):
  print(number*x + y)
  
mult_x_add_y(5, 2, 3)#13
mult_x_add_y(1, 3, 1)#4

#KEYWORD ARGUMENTS ( not dependant of position in the function)

def greet_customer(grocery_store, special_item):
    print("Welcome to "+ grocery_store + ".")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")
	
greet_customer(special_item="chips and salsa", grocery_store="Stu's Staples")

"""Welcome to Stu's Staples.
Our special is chips and salsa.
Have fun shopping!"""

#DEFAULT ARGUMENTS 

def greet_customer(special_item, grocery_store="Engrossing Grocers"): #default arguments are used during function definition 
    print("Welcome to "+ grocery_store + ".")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")
	
greet_customer("bananas")

"""Welcome to Engrossing Grocers.
Our special is bananas.
Have fun shopping!"""

#KEYWORD ARGUMENTS 
"""once you give an argument a default value you make it a keyword argument"""

def greet_customer(special_item="bananas", grocery_store): # this is not valid

def greet_customer(special_item, grocery_store="Engrossing Grocers"): # this is valid

#keyword arguments defined at the time of defining the function

def create_spreadsheet(title): #no keywords arguments
  print("Creating a spreadsheet called "+title)
  
create_spreadsheet("Downloads") #prints:  Creating a spreadsheet called Downloads

def create_spreadsheet(title,row_count = 1000):#with a keyword row_count
  print("Creating a spreadsheet called "+title + " with "+ str(row_count) + " rows")
create_spreadsheet("Downloads") #prints Creating a spreadsheet called Downloads with 1000 rows


def create_spreadsheet(title = "Applications ",row_count = 10): #with two keywords
  print("Creating a spreadsheet called "+title + " with "+ str(row_count) + " rows")
create_spreadsheet() #prints Creating a spreadsheet called Applications  with 10 rows