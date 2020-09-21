import random


def roll():
    for rolls in range(1001):
        roll_1 = random.randint(1, 7)
        roll_2 = random.randint(1, 7)
        tal = sum(roll_1, roll_2)
        d = {}
        for slag in tal:
            if slag not in d:
                d[slag] = 1
            else:
                d[slag] += 1


roll()
