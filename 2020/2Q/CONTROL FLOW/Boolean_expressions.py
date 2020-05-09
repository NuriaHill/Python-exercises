#Boolean Variables

my_baby_bool = "true"
print(type(my_baby_bool))#<class 'str'>
my_baby_bool_two = True
print(type(my_baby_bool_two))#<class 'bool'>

#IF STATEMENTS
def dave_check(user_name):
  if user_name == "Dave":
    return "Get off my computer Dave!"

user_name = "Dave"

print(dave_check(user_name))#Get off my computer Dave!


def dave_check(user_name):
  if user_name == "Dave":
    return "Get off my computer Dave!"
  if user_name == "angela_catlady_87":
    return "I know it is you Dave! Go away!"
  
user_name = "angela_catlady_87"

print(dave_check(user_name))#I know it is you Dave! Go away!

#RELATIONAL OPERATORS
def greater_than (x, y):
  if x > y:
    return x
  if y > x :
    return y
  if x == y: 
    return "These numbers are the same"


def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"

print(graduation_reqs(120))#You have enough credits to graduate!