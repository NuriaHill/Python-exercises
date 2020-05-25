Python_challenge_games of chance
import random #We import the randome module

money = 100 #This is our starting money

def coin_flip(guess, bet):  
  #Will randomly get 1 or 2. Will associate 1 to heads and 2 to tails.
  flip = random.randint(1,2)
    if flip == 1: 
    print("The coin toss result was heads")
  if flip == 2: 
    print("The coin toss result was tails")
  if (flip==1) and (guess.lower()== "heads"):
    print("Your guess is right! You won "+ str(bet) + " Euros")
    return +bet 
  elif (flip==2) and (guess.lower()== "tails"):
    print("Your guess is right! You won "+ str(bet) + " Euros")
    return +bet 
  else :
    print ("Sorry, try again, you lost " + str(bet) + " Euros")
    return -bet

coin_flip ("heads", 50)


def chohan (guess, bet):
  #We calculate a random number between 1 and 6 twice and sum the result.
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  result = dice1 + dice2
  print(result)
  if (result%2 == 0 and guess.lower() == "even"):
    print("your guess is even and you got it right, you won "+ str(bet) + " Euros")
    return +bet
  if (result%2 != 0 and guess.lower() == "odd"):
    print("your guess is odd and you got it right, you won "+ str(bet) + " Euros")
    return +bet
  else:
    print("Sorry, your guess is wrong, you lost " + str(bet)+ " Euros")
    return -bet
  

chohan ("odd" , 50)

def higher_card(bet):
  #Makes sure your bet is higher than 0
  if bet <= 0 : 
    print ("Your bet should be above 0.")
    return 0
  player1 = random.randint(1,10)
  player2  = random.randint(1,10)
  print ("Your card is "+ str(player1))
  print ("their card is " + str(player2))
  if player1 > player2: 
    print ("You won " + str(bet)+ " euros!")
    return bet
  if player1 < player2:
    print ("You lost " + str(bet)+ " euros!")
    return -bet
  else :
    print ("It was a tie!")
    return 0

higher_card(20)
	