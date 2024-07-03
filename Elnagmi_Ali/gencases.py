# Generation of 15 random aspiring professionals, and 3 random executives
# Properties and availability will be randomized, names are to be assumed as unique
# Check README for file save formatting explanation

import random

# File writer
open('testcase.txt', 'w').close()
f = open("testcase.txt", "a")

names = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
    "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph",
    "Jessica", "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy",
    "Daniel", "Lisa", "Matthew", "Ahmed", "Musa", "Betty", "Donald", "Sandra",
    "Mark", "Ashley", "Paul", "Dorothy", "Steven", "Kimberly", "Andrew", "Emily",
    "Kenneth", "Donna", "Joshua", "Michelle", "Kevin", "Carol", "Brian", "Amanda",
    "George", "Melissa", "Edward", "Ali", "Ronald", "Stephanie", "Timothy",
    "Rebecca", "Jason", "Sharon", "Jeffrey", "Laura", "Ryan", "Cynthia", "Jacob",
    "Mustafa", "Gary", "Amy", "Nicholas", "Angela", "Eric", "Arwa", "Jonathan",
    "Anna", "Stephen", "Brenda", "Larry", "Pamela", "Justin", "Nicole", "Scott",
    "Emma", "Brandon", "Helen",
]

professions = [
    "Computer Engineer",
    "IOS Developer",
    "Data Scientist",
    "Web Developer",
]

interests = [
    "Artificial Intelligence",
    "Machine Learning",
    "Data Structures",
    "Algorithms",
    "Computer Networks",
    "Operating Systems",
    "Databases",
    "Cyber Security",
]

hobbies = [
    "Reading",
    "Cooking",
    "Gardening",
    "Painting",
    "Photography",
    "Traveling",
    "Hiking",
    "Cycling",
]

# Creating boolean array to assure unique names
taken = []
for i in range(80):
    taken.append(False)

def persongen():
    # Generate name
    rand = random.randint(0, 79)
    if taken[rand]:
        while taken[rand]:
            rand = random.randint(0, 79)
    f.write(names[rand])
    f.write("\n")
    taken[rand] = True

    # Generate profession
    rand = random.randint(0, 3)
    f.write(professions[rand])
    f.write("\n")


    # Generate interests
    takenn = []
    for i in range(8):
        takenn.append(False)
    for i in range(3):
        rand = random.randint(0, 7)
        if takenn[rand]:
            while takenn[rand]:
                rand = random.randint(0, 7)
        takenn[rand] = True
        f.write(interests[rand])
        f.write("\n")

    # Generate hobbies
    takenn = []
    for i in range(8):
        takenn.append(False)
    for i in range(3):
        rand = random.randint(0, 7)
        if takenn[rand]:
            while takenn[rand]:
                rand = random.randint(0, 7)
        takenn[rand] = True
        f.write(hobbies[rand])
        f.write("\n")

    # Generate schedules
    for i in range(5):
        start = random.randint(7, 10) # starting time 7AM to 10AM
        end = random.randint(start + 1, 18) # ending time (start time + 1) to 6PM
        f.write(start.__str__() + " " + end.__str__())
        f.write('\n')


# Generating 15 different aspiring professionals and saving to testcase.txt file
for i in range(15):
    persongen()

# Generating 3 different executives
for i in range(3):
    persongen()

f.close()