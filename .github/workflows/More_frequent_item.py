#This function returns the most frequent item
def more_frequent_item(lst,item1,item2):
  if lst.count(item1)>lst.count(item2):
    return item1
  if lst.count(item2)>lst.count(item1):
    return item2
  else :
    return item1
#To check if our function works:
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))