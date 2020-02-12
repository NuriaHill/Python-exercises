#get the squares from a list using a for loop
single_digits = range(10)
squares =[]

for digit in single_digits:
  print(digit)
  squares.append(digit**2)
  
#get the cubes using a comprenhension list 

cubes =[(digit**3) for digit in single_digits]
print(cubes)