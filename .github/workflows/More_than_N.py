#We create a function called more than N.
#This fuction should return true if an item appears more than n times

def more_than_n(lst,item,n):
  if lst.count(item)>n:
    return True
  else:
    return False

#To test our function: 
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))