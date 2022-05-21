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

    player_input = int(input("Enter a Number Between 1 - 9"))

    while (player_input < 1 or player_input > 9):
            player_input = int(input())
    
    player_input = holes_filled_check(board_visual, player_input)

    if player_input == False:
        pass # gotta claim tie here

    else:
        board_visual[player_input - 1] = current_player



def holes_filled_check(board_visual, player_input): # This function will check if the input of the player is already where a spot has been taken

    count = 0

    for i in board_visual:
        if i == "-":
            count = count + 1
    

    if count > 0:
        while board_visual[player_input -1] != '-':
            print("Position occupied at", player_input, "Please Enter a new")
            player_input = int(input())

            while player_input < 1 or player_input > 9:
                player_input = int(input())

    else:
        return False
    

    return player_input
    
    


        



while gaming_running:
    game_board_print(board_visual)
    player_input(board_visual)




    
    

















