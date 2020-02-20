#STRING METHOD FORMAT
"""This method takes variables as an argument and includes them in the string that it is run on. You include {} marks as placeholders for where those variables will be imported."""
def poem_title_card (poet,title):
  return "The poem \"{}\" is written by {}.".format (title,poet)

print(poem_title_card("Walt Whitman", "I Hear America Singing"))