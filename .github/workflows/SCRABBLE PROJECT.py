#PROJECT SCRABBLE
"""We have provided you with two lists, letters and points. We would like to combine these two into a dictionary that would map a letter to its point value.

Using a list comprehension and zip, create a dictionary called letter_to_points that has the elements of letters as the keys and the elements of points as the values."""
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

zipped_letters = zip(letters,points)
letter_to_points ={key:value for key, value in zipped_letters}
#print (letter_to_points)

letter_to_points.update({" ": 0})
print (letter_to_points)

def score_word(word):
  point_total = 0
  for word in word : 
    point_total += letter_to_points.get(word, 0)
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words ={"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"],"Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points ={}

def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words :
      player_points += score_word(word)
    player_to_points[player]= player_points
  
update_point_totals()  
print (player_to_points)