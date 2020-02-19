#SPLIT + APPEND
"""Your boss at the Poetry organization sent over a bunch of author names that he wants you to prepare for importing into the database. Annoyingly, he sent them over as a long string with the names separated by commas."""
#STEP 1 Create a list called author names
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)

#STEP 2 Create another list called author_last_names that only contains the last names of the poets 
author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
  
print (author_last_names)