input = [n.rstrip('\n') for n in open("02_input.txt")]

rock, paper, scissors = ['A', 'X'], ['B', 'Y'], ['C', 'Z']
wins, points = ['C X', 'A Y', 'B Z'], {'X':1, 'Y':2, 'Z':3}

score1 = 0
score2 = 0
for x in input:
    x1, x2 = x.split(' ')
    play1 = [x1, x2]

    score1 += points[x2]
    if x in wins:
        score1 += 6
    elif play1 in [rock, paper, scissors]:
        score1 += 3

    if x2 == 'X':
        if x1 == 'A':
            score2 += points['Z']
        elif x1 == 'B':
            score2 += points['X']
        else:
            score2 += points['Y']
    elif x2 == 'Y':
        score2 += 3
        if x1 == 'A':
            score2 += points['X']
        elif x1 == 'B':
            score2 += points['Y']
        else:
            score2 += points['Z'] 
    else:
        score2 += 6
        if x1 == 'A':
            score2 += points['Y']
        elif x1 == 'B':
            score2 += points['Z']
        else:
            score2 += points['X']

print(score1)
print(score2)