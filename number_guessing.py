import random

secret_num = random.randrange(1, 100)

guess = ""
guesses = 0
while guess != secret_num:
    guesses+=1
    try:
      guess = int(input("Make a guess: "))
    except:
        print("Please type a number")
        continue
    if guess < secret_num:
        print("Too low!")
    elif guess > secret_num:
        print("Too big!")
    elif guess == secret_num:
        print("You got it!!")

print(f"Number of guesses {guesses}")