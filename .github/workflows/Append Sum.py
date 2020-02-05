#This function appends the last 2 elements sum to a given list three times.


def append_sum(lst):
  lst.append(lst[-1]+ lst[-2])
  lst.append(lst[-1]+ lst[-2])
  lst.append(lst[-1]+ lst[-2])
  return lst
  
  #We test our result as follows:
  print(append_sum([1, 1, 2]))