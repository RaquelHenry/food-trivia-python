import random

'''Task 1'''

'''
def guess_random_number(tries, start, stop):
    randomnum = random.randint(start, stop)
    while tries != 0:
        print("Number of tries left:", tries)
        guess = int(input("Guess a number between 1-10: "))
        if guess == randomnum:
            print("Success! You guessed the correct number!")
            break
        elif guess > randomnum:
            print("Guess lower!")
            tries -= 1
        elif guess < randomnum:
            print("Guess higher!")
            tries -= 1
    print("You have failed to guess the correct answer: ", randomnum)


guess_random_number(5, 0, 10)
'''

'''Task 2'''

'''
def guess_random_num_linear(tries, start, stop):
    randomnum = random.randint(start, stop)
    print("The number the computer has to guess is: ", randomnum)
    for guess in range(start, stop + 1):
        print("Number of tries left:", tries)
        print("The computer is guessing a number...", guess)
        if tries != 0:
            tries -= 1
        elif tries == 0:
            print("The computer has failed to guess the correct number.")
            break
        if guess == randomnum:
            print("Success! You guessed the correct number!")
            return guess
'''

# guess_random_num_linear(5, 0, 10)

# this was as close as I could get my code to work exactly like the example,
# the computer would still guess the number even after the guesses were out,
# so it has to be a placement issue that I am not understanding when it comes to stopping the guesses.

'''Task 3'''


def guess_random_num_binary(tries, start, stop):
    randomnum = random.randint(start, stop)
    print("Random number to find: ", randomnum)

    low = start
    high = stop

    for attempt in range(tries):
        guess = (low + high) // 2

        if guess == randomnum:
            print(
                "Found it: ", randomnum)
            return

        if guess < randomnum:
            print("Guessing Higher...")
            low = guess + 1
        else:
            print("Guessing Lower...")
            high = guess - 1

    print(
        "Your program failed to find the number.")


guess_random_num_binary(5, 0, 100)
