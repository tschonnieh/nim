from q_learning.Trainer import Trainer

import re

print('========================================================')
print('============== Q-Learning Trainer for Nim ==============')
print('Please enter the size of the board')
print('Eg. 5, 4, 3')
print('')

while True:
    inStr = input()
    inStr = re.split(' |,', inStr)
    pearlsPerRow = [int(d) for d in inStr if d.isdigit()]

    if len(pearlsPerRow) > 0:
        break

if sum(pearlsPerRow) > 12:
    print('========================================================')
    print('======================= Warning ========================')
    print('Big game sizes need a lot of memory and time to train')
    print('c: Continue, q: Abort and Exit')
    while True:
        c = input()
        c = c.lower()
        if c == 'c':
            break
        elif c == 'q':
            sys.exit(0)

print('========================================================')
print('Starting training for:')
print(pearlsPerRow)
print('This could take some time')
print('========================================================')

tr = Trainer(pearlsPerRow)

tr.startTraining()

tr.save()
tr.showPlots()
