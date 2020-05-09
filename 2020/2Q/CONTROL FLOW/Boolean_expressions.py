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


#Two conditionals

def graduation_reqs(gpa, credits):
  if gpa >= 2.0 and  credits >= 120:
    return "You meet the requirements to graduate!"

print(graduation_reqs(2.0, 120))#You meet the requirements to graduate!


def graduation_mailer(gpa,credits):
  if credits >= 120 or gpa >=2.0:
    return True
	
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and  (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if not (gpa >= 2.0) and not (credits >= 120):
    return "You do not meet either requirement to graduate!"