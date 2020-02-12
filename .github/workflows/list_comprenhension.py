#list comprenhension
#this is a python shorthand that combines for loop and list 
#In this exercise we have a list of heights but only those above 161 can ride the coaster.

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster =[height for height in heights if height >161]

print(can_ride_coaster)