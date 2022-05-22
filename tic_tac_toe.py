'''
Making a tic-tac-toe game with python. 

Features and plans to add:

1. Create a game board that can be visually displayed in the console 

2. Take in player inputs from player a and b

3. Display input on game board

4. Create functions that will check for winners, losers or possible ties

5. Switch player

6. Check if the player won or lost or tie from his side

5. If no result occurs, continue playing or else announce winner or announce its a tie

6. Ask if they want to play again

'''

board_visual =  ["-", "-", "-",
                 "-", "-", "-",
                 "-","-","-",]


current_player = "X"

winner = None

gaming_running = True



def game_board_print(board_visual):
    print(board_visual[0] + " | " + board_visual[1] + " | " + board_visual[2])
    print()
    print(board_visual[3] + " | " + board_visual[4] + " | " + board_visual[5])
    print()
    print(board_visual[6] + " | " + board_visual[7] + " | " + board_visual[8])




def player_input(board_visual):

    player_input = int(input("Enter a Number Between 1 - 9  "))

    while (player_input < 1 or player_input > 9):

            print("Please Enter a Number Between 1 - 9")

            player_input = int(input())
    
    player_input = holes_filled_check(board_visual, player_input)

    if player_input == False:

        global gaming_running

        game_board_print(board_visual)

        print("Its a tie")

        gaming_running = False

    else:
        board_visual[player_input - 1] = current_player



def holes_filled_check(board_visual, player_input): # This function will check if the input of the player is already where a spot has been taken

        while board_visual[player_input -1] != '-':
            print("Position occupied at", player_input, "Please Enter a New Input Between 1 - 9")
            player_input = int(input())

            while player_input < 1 or player_input > 9:
                print("Input still not correct. Please enter input between 1 - 9")
                player_input = int(input())

        return player_input




def check_horizontal(board_visual):

    global winner 

    if board_visual[0]  == board_visual[1] == board_visual[2] and board_visual[0] != '-':
        winner = board_visual[0]
        return True
    
    elif board_visual[3]  == board_visual[4] == board_visual[5] and board_visual[3] != '-':
        winner = board_visual[3]
        return True
    
    elif board_visual[6]  == board_visual[7] == board_visual[8] and board_visual[6] != '-':
        winner = board_visual[6]
        return True



def check_row(board_visual):

    global winner

    if board_visual[0]  == board_visual[3] == board_visual[6] and board_visual[0] != '-':
        winner = board_visual[0]
        return True
    
    elif board_visual[1]  == board_visual[4] == board_visual[7] and board_visual[1] != '-':
        winner = board_visual[3]
        return True
    
    elif board_visual[2]  == board_visual[5] == board_visual[8] and board_visual[2] != '-':
        winner = board_visual[6]
        return True



def check_diagonal(board_visual):

    global winner

    if board_visual[0] == board_visual[4] == board_visual[8] and board_visual[0] != '-':
        winner = board_visual[0]
        return True
    
    elif board_visual[2] == board_visual[4] == board_visual[6] and board_visual[2] != '-':
        winner = board_visual[2]
        return True



def check_win():

    global gaming_running

    global board_visual

    if check_diagonal(board_visual) == True or check_horizontal(board_visual) == True or check_row(board_visual) == True:
        print("game over, we have a winner who is!", winner)
        print()

        game_board_print(board_visual)

        gaming_running = False

    

    if gaming_running == False:
            
        game_choice = input("Do you want to play. Enter Y to play else any key to quit")

        if game_choice == 'Y' or game_choice == 'y':
            gaming_running = True
            board_visual =  ["-", "-", "-",
                 "-", "-", "-",
                 "-","-","-",]
            run_game()
        
        else:
            print("Thank you for playing. Bye")
            exit(0)


def tie_checker():

    global gaming_running

    global board_visual

    if "-" not in board_visual:
        print("It's a tie. Game over")
        
        gaming_running = False


    if gaming_running == False:

        game_choice = input("Do you want to play. Enter Y to play else any key to quit")

        if game_choice == 'Y' or game_choice == 'y':
            gaming_running = True

            board_visual =  ["-", "-", "-",
                 "-", "-", "-",
                 "-","-","-",]

            run_game()
        
        else:
            print("Thank you for playing. Bye")
            exit(0)
            


def switch_player():
    global current_player

    if current_player == 'X':
        current_player = "O"
    
    else:
        current_player = "X"




def run_game():
    global gaming_running

    while gaming_running:
        game_board_print(board_visual)
        player_input(board_visual)
        check_win()
        tie_checker()
        switch_player()


run_game()





    
    

















