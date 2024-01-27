import random
Guessing = random.randint(1, 20)

k = 0

print("Hello! What is your name?")
name = str(input())
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")
chislo = 0

while chislo != Guessing:
    chislo = int(input())
    if chislo < Guessing:
        print("Your guess is to low.\nTake a guess.")
        k += 1
    if chislo > Guessing:
        print("Your guess is to high.\nTake a guess.")
        k += 1
        
print(f"Good job, {name}! You guessed my number in {k} guesses!")


