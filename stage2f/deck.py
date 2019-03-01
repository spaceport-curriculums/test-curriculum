import random

# Provided Code for Stage 1
deck = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

def shuffle():
    ### STEP 1
    for i in range(0, 100):
        j = random.randint(0, 51)
        k = random.randint(0, 51)
        temp = deck[j]
        deck[j] = deck[k]
        deck[k] = temp

# Provided Code for Stage 1
print("Unshuffled deck: ", deck)
shuffle()
print("Shuffled deck: ", deck)

### BEGIN stage_2_starter
def deal():
    ### STEP 2
    # your code goes here
    
# Provided Code for Stage 2
players = list()
for i in range(5):
    players.append(list())
j = 0
while len(deck) != 0:
    players[j%5].append(deal())
    j += 1
for i in range(5):
    print("Hand %d:" % (i), players[i])

### SPLICE stage_3_starter

### END stage_2_starter