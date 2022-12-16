import random

def opening_message():
    print("*********************************")
    print("**Welcome to the Gallows Game!!**")
    print("*********************************")

def format_secret_word():
    file = open("words.txt", "r")
    words = []
    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0,len(words))
    secret_word = words[number].lower()
    return secret_word
    
def playing():
    opening_message()
    secret_word = format_secret_word()
    
    right_letter = ["_" for letter in secret_word] #Initializes right letter

    hung = False
    hit = False
    wrong = 0 

    print(right_letter)

    while(not hung and not hit):

        choice_str = input("Type a letter: ")
        choice_str = choice_str.strip().lower()

        if choice_str in secret_word:
            index = 0
            for letter in secret_word:
                if (choice_str == letter):
                    right_letter[index] = letter
                index += 1
        else:
            wrong += 1
            drawing(wrong)

        hung = wrong == 7
        hit = "_" not in right_letter
        print(right_letter)

    if (hit):
        print("Congratulations, you win!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("You've been hanged !")
        print("A palavra era {}".format(secret_word))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        print("End of the game")

def drawing(wrong):
        print("  _______     ")
        print(" |/      |    ")

        if(wrong == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if(wrong == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if(wrong == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if(wrong == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if(wrong == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if(wrong == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (wrong == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

if(__name__ == "__main__"):
    playing()