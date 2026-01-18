import random
choices = ("rock","paper","scissors")
is_playing = True

while(is_playing):
    player=None
    computer=random.choice(choices)

    player = str(input("Enter a Choice: "))
    print(f"COMPUTER : {computer}")
    print(f"PLAYER: {player}")

    if (player==computer):
        print("Draw")

    elif (player=="rock" and computer=="scissor"):
        print("You win! ! !")

    elif (player=="paper" and computer=="rock"):
        print("You win! ! !")

    elif (player=="scissor" and computer=="paper"):
        print("You win! ! !")

    else:
        print("You lose? ? ?")

    play_again=str(input("Wanna play again (y/n) :   ")).lower()
    if not play_again=="y":
        is_playing = False

print("-!-!-THANKS FOR PLAYING-!-!-")