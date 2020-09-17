i = 18
print('Welcome to the game of guessing a number')
print('You have total 9 guesses')

x = int(input("Guess the number:"))
print('No. of Guesses left:',8)

for n in range(0, 8):


    if x > i:

        x = int(input("Guess a smaller number:"))
        if x == i:
            print('Correct Number!!!')
            print('You took', 9 - (7 - n), 'guesses')
            break
        elif 7 - n != 0:
            print('No. of guesses left:', 7 - n)
        else:
            print('Game Over!')

    elif x < i:

        x = int(input("Guess a greater number:"))

        if x == i:
            print('Correct Number!!!')
            print('You took', 9 - (7 - n), 'guesses')
            break
        elif 7 - n != 0:
            print('No. of guesses left:', 7 - n)
        else:
            print('Game Over!')