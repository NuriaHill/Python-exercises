def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
    new_lst = lst[0:index]
    new_lst.append(lst[index]*2)
    new_lst = new_lst + lst[index+1:]
    return new_lst


print(double_index([3, 8, -10, 12], 2))
#This function returns a new list with the value of index we indicate, doubled