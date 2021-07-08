#Two Player Tic-Tac-Toe game in Python 3.9.

''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.). '''

gboard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

game_keys = []

for key in gboard:
    game_keys.append(key)

'''  print the updated board after every move in the game. '''

def printgame(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

         # it is the main function.
def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printgame(gboard)
        print("It's your turn," + turn + ".where to move?")

        move = input()        

        if gboard[move] == ' ':
            gboard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nwhere to move?")
            continue

        #  check if player X or O has won,for every move after 5 moves. 
        
        if count >= 5:
            if gboard['7'] == gboard['8'] == gboard['9'] != ' ': # across the top
                printgame(gboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif gboard['4'] == gboard['5'] == gboard['6'] != ' ': # across the middle
                printgame(gboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif gboard['1'] == gboard['2'] == gboard['3'] != ' ': # across the bottom
                printgame(gboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif gboard['1'] == gboard['4'] == gboard['7'] != ' ': # down the left side
                printgame(gboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif gboard['2'] == gboard['5'] == gboard['8'] != ' ': # down the middle
                printgame(gboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif gboard['3'] == gboard['6'] == gboard['9'] != ' ': # down the right side
                printgame(gboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif gboard['7'] == gboard['5'] == gboard['3'] != ' ': # diagonal
                printgame(gboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif gboard['1'] == gboard['5'] == gboard['9'] != ' ': # diagonal
                printgame(gboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("Game Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in game_keys:
            gboard[key] = " "

        game()

if __name__ == "__main__":
    game()