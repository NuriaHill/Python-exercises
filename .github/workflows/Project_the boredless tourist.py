#PROJECT : THE BOREDLESS TOURIST
"""at The Boredless Tourist run a recommendation engine using Python. We first evaluate what a person’s interests are and then give them recommendations in their area to venues, restaurants, and historical destinations that we think they’ll be engaged by"""
#Step 1 Keep code version controlled using git
"""We start by running git init in the terminal"""
#Step 2 we are doing most of our coding in the document called script.py
"""to track script.py we add it to Git staging area with git add script.py"""
#Step 3 perform a commit with the message "initial commit"
""" git commit -m "initial commit"""
#step 4, create some data
"""Now let’s create some data that we’re going to use to test the functionality that we create for The Boredless Tourist."""
"""A list of destintations to use """
destinations = ["Paris, France", "Shangai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
#step 5 let´s define a test traveler
test_traveler = ['Erin Wilkes', 'Shangai, China', ['historical site', 'art']]
""" Erin is a test traveler, user of our application, that is in China right now and
likes historical sites and art"""
#Steps 6  and 7 save and commit the changes.
""" first we save the script then we do a git add script.py and finally
we do a git commit - m " Added test objects" """
#Steps 8, 9 and 10 Adding functionality
""" when a traveler arrives to a destination, we want to know where they are"""
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

#step 11 We test our function
print(get_destination_index("Los Angeles, USA")) 
#The result should be 2
#step 12  13 and 14, try different destinations to see the result
#step 15  and 16 define a function to get the traveler location. Assuming traveler data will be structured as in test_traveler
def get_traveler_location(traveler):
  traveler_destination = traveler [1]
#step 17 and 18 get the index of the traveler destination
def get_traveler_location(traveler):
  traveler_destination = traveler [1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index
#step 19- 21  : testing the result should be 1
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)
#Step 22  and 23 save your work in git
""" git add script.py and git commit -m "Added logic to find traveler destinations and convert to internal data" """"
#step 24 create a list of atractions, empty at first
attractions =[]
#step 25, we want attractions to be an empty list for each location 
attractions =[[], [], [], [], []]
#method 1 for loop to achieve the same result
attractions =[]
for destination in destinations:
  attractions.append([])
#method 2, list comprenhension
atractions =[[] for destinations in destinations]

#step 26 print attractions save and run code. result should be [[], [], [], [], []]
print (attractions) 
#step 27-30 add attractions, we ad a try block to our function to try to cach possible ValueErrors when passing it
def add_attraction(destination,attraction):
  try:
  destination_index = get_destination_index(destination)
  except ValueError:
    return 
	
#Step 31-34 , if the destination exist, we already have a list for in in attractions, our function will look like this
def add_attraction(destination,attraction):
  try:
    destination_index = get_destination_index(destination)
  except ValueError:
    return 
  attractions_for_destination = attractions[destination_index].append(attraction)
  return
add_attraction("Los Angeles, USA",['Venice Beach', ['beach']])
print (attractions)       
#Result [[], [], [['Venice Beach', ['beach']]], [], []]  
#step 35 let´s add more places
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#step 36-37 add and commit changes
""" git add script.py and git commit -m "Created attractions and functionality for adding new attractions" """
#steps 38-46 finding the best places to go
def find_attractions(destination,interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest=[]
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction)
  return attractions_with_interest
#steps 47-48 to test our function find_attractions
la_arts = find_attractions("Los Angeles, USA", ['art'])
print (la_arts)
#steps 47-48 test the find_attractions function
#result ['LACMA', ['art', 'museum']]

#Step 49, we don´t want to show th tags to our users
"""In the body of find_attractions(), find where you append possible_attraction to attractions_with_interest. Change this so you only append possible_attraction[0] which will only append the name."""
def find_attractions(destination,interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest=[]
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest
  
 #Step 50 test, result is now ['LACMA']
 #Steps 51-52 save and commit
 """ git add script.py and git commit -m "Added interest finder logic" """
 #Steps53-60 See parts of the city that you want to see and print an statement for the traveler
 def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination,traveler_interests)
  interest_string = "Hi " +traveler[0]+ ", we think you´ll like these places around " + traveler_destination +": " 
  for i in range(len(traveler_attractions)):
    if traveler_attractions[-1] == traveler_attractions[i]:interest_string += "the " + traveler_attractions[i]+"."
    else:
      interest_string +=  "the " + traveler_attractions[i] + ", "
  return interest_string

 #step 61-62 we test it with a traveler
 smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print (smills_france)
#result"Hi Dereck Smill, we think you'll like these places around Paris, France: the Arc de Triomphe"
#steps 63-64 save add and commit 
""" git add script.py and git commit -m ""Added function to generate message for traveler and present attractions they might be interested in." """
