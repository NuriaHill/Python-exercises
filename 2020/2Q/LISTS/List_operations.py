#LIST LENGTH
list1 = range(2, 20, 2)

list1_len = len(list1)
print(list1_len) #9

list1 = range(2, 20, 3)

list1_len = len(list1)
print(list1_len) #6


#SELECTING LIST ELEMENTS

employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']

index4 = employees[4]
print(index4)#Ryan

shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']

print(len(shopping_list))

last_element = shopping_list[-1]

element5 = shopping_list[5]

print(last_element)#cereal
print(element5)#cereal

#SLICING LISTS
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:2]

print (beginning)#['shirt', 'shirt']

middle = suitcase [2:4]

print(middle)#['pants', 'pants']

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start = suitcase[:3]
print (start) #['shirt', 'shirt', 'pants']
end = suitcase[-2:]
print (end)#['pajamas', 'books']


#COUNTING ELEMENTS
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')
print(jake_votes)

#SORTING LISTS
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print (addresses)#['10 Downing St.', '12 Grimmauld Place', '1600 Pennsylvania Ave', '221 B Baker St.', '42 Wallaby Way', '742 Evergreen Terrace']