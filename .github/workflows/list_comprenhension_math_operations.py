#list comprenhension and math operations

celsius = [0, 10, 15, 32, -5, 27, 3]
#to convert the above list into farenheit we need to use a formula
#Formula F= C*9/5 +32

fahrenheit =[(celsius_value*9/5)+ 32 for celsius_value in celsius]
print(fahrenheit)

#result [32.0, 50.0, 59.0, 89.6, 23.0, 80.6, 37.4]