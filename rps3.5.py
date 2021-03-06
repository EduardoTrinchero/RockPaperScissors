import random

roundlist = [1,3,5]
playerpoints = 0
computerpoints = 0

length = None
while length is None:
    try:
        length = int(input('Please choose the length of your match, type "0" for a short match, "1" for a medium match or "2" for a long match:'))
        numerodepartidas = roundlist[length]
    except:
        print('Please input a valid command.')

for i in range(numerodepartidas):
    draw = True
    while(draw):
        print(f'Round: {i+1}')
        player = int(input('Please type "0" for Rock, "1" for Paper or "2" for Scissors:'))
        computer = (random.randrange(3))
        draw = False

        if player == 0:
            print('Player chose Rock!') 
        elif player == 1:
            print('Player chose Paper!')
        elif player == 2:
            print('Player chose Scissors!')
            
        if computer == 0:
            print('The computer chose Rock!')
            if player == 0:
                draw = True
                print('Draw!')
            elif player == 1:
                playerpoints += 1
                print('You Win!')
            elif player == 2:
                computerpoints += 1
                print('You Lose!')
            
        elif computer == 1:
            print('The computer chose Paper!')
            if player == 1:
                draw = True
                print('Draw!')
            elif player == 2:
                playerpoints += 1
                print('You Win!')
            elif player == 0:
                computerpoints += 1
                print('You Lose!')        
                
        if computer == 2:
            print('The computer chose Scissors!')
            if player == 2:
                draw = True
                print('Draw!')
            elif player == 0:
                playerpoints += 1
                print('You Win!')
            elif player == 1:
                computerpoints += 1
                print('You Lose!')

if playerpoints > numerodepartidas/2.0:
            print('Congratulations, You won this match!')
elif computerpoints > numerodepartidas/2.0:
            print('Too bad! You lost the match!')
if playerpoints == computerpoints:
            print('This match is a draw.')