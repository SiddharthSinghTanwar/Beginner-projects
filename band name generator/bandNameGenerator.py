print("Welcome to the band name generator!")
print("What's the name of the city you grew up in?")
city = input()
contained = []
with open('words.txt') as f:
    for word in f:
        word = word.strip('\n')
        if word in city:
            contained.append(word)

print(contained)
print("What's your pet's name?")
pet = input()

if len(contained) == 0:
    print('running if')
    print(f"Your band name could be {city} {pet}")
else:
    for name in contained:
        #print('running else')
        print(f"Your band name could be: {name} {pet}")
