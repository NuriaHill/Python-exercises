def remove_middle(lst,start,end):
  #first half from 0 to start will not include index at start.
  first_half = lst [:start]
  #second half will be from end +1 so it will not take last index 
  second_half = lst [end+1:]
  return first_half + second_half 
  

#to check the function
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#Optimized code:
def remove_middle(lst,start,end):
	new_list = lst[:start]+ lst[end+1:]
	return new_list
	
#Even more optimized : 
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]