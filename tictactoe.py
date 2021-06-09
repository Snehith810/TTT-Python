# The board of the game.
board = ["_","_","_","_","_","_","_","_","_"]

# The required vairables.
streak = ["xxx", "ooo"]
chance = 1

# The function to display the board.
def display_Board():
    print(board[0] + "|" + board[1] + "|" + board[2] + "     " + "1|2|3")
    print(board[3] + "|" + board[4] + "|" + board[5] + "     " + "4|5|6")
    print(board[6] + "|" + board[7] + "|" + board[8] + "     " + "7|8|9")

while True:
    # The required vairables.
    available = False
    
    # The first thing is to display the board.
    display_Board()

    # Cheking if the boxes are empty.
    for i in board:
        if i == "_":
            available = True
            break

    if available is False:
        print("It's a tie.")
        break

    if chance == 1:
        move = int(input("Player one, enter your move: "))
        move -= 1
        if board[move] != "_":
            print("This move is already taken, try again!")
            continue
        else:
            board[move] = "x"
            chance += 1
    else:
        move = int(input("Player two, enter your move: "))
        move -= 1
        if board[move] != "_":
            print("This move is already taken, try again!")
            continue
        else:
            board[move] = "o"
            chance -= 1
        
    if ((board[0] + board[1] + board[2] in streak) or (board[3] + board[4] + board[5] in streak) or (board[6] + board[7] + board[8] in streak) or \
        (board[0] + board[4] + board[8] in streak) or (board[6] + board[4] + board[2] in streak) or (board[0] + board[3] + board[6] in streak) or \
            (board[1] + board[4] + board[7] in streak) or (board[2] + board[5] + board[8] in streak)):
            display_Board()
            if chance == 1:
                print("Player two wins!")
            else:
                print("Player one wins!")
            break