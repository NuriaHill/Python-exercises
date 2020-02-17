#LIST REVIEW
#STEP ONE Define a function to generate user name
"""The fucntion will have two parameters, first_name and last_name. 
If first_name is less than 3 characters and last_name is less than 4 characters, the user name generator will generate a user name with
 the result of the sum of the first and last name complete. 
If they are longer it will take a slice of the parameters to generate  the user name"""
def username_generator(first_name, last_name):
  if (len(first_name)<3) and (len(last_name)<4):
     username = first_name + last_name
  else:
      username = first_name[:3] + last_name[:4]
  return username
#Another way to do this 
  def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
 #We test our function
 print(username_generator("Abe", "Simpson"))#AbeSimp
 
 #STEP TWO define a function to generate password, dependant on username
 def password_generator(username):
  password =""
  
#STEP THREE Develop your password generator function , the temporary password should  shift all of the lettersof username to the right one by one

def password_generator(username):
  password = ""
  for i in range (0,len(username)):
    password += username[i-1]
  return password

#We test our function
print(password_generator(username_generator("Abe", "Simpson"))) #pAbeSim