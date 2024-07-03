# Profession, Interests (up to 3), Hobbies (up to 3)
aspiring = []

# Profession, Interests (up to 3), Hobbies (up to 3)
executive = []

# 5 days per week, start time to end time (24-hour format)
aspireav = {}

# 5 days per week, start time to end time (24-hour format)
execav = {}




f = open("testcase.txt", "r")

# Reading aspiring professional data
for i in range(15):
    name = f.readline().strip()
    profession = f.readline().strip()
    interests = [f.readline().strip, f.readline().strip(), f.readline().strip()]
    hobbies = [f.readline().strip, f.readline().strip(), f.readline().strip()]
    timings = []
    for i in range(5):
        values = f.readline().split()
        timings.append([int(values[0]), int(values[1])])

    aspiring.append({'Name': name, 'Profession': profession, 'Interests': interests, 'Hobbies': hobbies})
    aspireav[name] = timings


# Reading executive data
for i in range(3):
    name = f.readline().strip()
    profession = f.readline().strip()
    interests = [f.readline().strip, f.readline().strip(), f.readline().strip()]
    hobbies = [f.readline().strip, f.readline().strip(), f.readline().strip()]
    timings = []
    for i in range(5):
        values = f.readline().split()
        timings.append([int(values[0]), int(values[1])])

    executive.append({'Name': name, 'Profession': profession, 'Interests': interests, 'Hobbies': hobbies})
    execav[name] = timings

chats = []

rankings = []

for ex in executive:
    rankings.append({'Name': ex['Name'], 'people': []})


for ex in executive:
    for prof in aspiring:

        # Matching score - points awarded out of 10 that determine if a professional and executive are a good match
        Mscore = 0
        if prof['Profession'] == ex['Profession']:
            Mscore+=4
        for i in range(3):
            if ex['Interests'].__contains__(prof['Interests'][i]):
                Mscore+=1
        for i in range(3):
            if ex['Hobbies'].__contains__(prof['Hobbies'][i]):
                Mscore+=1

        # Placing aspiring professional on a list of the executives coffee chat rankings (with a frequency cut off)
        for ran in rankings:
            if ran['Name'] == ex['Name']:
                new_pair = (prof['Name'], Mscore)
                ran['people'].append(new_pair)

        # Sorting the aspiring professionals by matching score
        for ran in rankings:
            if ran['Name'] == ex['Name']:
                ran['people'] = sorted(ran['people'], key=lambda x: (x[1], x[0]))
                ran['people'].reverse()

for ex in executive:
    freq = 0  # The number of meetings scheduled already (maximizes at 2)
    # Scheduling coffee chats with aspiring professionals that have the highest matching score and the same availability
    for ran in rankings:
        if ran['Name'] == ex['Name']:
            for j in ran['people']:
                aspname = j[0]
                execname = ran['Name']
                for i in range(5):
                    if aspireav[aspname][i][0] >= execav[execname][i][0] and aspireav[aspname][i][0] <= execav[execname][i][1] or aspireav[aspname][i][1] >= execav[execname][i][0] and aspireav[aspname][i][1] <= execav[execname][i][1]:
                        if freq < 2:
                            freq+=1
                            chats.append(execname + " and " + aspname)
                            break

# List out coffee chats
print("Coffee chats:")
for chat in chats:
    print(chat)