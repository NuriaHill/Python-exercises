#double index
"""This function should return a list except for the element at index
that should be doubled. If the index is not a valid index(out of range, 
the function should return the original list"""
def double_index(lst,index):
  if index >= len(lst):
    return lst
  else: 
    new_lst = lst[0:index]
    new_lst.append(lst[index]*2)
    new_lst = new_lst + lst [index+1:]
    return new_lst
	
#to test the function
print(double_index([3, 8, -10, 12], 2))
#Result [3, 8, -20, 12]

#Remove Middle
""" Function with 3 parameters, should return a list where the start index
and the end index of a given list have been removed."""
def remove_middle (lst,start,end):
  new_list = lst[:start] + lst[end+1:]
  return new_list
#to test the function
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
#results [4, 23, 42]

#More Than N
""" function that has 3 parameters , function should return true if item appears in the list 
more than n times.False otherwise"""
def more_than_n (lst,item,n):
  if lst.count(item)>n:
    return True
  else:
    return False
#To check results: 
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
#result True

#More Frequent Item
"""Function with 3 parameters.return item1 or item2 depending on which
item appears more often in a list.If ocurrency is the same for both items, return item1"""
def more_frequent_item(lst,item1,item2):
  if lst.count(item1) >  lst.count(item2):
    return item1
  if lst.count(item2) >  lst.count(item1):
    return item2
  else:
    return item1
#To check results:
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
#result 3

#Middle Item
"""One function with one parameter.If there are an odd number of elements in a list,
the function should return the middle element. If there is an even number,the function
should return the average of the middle two elements"""
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] +lst[int(len(lst)/2)-1]
    return sum/2
  else :
    return lst[int(len(lst)/2)]
#To test our function 
print(middle_element([5, 2, -10, -4, 4, 5]))
#result : -7.0

#Append Sum
"""Funtion with one parameter, should add the last 2 elements of list together and
append the result to the list. It should do this 3 times"""
def append_sum(lst):
  lst.append(lst[-1]+lst[-2])
  lst.append(lst[-1]+lst[-2])
  lst.append(lst[-1]+lst[-2])
  return lst 
#To check the result
print(append_sum([1, 1, 2]))
#result [1, 1, 2, 3, 5, 8]

#Lager List
""" A function, 2 parameters.Should return the last element of a list that 
contains more elements, if both lists are the same size it should return the last element
of list 1"""
def larger_list(lst1,lst2):
  if len(lst1)>= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]
#to test the result 
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
#result is 5
print(larger_list([4, 10, 2, 5,-10], [-10, 2, 5, 10]))
#result is -10

#Combine Sort
"""One function, 2 parameters. The function should combine 2 list into a new one
and sort the result"""
#Using sorted method
def combine_sort(lst1,lst2):
  unsorted = lst1 + lst2
  lst3 = sorted(unsorted)
  return lst3
# to check result 
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
#result [-10, 2, 2, 4, 5, 5, 10, 10]
#Using sort method
def combine_sort(lst1,lst2):
  lst3 = lst1 + lst2
  lst3.sort()
  return lst3
# to check result 
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
#result [-10, 2, 2, 4, 5, 5, 10, 10]

#Append Size
""" One function, one parameter. Functions should append the size of a given list
and then return this new list"""
def append_size(lst):
  lst.append(len(lst))
  return lst
#to check result 
print(append_size([23, 42, 108]))
#Result [23, 42, 108, 3]

#Every Three Nums
"""One function, one parameter. Function should return a list of every 3 numbers between a given start and 100. If Start 
is greater than 100, it should return an empty list"""	
def every_three_nums(start):
  if start > 100:
    empty_list=[]
    return empty_list
  else:
    lst = list(range(start,101,3))
    return lst
#to check result 
print(every_three_nums(91))
#solution [91, 94, 97, 100]
