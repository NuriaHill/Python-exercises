#JOINING STRINGS 
""" we use the method .join() the syntax is "delimiter".join(list)"""
#Exercise 1
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = " ".join(reapers_line_one_words)
print (reapers_line_one)

"""the ouput will be the following string: Black reapers with the sound of steel on stones"""

#Exervise 2 join a list using new line as delimiter
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = "\n".join(winter_trees_lines)
print (winter_trees_full)

"""the output will be : 
All the complicated details
of the attiring and
the disattiring are completed!
A liquid moon
moves gently among
the long branches.
Thus having prepared their buds
against a sure winter
the wise trees
stand sleeping in the cold."""

