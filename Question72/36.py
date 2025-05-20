import random

listRandom = []

for i in range(15):
    value = random.randint(1, 20)  # Generates number between 1 and 20 inclusive
    listRandom.append(value)

print(listRandom)
