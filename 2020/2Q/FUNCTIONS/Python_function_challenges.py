#1 TENTH POWER
def tenth_power(num):
  return num**10
  print(tenth_power(1))#1
  print(tenth_power(0))#0
  print(tenth_power(2))#1024
  
#2. SQUARE ROOTH
def square_root(num):
  num = num **0.5
  return num 
print(int(square_root(16)))
# should print 4
print(int(square_root(100)))
# should print 10

#3. WIN PERCENTAGE
def win_percentage(wins, loses):
  total = (wins + loses)
  percentage_total  = (wins/total)*100
  return percentage_total

print(int(win_percentage(5, 5)))
# should print 50
print(int(win_percentage(10, 0)))
# should print 100

#4. AVERAGE
def average(num1, num2):
  average = (num1 + num2)/2
  return int(average)
  
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

#5. REMAINDER
def remainder(num1, num2):
  remainder = (num1*2)%(num2/2)
  return int(remainder)
  
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0