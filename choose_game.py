import gallows_game
import guessing_game

def choose_game():
    print("*********************************")
    print("********Choose your Game*********")
    print("*********************************")

    print("(1) Gallows (2) Guessing")

    game = int(input("Type the number of the game: "))

    if(game == 1):
        print("Playing Gallows ")
        gallows_game.playing()
    elif(game == 2):
        print("Playing Guessing")
        guessing_game.playing()

if(__name__ == "__main__"):
    choose_game()