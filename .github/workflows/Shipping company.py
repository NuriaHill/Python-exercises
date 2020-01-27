def cost_ground_shipping(weight):
  if weight <= 2:
    cost = weight * 1.50 + 20.00
  elif weight <= 6:
    cost = weight * 3.00 + 20.00
  elif weight <= 10:
    cost = weight * 4.00 + 20.00
  else : 
    cost = weight * 4.75 + 20.00
  return cost
    
print (cost_ground_shipping(8.4))

cost_premium_ground_shipping = 125.00

def cost_drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.50 + 0.00
  elif weight <= 6:
    cost = weight * 9.00 + 0.00
  elif weight <= 10:
    cost = weight * 12.00 + 0.00
  else : 
    cost = weight * 14.25 + 0.00
  return cost
print (cost_drone_shipping(1.5))

def best_method(weight):
  if (cost_premium_ground_shipping < cost_ground_shipping(weight)) and (cost_premium_ground_shipping < cost_drone_shipping(weight)):
    return " You should ship using premium ground shipping, it will cost you " + "$" +str(cost_premium_ground_shipping)
  elif (cost_ground_shipping(weight) < cost_premium_ground_shipping) and (cost_ground_shipping(weight)<cost_drone_shipping(weight)):
    return " You should ship using  ground shipping, it will cost you " + "$" +str(cost_ground_shipping(weight))

  else :
    return " You should ship using  drone shipping, it will cost you " + "$" +str(cost_drone_shipping(weight))
  
print (best_method(4.8))
  
  

