#MODULES INTRODUCTION
#importing datetime from module datetime
from datetime import datetime
current_time = datetime.now()
print(current_time)
#result : 2020-02-25 08:52:54.051234

#random : allows you to generate numbers or select items at random
# Import random below:
import random

# Create random_list below:
random_list =[]

# Create randomer_number below:
random_list = [random.randint(1,100) for i in range(101)]
randomer_number = random.choice(random_list)
# Print randomer_number below:
print (randomer_number)