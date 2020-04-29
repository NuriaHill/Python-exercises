#This function appends a given list size and returns the new list
def append_size(lst):
  lst.append(len(lst))
  return lst

#to try our function
print(append_size([23, 42, 108]))
