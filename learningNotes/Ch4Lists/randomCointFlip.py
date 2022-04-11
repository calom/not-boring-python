import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    random_toss_list = []
    for toss in range(100):
        if random.randint(0,1) == 0:
            random_toss_list.append('H')
        else:
            random_toss_list.append('T')

 # Code that checks if there is a streak of 6 heads or tails in a row.
    same_toss = []
    for toss in random_toss_list:
        if len(same_toss) == 0:
            same_toss.append(toss)
            continue
        if toss == same_toss[0]:
            same_toss.append(toss)
        else:
            same_toss = [toss]
        if len(same_toss) >= 6:
            numberOfStreaks += 1
            break
print('Chance of streak: %s%%' % (numberOfStreaks / 100))