"""
Selective copying from one file to another.
"""

#Take user input from the user, to write some names separated with comma(,).
#Split the user input using comma as a separator.
friends_names = input("Please enter names seperated by comma(,) and not spaces: ").split(',')

#Open the people.txt file consisting name and use splitlines() command to seperate names in the list without \n in the output.
people_file = open('people.txt','r')
people_names = people_file.read().splitlines()
people_file.close()

#convert both list into sets.
friends_set = set(friends_names)
people_set = set(people_names)

#Intersection between two sets.
nearby_set = friends_set.intersection(people_set)

#open nearby file to copy selective data.
nearby_write = open("nearby.txt",'w')

#writting the selective in the nearby file.
for i in nearby_set:
    print(f"{i} is nearby. Time to catch-up")
    nearby_write.write(f"{i}\n")

#closing the file.
nearby_write.close()

