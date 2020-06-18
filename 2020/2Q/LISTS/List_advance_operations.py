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
  
#BREAK

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog in dog_breeds_available_for_adoption:
  print(dog)
  if dog == dog_breed_I_want:
    print("They have the dog I want!")
    break

#CONTINUE

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages: 
  if age < 21:
    continue
  print(age)#38 34 26 21 67 41  
  
  
#WHILE LOOPS

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6: 
  students_in_poetry.append(all_students.pop())


print(students_in_poetry)#['Loki', 'Arius', 'Obie', 'Alexa', 'Minerva', 'Dora']

  