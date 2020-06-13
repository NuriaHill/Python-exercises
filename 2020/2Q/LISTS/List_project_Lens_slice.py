#Len´s sice 

toppings =[
  'pepperoni',
  'pineapple',
  'cheese',
  'sausage',
  'olives',
  'anchovies',
  'mushrooms'
]

prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)

print ("We sell " + str(num_pizzas) + " different kinds of pizza!") #We sell 7 different kinds of pizza!

pizzas = list(zip(prices,toppings))
print(pizzas)#[(2, 'pepperoni'), (6, 'pineapple'), (1, 'cheese'), (3, 'sausage'), (2, 'olives'), (7, 'anchovies'), (2, 'mushrooms')]

pizzas.sort()

print (pizzas)#[(1, 'cheese'), (2, 'mushrooms'), (2, 'olives'), (2, 'pepperoni'), (3, 'sausage'), (6, 'pineapple'), (7, 'anchovies')]

cheapest_pizza = pizzas[0]
print(cheapest_pizza)#(1, 'cheese')
priciest_pizza = pizzas[-1]
print(priciest_pizza)#(7, 'anchovies')
three_cheapest = pizzas[:3]

print(three_cheapest)#[(1, 'cheese'), (2, 'mushrooms'), (2, 'olives')]
num_two_dollar_slices = prices.count(2)

print(num_two_dollar_slices)#3