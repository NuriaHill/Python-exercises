def every_three_nums(start):
  if start >100:
    empty_list = []
    return empty_list
  else:
    lst = list(range (start,101,3))
    return lst

#we check our code with the following expressions
print(every_three_nums(91))
print(every_three_nums(103))
