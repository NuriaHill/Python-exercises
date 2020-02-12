#list comprehension user names
#first we have scraped a website and gotten a list of words:

words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
#We create a new list called usernames, we want there only words starting with @
#Method 1, standard for loop
words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
  if word[0] == '@':
    usernames.append(word)
#Method 2, list comprenhesion
usernames = [word for word in words if word[0] == '@']
print(usernames)
#Now we want to put a message to the users : 
messages = [user + " please follow me!" for user in usernames]
#the output will be 
#["@coolguy35 please follow me!", "@kewldawg54 please follow me!", "@matchamom please follow me!"]
