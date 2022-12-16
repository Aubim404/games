import random

def playing():
    print("*********************************")
    print("**Welcome to the Quessing Game!**")
    print("*********************************")

    secret_number = random.randrange(1,101)
    total_attempts = 0
    points = 1000

    print("Choose the level")
    print("(1) Easy (2) Medio (3) Hard")

    level = int(input("Type the level: "))

    if(level == 1):
        total_attempts = 20
    elif (level == 2):
        total_attempts = 10
    elif (level == 3):
        total_attempts = 5

    for round in range(total_attempts + 1):
        print("Round {} of {}".format(round,total_attempts))
        choice_str = input("Type a number between 1 and 100: ")
        print("Your choice is: ", choice_str)
        choice = int(choice_str)

        if(choice < 1 or round > 100 ):
            print("Inform a number between 1 and 100")
            continue

        right  = choice == secret_number
        bigger = choice > secret_number
        minor  = choice < secret_number

        if(right):
            print("You are right and gain {} points".format(points))
            break
        else: 
            if(bigger):
                print("You are wrong! Your choice is bigger than the secret number")
            elif(minor):
                print("You are wrong! Your choice is minor than the secret number")
            lost_points = abs(secret_number - choice) 
            points = points - lost_points 
    print("End of the game")

if(__name__ == "__main__"):
    playing()