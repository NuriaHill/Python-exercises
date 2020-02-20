#STRINGS STRIP METHOD
"""This method is used to clean strings and we can also use an element"""
#Exercise 1 remove the whitespaces

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

#Step one, iterate throgh the list and save the result in new list

love_maybe_lines_stripped =[]

for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
  
#Step two, join the lines of love_maybe_lines_stripped in a new list
love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_full )
""" The ouput will be Always
in the middle of our bloodiest battles
you lay down your arms
like flowering mines

to conquer me home."""
