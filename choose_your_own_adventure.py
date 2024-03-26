# choose your own adventure 

playing = input("Do you want to play a game?(Type yes/no): ")

if playing.lower() != "yes":
    # use quit to terminate program if the user does not type "yes"
    quit()


name = input('Type your name: ')
print('Welcome', name, 'to this adventure')

answer = input(
    'You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?(left/right): ').lower()

if answer == 'left':
    answer = input('You come to a river, you can walk around it or swim across. Type "walk" to walk around it or "swim" to swim across i: ')

    if answer == 'swim':
        print('You swam across and were eaten by a crocodile')
   
    elif answer == 'walk':
        print('You walked for many miles, ran out of water and you lost the game')
    
    else:
        print('Not a valid option. You lose')

elif answer == 'right':
   answer = input("You've come to a bridge, it looks wobbly. Do you want to cross it or go back?(Type cross/back): ").lower()

   if answer == 'back':
       print('You try to walk back and night falls and you get eaten by a wild animal')

   if answer == 'cross':
        answer = input('You cross the bridge and meet a stranger. Do you talk to them?(Type yes/no): ').lower()

        if answer == 'yes':
            print('You talk to the stranger and they give you gold. You win!!')

        elif answer == 'no':
                print('You ignore the stranger and they are offended to death. You lose')

else:
    print('Not a valid option. You lose')

print('Thank you for playing,', name)