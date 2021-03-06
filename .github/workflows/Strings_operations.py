#STRINGS
#A string is a LIST of characters
my_name = "Nuria"
first_initial = my_name[0]
print(first_initial)
#The result of the avobe will be N

#STRING SLICING
"""you work for a company where each employee´s user name is generated by taing the 5 first letters of their last name.Temporary passwords are created slicing the last name too, from the third to the sitch letter"""

first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
temp_password = last_name[2:6]

print (new_account) #Villa
print(temp_password) #llan

"""We are going to improve the account generator, it will take two imputs: first_name and last_name"""
def account_generator(first_name,last_name):
  account_name = first_name[:3]+last_name[:3]
  return account_name
#We test our function out 
new_account = account_generator("Jullie","Blevins")
print (new_account)#Julble

"""We are going to improve the password generator, it will take two imputs: first_name and last_name"""
def password_generator(first_name,last_name):
  temp_password = first_name[len(first_name)-3:]+last_name[len(last_name)-3:]
  return temp_password
  
#We test our function out 
temp_password = password_generator("Reiko","Matsuki") 
print (temp_password) #ikouki
  

#NEGATIVE INDICES
#Find the second to last character on a given string
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2] 
print(second_to_last) #f

#Last four characters
final_word =  company_motto[-4:]
print(final_word)#life

#Changing Strings. 
first_name = "Bob"
last_name = "Daily"

first_name[0] = "R" #this will give us an error since stings are immutable

#To change Bob to Rob we need to do the following:
fixed_first_name = "R"+ first_name[1:]
print (fixed_first_name) #Rob

#ESCAPE CHARACTERS
#let´s fix the below
password = "theycallme"crazy"91" #This will throw a syntax error.
password = "theycallme\"crazy\"91" #We used \ to escape the " characters without terminating the string.
print(password)#theycallme"crazy"91

#ITERATING THROUGH STRINGS
#We write a function that will iterate through a string a give us its length
def get_length(string):
  counter = 0
  for i in string:
    counter+= 1
  return counter
 
#we test our function
print(get_length("Hello my name is Nuria"))#22

#STRINGS AND CONDITIONALS
#We want to check if a word contains a given letter

def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False #because we only have two options
#We test our function
print (letter_check("Murcielago", "u")) #True

#We want to check if a word contains a given letter in a more efficient way with in method.
def contains (big_string, little_string):
  if little_string in big_string:
    return True
  return False
 #Testing the function
 print(contains ("copycat", "cat")) #True
 
 #function that compares two sring and put the common letters in a new list
 def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not(letter in common):
      common.append(letter)
  return common
  #We test our function
  print (common_letters("house", "hello"))#['h', 'o', 'e']