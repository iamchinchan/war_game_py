def wanna_play_again():
    print(f"Do you want to play the game again? ")
    while True:
        try:
            val = input("Type y/Y for Yes and type n/N for No: ")
            if val.lower() in ("y", "n"):
                return val.lower() == "y"
            else:
                print(f"please enter a correct choice\n")
        except:
            print(f"Please try Again with a valid input\n")
