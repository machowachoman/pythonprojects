import os
keep_playing = True
while True:
    os.system('cls')
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
'''
    #variables
    import random
    game_choices = ["Rock" , "Paper", "Scissors"]
    player_input = input("What do you choose?\n0. Rock\n1. Paper\n2. Scissors\n\n")
    random_int = random.randint(0,2)
    cpu_choice = game_choices[random_int]
    forfeit_flag = int

    #what does the player choose?
    if player_input == "":
        forfeit_flag = 1
    elif player_input.isdigit() == False:
        forfeit_flag = 1
    else:
        player_choice = int(player_input)
        if player_choice == 0:
            print(f"\nYou chose:\n  {rock}")
        elif player_choice == 1:
            print(f"\nYou chose:\n  {paper}")
        elif player_choice == 2:
            print(f"\nYou chose:\n  {scissors}")
        else:
            forfeit_flag = 1

        #elif player_input == "":
        #print("You forfeit.\n")
        #forfeit_flag = 1

    #does player forfeit? if not, what did cpu choose?
    if forfeit_flag == 1:
        print("\nYou forfeit. Choose a valid option.")

    else:
        player_choice = int(player_input)
        if random_int == 0:
            print(f"Computer chooses:\n  {rock}")
            if random_int == player_choice:
                print("\nTie!")

            elif player_choice == 1:
                print("\nYou Win!")

            else:
                print("\nYou Lose!")

        elif random_int == 1:
            print(f"Computer chooses:\n  {paper}")
            if random_int == player_choice:
                print("\nTie!")

            elif player_choice == 0:
                print("\nYou Lose!")

            else:
                print("\nYou Win!")

        else:
            print(f"Computer chooses:\n  {scissors}")
            if random_int == player_choice:
                print("\nTie!")

            elif player_choice == 0:
                print("\nYou Win!")

            else:
                print("\nYou Lose!")


    retry = input("\nEnter 'N' to stop playing, anything else to continue testing your odds.\n").lower()
    if retry == "n":
        break

