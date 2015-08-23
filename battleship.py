#This allows randomization of an integer
from random import randint

#This prints the board
def print_board(board):
    for row in board:
        print " ".join(row)

#This places the battleship on the map
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#This verifies that a valid number was entered
def number_check(x, y):
	number_check_loop = True
	while number_check_loop == True:
		try:
			x = int(raw_input(y))
			number_check_loop = False
			global z
			z = x
		except ValueError:
			print "\nUnrecognized input, try again."
		
#Program start
board = []
turn = 0
	
for x in range(5):
	board.append(["O"] * 5)

print "\nLet's play Battleship!\n"
print_board(board)
ship_row = random_row(board)
ship_col = random_col(board)
	
for turn in range(4):
	print "\nTurn", turn + 1
	guess_row = 0
	guess_col = 0
	number_check(guess_row, "\nGuess Row:\n> ")
	guess_row = z
	number_check(guess_col, "\nGuess Column:\n> ")
	guess_col = z
	if guess_row == ship_row and guess_col == ship_col:
		print "\nCongratulations! You sunk my battleship!\n"
		break
	else:
		if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
			print "\nOops, that's not even in the ocean.\n"
		elif(board[guess_row][guess_col] == "X"):
			print "\nYou guessed that one already.\n"
		else:
			print "\nYou missed my battleship!\n"
			board[guess_row][guess_col] = "X"
	print_board(board)
	if turn == 3:
		print "\nGame Over\n"
		break
