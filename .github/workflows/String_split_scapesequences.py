#SCAPE SEQUENCES TO SPLIT STRINGS
""" there are two \n for new line and \t for horizontal tab"""
#Exercise 1 , split by new line and store output in a list
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""
spring_storm_lines = spring_storm_text.split("\n")
print (spring_storm_lines)
"""Output to be ['The sky has given over ', 'its bitterness. ', 'Out of the dark change ', 'all day long ', 'rain falls and falls ', 'as if it would never end. ', 'Still the snow keeps ', 'its hold on the ground. ', 'But water, water ', 'from a thousand runnels! ', 'It collects swiftly, ', 'dappled with black ', 'cuts a way for itself ', 'through green ice in the gutters. ', 'Drop after drop it falls ', 'from the withered grass-stems ', 'of the overhanging embankment.']"""
