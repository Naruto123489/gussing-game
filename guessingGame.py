import random
i=0
number=(random.randrange(1,9))
guess=int(input("Guess your number between 1-9:    "))
while i < 5:
    i += 1
    if (guess > number) :
        guess= int(input("Your guess is too high: Guess a lower number: "))
        continue
    elif (guess < number) :
        guess= int(input("Your guess is too low: Guess a higher number: "))
        continue
    else:
        print("Congratulations, You won!!")
    break
if (i==5):
    print("\n Game over, you lost! Correct number is :", number)
    print("\n")