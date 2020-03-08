#TEMPERATURE SENSOR DICTIONARY
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
print(sensors)
#returns {'living room': 21, 'kitchen': 23, 'bedroom': 20, 'pantry': 22}

#TRANSLATIONS DICTIONARY English-sindarin
translations ={"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

#FAMILY DICTIONARY 
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

#ANIMALS IN ZOO WITH ADDITION DICTIONARY
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)
#returns {'zebras': 8, 'monkeys': 12, 'dinosaurs': 0}

#USERS DICTIONARY UPDATE
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)
#result {'teraCoder': 9018293, 'proProgrammer': 119238, 'theLooper': 138475, 'stringQueen': 85739}

#OSCAR WINNERS DICTIONARY ADD and OVERWRITE
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"
print (oscar_winners)
#Result {'Best Picture': 'Moonlight', 'Best Actor': 'Casey Affleck', 'Best Actress': 'Emma Stone', 'Animated Feature': 'Zootopia', 'Supporting Actress': 'Viola Davis'}

#LISC COMPRENHENSION TO DICTIONARY
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)
#Result {'espresso': 64, 'chai': 40, 'decaf': 0, 'drip': 120}

#REVIEW
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
zipped_songs = zip(songs,playcounts)
plays ={key:value for key, value in zipped_songs}
print(plays)
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
zipped_songs = zip(songs,playcounts)
plays ={key:value for key, value in zipped_songs}
print(plays)
plays["Purple Haze"] = 1
plays["Respect"] = 94
library ={"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
"""Result : 
{'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44, "What's Going On": 21, 'Respect': 89, 'Good Vibrations': 5}
{'The Best Songs': {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44, "What's Going On": 21, 'Respect': 94, 'Good Vibrations': 5, 'Purple Haze': 1}, 'Sunday Feelings': {}}"""

#GET METHOD
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id  = user_ids.get("teraCoder", 100000)
print(tc_id)
#Returns 100019
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)
#Returns 100000

#KEY DELECTION- POP METHOD
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
health_points = health_points + available_items.pop("stamina grains", 0)
health_points = health_points + available_items.pop("power stew", 0)
health_points = health_points + available_items.pop("mystic bread", 0)
print(available_items)
print(health_points)
#Returns {'health potion': 10, 'cake of the cure': 5, 'green elixir': 20, 'strength sandwich': 25} and 65

#KEY METHOD
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()
print(users) #returns dict_keys(['teraCoder', 'pythonGuy', 'samTheJavaMaam', 'lyleLoop', 'keysmithKeith'])
print(lessons)#returns dict_keys(['functions', 'syntax', 'control flow', 'loops', 'lists', 'classes', 'dictionaries'])