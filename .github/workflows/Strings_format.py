#STRING METHOD FORMAT
"""This method takes variables as an argument and includes them in the string that it is run on. You include {} marks as placeholders for where those variables will be imported."""
#Exercise 1
def poem_title_card (poet,title):
  return "The poem \"{}\" is written by {}.".format (title,poet)

print(poem_title_card("Walt Whitman", "I Hear America Singing"))

#Exercise 2 using keywords

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date =publishing_date, author= author, title = title, original_work = original_work)
  return poem_desc

#We test the above 
my_beard_description =  poem_description(
author = "Shel Silverstein" ,
title = "My Beard" ,
original_work = "Where the Sidewalk Ends" ,
publishing_date = "1974"  
)
print (my_beard_description)
""" The result will be The poem My Beard by Shel Silverstein was originally published in Where the Sidewalk Ends in 1974."""