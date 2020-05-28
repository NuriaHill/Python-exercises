def shipping_cost_ground(weight):
	
	if weight <= 2:
		price_per_pound = 1.50
	elif weight <= 6:
		price_per_pound = 3.00
	elif weight <= 10:
		price_per_pound = 4.00
	else : 
		price_per_pound = 4.75
	
	return 20 + (price_per_pound * weight) #this option has a flat rate of 20 that we need to add to final price
	
print(shipping_cost_ground(8.4)) #result should be 53.6

shipping_cost_premium = 125.00 #This is a variable as the price does not depend on weight , it is a fixed price

def shipping_cost_drone(weight):
	
	if weight <= 2:
		price_per_pound = 4.50
	elif weight <= 6:
		price_per_pound = 9.00
	elif weight <= 10:
		price_per_pound = 12.00
	else : 
		price_per_pound = 14.25
	
	return  price_per_pound * weight #drone shipping has no flat rate
	
print(shipping_cost_drone(1.5)) #result should be 6.75

def print_cheapest_shipping_method(weight):

	ground = shipping_cost_ground(weight)
	premium = shipping_cost_premium
	drone = shipping_cost_drone(weight)
	
	if ground < premium and ground < drone:
		method = "standard ground"
		cost = ground 
		
	elif premium < ground and premium < drone:
		method = "premium ground"
		cost = premium
	else: 
		method = "drone"
		cost = drone

	print(
		"The cheapest option available is $%.2f with %s shipping."  #this print statement will replace $% with a paramenter either cost of method in that order
		% (cost, method)
		) 

print_cheapest_shipping_method(4.8)#The cheapest option available is $34.40 with standard ground shipping.
print_cheapest_shipping_method(41.5)#The cheapest option available is $125.00 with premium ground shipping.