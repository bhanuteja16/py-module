#!/bin/python3

from random import randint

def difficulty():
    #setting board length and retry limit 
    board_size = str(input("Enter size of the board (easy,medium,hard): "))
    retry = 0
    if board_size.lower() == 'easy' or board_size.lower() == 'e' :
        board_len = randint(4,6)
        retry = 6
    elif board_size.lower() == 'medium' or board_size.lower() == 'm' :
        board_len = randint(7,10)
        retry = 10
    elif board_size.lower() == 'hard' or board_size.lower() == 'h' :
        board_len = randint(10,13)
        retry = 13
    else :
        print ("Wrong option exiting...")
        exit()
    return(board_len, retry)

def no_ship_fun() :
    #setting number of ships 
    no_ship = int(input("Enter number of ships - max 3: "))
    if no_ship not in range(1,4) :
        print ("Wrong option exiting....")
        exit()
    return no_ship

def set_board(board_len):
    #creating the board
    board = []
    for i in range(board_len) :
        board.append(["O"] * board_len)
    return board

def ship_cor(board_len) :
    #setting random ship coordinates
    x = randint(0,board_len)
    y = randint(0,board_len)
    return (x,y)

def get_cor() :
    x = int(input("Enter the row number: ")) - 1
    y = int(input("Enter the col number: ")) - 1
    return (x,y)

while True :

    def cor_check(x,y) :
        if org_board[x][y] == "O" :
            return True
        else :
            return False

    def print_board(board) :
        for i in range(len(board)) :
            print(" ".join(board[i]))

    board_len, retry = difficulty()
    no_ship = no_ship_fun()
    org_board = set_board(board_len)
    game_board = set_board(board_len)
    print ("Setting up a board of %d X %d " % (board_len, board_len))

    def found_ship(x,y) :
        # cheeck if the ship has been really found 
        if org_board[x][y] == "O" or org_board[x][y] == "X" :
            print ("There is a error")
            exit()
        else :
            sh = org_board[x][y]
            for i in range(len(org_board)) :
                for j in range(len(org_board)) :
                    if org_board[i][j] == sh :
                        game_board[i][j] = "X"
                        org_board[i][j] = "X"

    for i in range(0,no_ship) :
        while True :
            x,y = ship_cor(board_len - 1)
            j = i + 1
            print (x,y)
            try :
                if i % 2 == 0 :
                    if cor_check(x,y) and cor_check(x,y+1) == True :
                        org_board[x][y] = str(j)
                        org_board[x][y+1] = str(j)
                        break
                else :
                    if cor_check(x,y) and cor_check(x+1,y) == True :
                        org_board[x][y] = str(j)
                        org_board[x+1][y] = str(j)
                        break
            except IndexError :
                continue

    #Testing , comment this after done
    #print_board(org_board)

    # game start with retries
    while retry > 0 :
        done = True
        x,y = get_cor()
        if org_board[x][y] == "O" and game_board[x][y] == "O" :
            print ("There is nothing over there...")
            game_board[x][y] = "X"
            #retry = retry - 1
        elif game_board[x][y] == "X" :
            print ("you already tried that..")
            #retry = retry - 1
        else :
            print ("You found a ship")
            found_ship(x,y)
        for i in range(len(org_board)) :
            for j in range(len(org_board)) :
                if org_board[i][j] != "O" or org_board[i][j] != "X" :
                    done = False
                    break
        retry = retry - 1
        print_board(game_board)
        if retry == 0 or done == True :
            print ("No more retries")
            break

    replay = str(input("Do you want to paly again [y/n] :"))
    if replay.lower() == 'n' or replay.lower() == 'no' :
        break








