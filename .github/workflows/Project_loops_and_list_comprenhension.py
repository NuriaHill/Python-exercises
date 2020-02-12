#Project : Carly´s Clippers
#As a DA you need to calculate some metrics based on some data to plan out the business operation the rest of the month

#Starting Data

#names of the cuts offered
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
#price of each hairstyle
prices = [30, 25, 40, 20, 20, 35, 50, 35]
#number of hairstyle from hairstyles purchased last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#step 1 : create a total_price variable and set to 0
total_price = 0
#step 2 : Iterate through prices list and add the value to total_prices
for price in prices:
  total_price += price
  
#step 3 :After this loop we create variable for average price (Average = total/number of prices)
average_price = total_price/len(prices)
#Step 4 : print the average price
print("Average Haircut Price :" + str(average_price))
#Another way to print
print("Average Haircut Price : ${0}".format(average_price))
#output : Average Haircut Price : $31.875
#Step 5 too pricey, we want to cut by 5 dolars using a comprenhension list
new_prices =[price -5 for price in prices]
#Step 6 print new prices
print(new_prices)

#step 7 we want to know total revenue,first we create a variable	
total_revenue = 0

#step 8  for loop to know how many  hairstyles we have
for i in range(len(hairstyles)):
#step 9 We want to know the revenue of last week:
for i in range(len(hairstyles)):
  total_revenue += prices[i]*last_week[i]
#step 10 we print the total revenue:
print ("Total Revenue : "+ str(total_revenue))
#Step calculate daily total revenue:
average_daily_revenue = total_revenue/7
print (average_daily_revenue)

#step 12 we advertise the cheapers haircuts(under30)
cuts_under_30 =[hairstyles[i] for i in range(len(hairstyles)) if new_prices[i]<30]
#step 13 print cuts_under_30
print(cuts_under_30)
