#DICTIONARY CHALLENGE
#1.GET A KEY
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["earth"])
#returns : ['Taurus', 'Virgo', 'Capricorn']
print(zodiac_elements["fire"])
#returns: ['Aries', 'Leo', 'Sagittarius']

#2.CHECKING FOR KEY
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

key_to_check = "matcha"
try: 
  print(caffeine_level[key_to_check])
except KeyError:
  print("Unknown Caffeine Level")
#returns Unknown Caffeine Level
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level["matcha"]=30
key_to_check = "matcha"
try: 
  print(caffeine_level[key_to_check])
except KeyError:
  print("Unknown Caffeine Level")
#returns 30

#DICTONARY REVIEW
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread ={}
spread["past"]= tarot.pop(13)
spread["present"]= tarot.pop(22)
spread["future"] = tarot.pop(10)

for number,card in spread.items():
  print ("Your " + number +" is the " + card + " card." )
  
"""result : 
Your past is the Death card.
Your present is the The Fool card.
Your future is the Wheel of Fortune card"""