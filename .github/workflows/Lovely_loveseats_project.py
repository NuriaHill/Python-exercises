#PYTHON PROJECT LOVELY LOVESEATS
""" review of python syntax and variables and mathematical operations with python"""
#Task 1 Adding the catalog
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""
#Task 2 adding price to the lovely_loveseat
lovely_loveseat_price = 254.00
#Task 3 inventory extention
stylish_settee_description ="""Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""
#Task 4 add price to the new item
stylish_settee_price = 180.50
#Task 5 add a new item
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""
#Task 6 set the new item price
luxurious_lamp_price = 52.15
#Task 7 calculate sales tax
sales_tax = .088 #this is 8.8%
#Task 8 first customer 
customer_one_total = 0
# Task 9 first customer items bought 
customer_one_itemization = ""
#Task 10 customer buys love seat
customer_one_total += lovely_loveseat_price
#Task 11 add the item description
customer_one_itemization += lovely_loveseat_description
#Task 12  and 13 add another item
customer_one_total +=luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description 
#Task 14 checkout
customer_one_tax = customer_one_total * sales_tax
#Task 15 add tax to total
customer_one_total += customer_one_tax
#Full code
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""
lovely_loveseat_price = 254.00

stylish_settee_description ="""Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""
stylish_settee_price = 180.50

luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""
luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0
customer_one_itemization = ""
#print (customer_one_total )
#print (customer_one_itemization)

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
#print (customer_one_total )
#print (customer_one_itemization)

customer_one_total +=luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description 
#print (customer_one_total )
#print (customer_one_itemization)
customer_one_tax = customer_one_total * sales_tax
#print (customer_one_tax)

customer_one_total += customer_one_tax
#print (customer_one_total)

print ("Customer One Items:")
print (customer_one_itemization)
print ("Customer One Total:")
print (customer_one_total)

"""The result should be Customer One Items:
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
Customer One Total:
333.09119999999996"""