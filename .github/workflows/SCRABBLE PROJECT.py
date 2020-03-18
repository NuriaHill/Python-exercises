#PROJECT SCRABBLE
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters += [letter.lower() for letter in letters] #This is to include all the lowercase version of letters
points *= 2 #this is to add points to each lowercase version

zipped_letters = zip(letters,points)
letter_to_points ={key:value for key, value in zipped_letters}
#print (letter_to_points)

letter_to_points.update({" ": 0})
print (letter_to_points)
"""Result dictionary should look like this :
{'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 4, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, ' ': 0}"""


def score_word(word):
  point_total = 0
  for word in word : 
    point_total += letter_to_points.get(word, 0)
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points) #Result is 15

player_to_words ={"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"],"Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points ={}

def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words :
      player_points += score_word(word)
    player_to_points[player]= player_points
  
update_point_totals()  
print (player_to_points) #Result is {'player1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}
  
def play_word(player,word):
  player_to_words[player].append(word)

play_word("player1", "CODE")
print (player_to_words) #Result is {'player1': ['BLUE', 'TENNIS', 'EXIT', 'CODE'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}
  
  