#ADVANCE LIST OPERATIONS

#1 ITERATING WITH LOOPS

dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
    print(breed) 
	
	
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
  print(game)

for sport in sport_games:
  print(sport)
  
  
 #USING RANGE TO ITERATE
 
 promise = "I will not chew gum in class"

for i in range (5):
  print(promise)#will print promise 5 times
  
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
  print(student)