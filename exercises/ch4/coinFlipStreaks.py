import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinFlips = [] # List of coin flips
    # numHeads = 0
    # numTails = 0
    streak = 0

    for i in range(100): # list of 100 coin flips
        if random.randint(0, 1) == 1:
            coinFlips.append('T')
        else:
            coinFlips.append('H')

        if i == 0: # if only one element, skip comparison check
            continue

        if coinFlips[i] == coinFlips[i-1]: # If current = previous, increment streak counter
            streak += 1
        else: # if not, restart streak counter
            streak = 0

        # Code that checks if there is a streak of 6 heads or tails in a row.
        if streak == 6:
            numberOfStreaks += 1
            streak = 0

print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))