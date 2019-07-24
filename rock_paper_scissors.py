import random
# r_p_s compares the user and the computer values and returns the winner
def r_p_s(user,computer):
	if user == 'r':
		if computer == 'rock':
			return 'tie'
		if computer == 'paper':
			return 'lose'
		if computer == 'scissors':
			return 'win'	
	elif user == 'p':
		if computer == 'rock':
			return 'win'
		if computer == 'paper':
			return 'tie'
		if computer == 'scissors':
			return 'lose'
	elif user == 's':
		if computer == 'rock':
			return 'lose'
		if computer == 'paper':
			return 'win'
		if computer == 'scissors':
			return 'tie'
	return 'something wrong'

# Takes in r/s/p, returns rock, paper, scissors
def spellout(a_letter):
	if a_letter == 'r':
		return 'rock'
	elif a_letter == 's':
		return 'scissors'
	return 'paper'

# The computer initally wants to play the game
game = True

# Defining score for sc command
user_score = 0
computer_score = 0

# While loop to continue playing the game
while game == True: 

	# Computer starts the game
	print('Make a move! (r/s/p)')

	# Take user input as the user's move
	# If the input is not r/s/p, redo move
	rsp = False
	while rsp == False:
		user_move = input()
		if user_move == 'r' or user_move == 's' or user_move =='p':
			rsp = True
		else: 
			print('Please enter r/s/p.\nMake a move! (r/s/p)')
	# Randomize the computer's move
	possible_computer_moves = ['rock', 'paper', 'scissors']
	computer_move = random.choice(possible_computer_moves)

	# Result of the user vs comparison via function
	result = r_p_s(user_move,computer_move)
	if result == 'win':
		user_score += 1
	if result == 'lose':
		computer_score += 1
	# Print the result, change user input to word
	print('You chose ' + spellout(user_move) + ' and the computer chose ' + computer_move +'. You ' + result + '!')

	# Ask if you want to play again	
	play = True
	while play == True:
		print('Do you want to play again? (y/n)')
		play_again = input()
		
		# Allow user to type sc
		if play_again == 'sc':
			print('human: ' + str(user_score) + ', computer: ' + str(computer_score))
		
		# Continue game if y
		elif play_again == 'y':
			play = False

		# End game if n
		elif play_again == 'n':
			print('Thanks bye!')
			game = False
			play = False

		# User correction	
		else:
			print('Please enter (y/n)')

