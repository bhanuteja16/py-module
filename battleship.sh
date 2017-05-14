#!/bin/python3

from random import randint

def ship_cor(board_len):
	ship_lst = []
	ship_lst.append(randint(0,board_len))	
	ship_lst.append(randint(0,board_len))
	return ship_lst

while True :
	#setting board length
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
	
	# setting number of ships
	no_ship = int(input("Enter number of ships maximum 3 :"))
	if no_ship not in range(1,4) :
		print ("Wrong option exiting...")
		exit()

	# set the board
	board = []
	#board_row = ["O"] * board_len
	for i in range(board_len) :
		board.append(["O"] * board_len)
		#print (" ".join(board_row))
	
	# set the ships
	ship_lsts = []
	for i in range(no_ship) :
		while True :
			ship_lst = ship_cor(board_len - 1)
			overlap = False
			for x in ship_lsts :
				if x == ship_lst :
					overlap = True
			if overlap == False :
				ship_lsts.append(ship_lst)
				#print (ship_lst)
			if len(ship_lsts) <= no_ship :
				break
	print (ship_lsts)

	# game start with retries
	while retry > 0 :
		for i in range(board_len) :
			print (" ".join(board[i]))
		#print (board)
		user = []
		retry = retry - 1
		
		if len(ship_lsts) == 0 :
			break
			
		user_row = int(input("Enter the row number: ")) - 1
		user_col = int(input("Enter the col number: ")) - 1

		user.append(user_row)
		user.append(user_col)
		#print(user)
		if  user in ship_lsts :
			print ("You found a ship")
			#print (board[user_row][user_col])
			#print (ship_lsts)
			#print (user)
			ship_lsts.remove([user_row,user_col])
			#print (ship_lsts)
			board[user_row][user_col] = 'S'
			#ship_lsts.remove(user)
			#print (ship_lst)
			continue
			
		print (" Its a wrong one")
		print(board[user_row][user_col])
		print (" You have %d reties" % retry)
		print (ship_lst)
		


		board[user_row][user_col] = 'X'
	
	# Ask if user wants to play the game again 
	replay = str(input("Do you want to play again [y/n] :"))
	if replay.lower() == 'n' or replay.lower() == 'no' :
		break





				









	
	
	
