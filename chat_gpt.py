# trying out Chat GPT

import random

def guess_random_num_binary(tries, start, stop):
    target = random.randint(start, stop)
    print(f"I'm thinking of a number between {start} and {stop}. You have {tries} tries to guess it.")
    
    low = start
    high = stop
    
    for attempt in range(tries):
        guess = (low + high) // 2
        
        if guess == target:
            print(f"Congratulations! You guessed the number {target} in {attempt + 1} tries!")
            return
        
        if guess < target:
            print(f"Attempt {attempt + 1}: {guess} is too low.")
            low = guess + 1
        else:
            print(f"Attempt {attempt + 1}: {guess} is too high.")
            high = guess - 1
    
    print(f"Sorry, you did not guess the number {target} in {tries} tries. Better luck next time!")
