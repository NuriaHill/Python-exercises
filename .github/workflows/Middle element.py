#this function gives us the middle element
#it should return the average of the middle two elements if there is an odd number
#it should return the middle element is there is an odd number of elements in the list
def middle_element(lst):
#to know if the lenght is odd number or not, we use module.
  if len(lst)%2 == 0: 
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) -1]
    return sum /2
  else:
    return lst[int(len(lst)/2)]

#we test our function with the following : 
print(middle_element([5, 2, -10, -4, 4, 5]))