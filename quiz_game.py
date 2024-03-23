print("Welcome to my mini quiz")

playing = input("Do you want to play (yes/no) ")
# print(playing)

if playing.lower() != "yes":
    # use quit to terminate program if the user does not type "yes"
    quit()

print("Okay! Let's play :)")

# keep track of the players' correct answers
score = 0

# Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect Answer!")

# Question 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect Answer!")

# Question 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect Answer!")

# Question 4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect Answer!")

# you have to turn score into a str because you can only concatenate strings to string
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + " %")