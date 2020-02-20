#STRING METHODS REVIEW
"""Parse the string into something that can display the name, title, and publication date of the highlighted poems """
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#STEP 1 print the string

print(highlighted_poems)

"""Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"""

#STEP 2 we start by splitting the string by the commas

highlighted_poems_list = highlighted_poems.split(",")

#STEP 3 print highlighted_poems_list
print(highlighted_poems_list)
"""['Afterimages:Audre Lorde:1997', '  The Shadow:William Carlos Williams:1915', ' Ecstasy:Gabriela Mistral:1925', '   Georgia Dusk:Jean Toomer:1923', '   Parting Before Daybreak:An Qi:2014', ' The Untold Want:Walt Whitman:1871', " Mr. Grumpledump's Song:Shel Silverstein:2004", ' Angel Sound Mexico City:Carmen Boullosa:2013', ' In Love:Kamala Suraiyya:1965', ' Dream Variations:Langston Hughes:1994', ' Dreamwood:Adrienne Rich:1987']"""

#STEP 4 clear the whitspaces

highlighted_poems_stripped =[]
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
  
#STEP 5 print highlighted_poems_stripped 

print(highlighted_poems_stripped )

"""['Afterimages:Audre Lorde:1997', 'The Shadow:William Carlos Williams:1915', 'Ecstasy:Gabriela Mistral:1925', 'Georgia Dusk:Jean Toomer:1923', 'Parting Before Daybreak:An Qi:2014', 'The Untold Want:Walt Whitman:1871', "Mr. Grumpledump's Song:Shel Silverstein:2004", 'Angel Sound Mexico City:Carmen Boullosa:2013', 'In Love:Kamala Suraiyya:1965', 'Dream Variations:Langston Hughes:1994', 'Dreamwood:Adrienne Rich:1987']"""

#STEP 6 create a new  emply list 
highlighted_poems_details=[]

#STEP 7 lets put each poem in a list
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(":"))

"""This will give us a list of lists [['Afterimages', 'Audre Lorde', '1997'], ['The Shadow', 'William Carlos Williams', '1915'], ['Ecstasy', 'Gabriela Mistral', '1925'], ['Georgia Dusk', 'Jean Toomer', '1923'], ['Parting Before Daybreak', 'An Qi', '2014'], ['The Untold Want', 'Walt Whitman', '1871'], ["Mr. Grumpledump's Song", 'Shel Silverstein', '2004'], ['Angel Sound Mexico City', 'Carmen Boullosa', '2013'], ['In Love', 'Kamala Suraiyya', '1965'], ['Dream Variations', 'Langston Hughes', '1994'], ['Dreamwood', 'Adrienne Rich', '1987']]"""

#STEP 8 create 3 more empty lists
titles =[]
poets = []
dates = []

#STEP 9 append to each list title, poet and date of each poem

for lst in highlighted_poems_details:
  titles.append(lst[0])
  poets.append(lst[1])
  dates.append(lst[2])
  
#STEP 10, format to print a string for each poem

for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))
	
""" RESULT : 
The poem Afterimages was published by Audre Lorde in 1997
The poem The Shadow was published by William Carlos Williams in 1915
The poem Ecstasy was published by Gabriela Mistral in 1925
The poem Georgia Dusk was published by Jean Toomer in 1923
The poem Parting Before Daybreak was published by An Qi in 2014
The poem The Untold Want was published by Walt Whitman in 1871
The poem Mr. Grumpledump's Song was published by Shel Silverstein in 2004
The poem Angel Sound Mexico City was published by Carmen Boullosa in 2013
The poem In Love was published by Kamala Suraiyya in 1965
The poem Dream Variations was published by Langston Hughes in 1994
The poem Dreamwood was published by Adrienne Rich in 1987"""
