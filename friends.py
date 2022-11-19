friends_names = input("Please enter names seperated by comma(,) and not spaces: ").split(',')

people_file = open('people.txt','r')
people_names = people_file.read().splitlines()
people_file.close()

friends_set = set(friends_names)
people_set = set(people_names)

nearby_set = friends_set.intersection(people_set)

nearby_write = open("nearby.txt",'w')
for i in nearby_set:
    print(f"{i} is nearby. Time to catch-up")
    nearby_write.write(f"{i}\n")

nearby_write.close()

