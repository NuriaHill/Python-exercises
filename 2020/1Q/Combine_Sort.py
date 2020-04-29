#this function combines two list and return the result sorted
#Using sorted
def combine_sort(lst1,lst2):
  unsorted = lst1 + lst2
  lst3= sorted(unsorted)
  return lst3

#to check on the function 
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#using sort
def combine_sort(lst1,lst2):
  lst3 = lst1 + lst2
  lst3.sort()
  return lst3
#to check on the function 
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
