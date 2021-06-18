'''
Create a board
Get user input
Add input to the board
Check to see if there is a winner

'''

my_board = {'1':' ', '2':' ', '3':' ',
            '4':' ', '5':' ', '6':' ',
            '7':' ', '8':' ', '9':' '
}

def prt_board(board):
	print(board['1'],'|',board['2'],'|',board['3'],)
	print('--+---+--')
	print(board['4'],'|',board['5'],'|',board['6'],)
	print('--+---+--')
	print(board['7'],'|',board['8'],'|',board['9'],)



def game():
	turn = 'X'
	winner = False
	count = 0

	while winner == False:
		prt_board(my_board)
		move = input("Turn " + turn + ". Enter a number of a box: ")
		if my_board[move] == ' ':
			my_board[move] = turn
			count += 1

		if my_board['1'] == my_board['2'] == my_board['3'] != ' ':
			prt_board(my_board)
			print(turn, 'is the winner')
			winner = True
		elif my_board['4'] == my_board['5'] == my_board['6'] != ' ':
			prt_board(my_board)
			print(turn, 'is the winner')
			winner = True
		elif my_board['7'] == my_board['8'] == my_board['9'] != ' ':
			prt_board(my_board)
			print(turn, 'is the winner')
			winner = True
		elif my_board['1'] == my_board['4'] == my_board['7'] != ' ':
			prt_board(my_board)
			print(turn, 'is the winner')
			winner = True
		elif my_board['2'] == my_board['5'] == my_board['8'] != ' ':
			prt_board(my_board)
			print(turn, 'is the winner')
			winner = True
		elif my_board['3'] == my_board['6'] == my_board['9'] != ' ':
			prt_board(my_board)
			print(turn, 'is the winner')
			winner = True
		elif my_board['1'] == my_board['5'] == my_board['9'] != ' ':
			prt_board(my_board)
			print(turn, 'is the winner')
			winner = True
		elif my_board['3'] == my_board['5'] == my_board['7'] != ' ':
			prt_board(my_board)
			print(turn, 'is the winner')
			winner = True
		else: 
			print('Game Tie')
			winner = True

		if turn == 'X':
			turn = 'O'
		else:
			turn = 'X'

if __name__ == '__main__':
	game()