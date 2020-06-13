#LEN
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
inventory_len = len(inventory)
print (inventory_len)#19

#Select an element

first = inventory[0]
print(first)#twin bed

last = inventory[-1]
print(last)#pillow

inventory_2_6 = inventory[2:6]
print (inventory_2_6)#['headboard', 'queen bed', 'king bed', 'dresser']

#Slicing

first_3 = inventory[:3]
print(first_3)#['twin bed', 'twin bed', 'headboard']

#Count
twin_beds = inventory.count('twin bed')
print(twin_beds)#4

#Sort

inventory.sort()
print(inventory)
['dresser', 'dresser', 'headboard', 'king bed', 'king bed', 'king bed', 'nightstand', 'nightstand', 'pillow', 'pillow', 'queen bed', 'sheets', 'sheets', 'table', 'table', 'twin bed', 'twin bed', 'twin bed', 'twin bed']