import random

print('Number by Tom Adametx')
print('You have 100 points by guessing numbers from 1 to 5, you\n\
can gain or lose points depending upon how close you get to\n\
a random number selected by the computer.\n')

print('You occasionaly will get jackpot wich will double your points.\n\
You will win when you get 500 points.')

print('Ctrl + C to stop program.\n')

points = 100

while True:
    number = random.randint(1, 5)
    print('Guess the number form 1 to 5: ', end='')
    try:
        guess = int(input())
    except ValueError:
        print('Please enter an integer!')
        continue
    except KeyboardInterrupt:
        break
 
    if guess == number:
        points = points + points
        print('YOU HIT THE JACKPOT!')
    elif guess > 5 or guess < 1:
        print('You entered a number out of scope!')
        continue
    elif abs(number - guess) == 4:
        points = int(points - (points * 0.5))
    elif abs(number - guess) == 3:
        points = points - 5
    elif abs(number - guess) == 2:
        points = points + 1
    elif abs(number - guess) == 1:
        points = points + 5

    print('You have ' + str(points) + ' points.')

    if points >= 500:
        print('You win! with ' + str(points) + '.')
        break
    elif points <= 0:
        print('You lose!')
        break
