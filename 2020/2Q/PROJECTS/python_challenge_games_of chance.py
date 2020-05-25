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

def roulette(guess, bet):
  if bet <= 0 : 
    print ("Your bet should be above 0.")
    return 0
    #A standard roulette wheel has the numbers 0 through 36 as well as 00. We'll use 37 to represent 00.
  result = random.randint(0,37)
  if result == 37: 
    print ("The wheel landed on 00")
  else: 
    print ("the wheel landed on "+ str(result))
    #Checks to see if we guessed Even and the result was even. If the result was 0, the player shouldn't win
  if guess == "Even" and result % 2 == 0 and result != 0:
    print (str(result) + " is an even number.")
    print ("You won "+ str(bet)+ " Euros!")
    return bet
      #Checks to see if we guessed Odd and the result was odd. If the result was 37, the player shouldn't win, since that's what we are using to represent 00.
  if guess == "Odd" and result % 2 == 1 and result != 37:
    print (str(result) + " is an odd number.")
    print ("You won "+ str(bet)+ " Euros!")
    return bet  
    # If you guessed a number and the result was that number, you should win 35 times the amount they bet
  elif guess == result:
    print ("You guessed "+ str(guess)+ " and the result was "+ str(result))
    print ("You won "+ str(bet) + " Euros!")
    return bet * 35
      # If none of the above are true, you lost.
  else: 
    print ("You lost " + str(bet)+ " Euros!")
    return -bet 

roulette ("Even", 10)

money += coin_flip("Heads", 10)
money += higher_card(5)
money += chohan("Even", 2)
money += roulette("Even", 10)
money += roulette(3, 1)
money += roulette("Odd", 10)
print("Your total amount of money is " + str(money))

	