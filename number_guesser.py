# getting a random number
import random 

# print(random.randrange(-5, 11))
# print(random.randint(-5, 11))

print("Welcome to the number guessing game")

playing = input("Do you want to play?(yes/no) ")

if playing.lower() != "yes":
    quit()

print("Okay, lets begin!")

top_of_range = input("Type a random number: ")


if top_of_range.isdigit():
    # use int() method to convert the input into a number
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number greater than zero")
        quit()

else:
    print("Please type a number next time")
    quit()


random_number = random.randint(0, top_of_range)
# print(random_number)

# Keep track of the guesses 
guesses = 0

while True:
    # increment the guesses every time the loop comes back to the top after keyword 'break'
    guesses += 1

    user_guess = input("Make a guess of the random number generated: ")
    if user_guess.isdigit():
    # use int() method to convert the input into a number
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("Congratulations! You got it right!")
        break
    elif user_guess > random_number:
        print("You were above the number")
   
    else:
        print("You were below the number")


print("You got it in ", guesses, "guesses")