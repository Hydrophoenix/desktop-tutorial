import random
# randrange() equally does same kind of job
num = random.randint(1, 14)
print("Welcome to the Number Guessing Game, Tell us your name")
username = input()
username = username.capitalize()
print(username, "I'm thinking of a number between 1 and 14 \
can you guess. Your have 3 trys")
guessessTaken = 3
while guessessTaken > 0:
    guess = int(input("Take a guess: "))
    guessessTaken -= 1
    if guess > num:
        print("Your guess is high")
    if guess < num:
        print("Your guess is low")
    if guess == num:
        break

if guess == num:
    guessessTaken = str(guessessTaken)
    print("Great job", username, "You guessed my number with\
 just", guessessTaken, "guesses left")

if guess != num:
    num = str(num)
    print("Nope, The number was", num)
