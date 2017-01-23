import time


#
# Clear the terminal and put cursor at line 1
#
def clear():
	print("\x1b[2J")
	print("\x1b[1;1f")

#
# Print the hangman board and clear anything above
#
def printBoard(noose):
	clear();
	for line in noose:
		printline = ''
		for element in line:
			printline += element;
		print printline

#
# Introduce User and provide them with the rules (assume that they understand what hangman is)
#
def welcomeMessage():
	clear();
	word = raw_input('Welcome to Hangman, what would you like to the word to be? ').upper();
	print 'You will only be allowed 6 incorrect guesses to guess this word correctly'
	return word

#
# Print out the word for the board in specific format
#
def printWord(word):
	list1 = ''
	for i in word:
		list1 += ' _'
	print list1

#
# Static evaluation of board to add to the hangman for incorrect guesses
#
def addToMan(man):
	if man[2][1] != 'O':
		man[2][1] = 'O'
		return man
	elif man[2][1] == 'O' and man[3][1] != '|':
		man[3][1] = '|';
		return man
	elif man[2][1] == 'O' and man[3][1] == '|' and man[3][0] != '(':
		man[3][0] = '(';
		return man
	elif man[2][1] == 'O' and man[3][1] == '|' and man[3][0] == '(' and man[3][2] != ')':
		man[3][2] = ')';
		return man
	elif man[2][1] == 'O' and man[3][1] == '|' and man[3][0] == '(' and man[3][2] == ')' and man[4][0] != '/':
		man[4][0] = '/';
		return man
	elif man[2][1] == 'O' and man[3][1] == '|' and man[3][0] == '(' and man[3][2] == ')' and man[4][0] == '/' and man[4][2] != '\ ':
		man[4][2] = '\ ';
		man[4][3] = '';
		return man

#
# Initialize the board and collect the word to guess from user
#
def setup(noose):
	word = welcomeMessage();
	printBoard(noose);
	printWord(word);
	return word

#
# Check to see if a letter is a valid guess against the secret word
#
def checkLetter(letter, word):
	if letter in word:
		return True
	else:
		return False

#
# Prompts user to guess a letter
#
def guess_letter():
	letter = raw_input('What letter would you like to guess? ').upper()
	return letter

#
# Defines the main workflow of the game
#
def play(new_noose):
	secretWord = setup(new_noose);
	finished = False;
	guesses = []
	incorrectGuesses = []
	
	#creates printout for user of what has been guessed
	guessedWord = ' '
	for letter in secretWord:
		if letter in guesses:
			guessedWord += letter + ' ';
		else:
			guessedWord += '_ ';
	
	while finished != True:
		guess = guess_letter();
		# static check to make sure only one letter is guessed at a time
		# this will hang until it gets a digit input
		# allows for any type of character input
		if len(guess) != 1:
			print 'Each guess must be exactly 1 letter long'
			time.sleep(1)
			clear();
			printBoard(new_noose)
			print guessedWord
			guess = guess_letter();

		# maintains a list of all guesses
		if guess not in guesses:
			guesses.append(guess);
		else:
			print "You've already guessed that letter!"
			time.sleep(1)
		# maintains a formatted guessed word for print out
		# creates a string to check against the secret word
		guessedWord = ' '
		checkWord = ''
		for letter in secretWord:
			if letter in guesses:
				guessedWord += letter + ' ';
				checkWord += letter;
			else:
				guessedWord += '_ ';
				checkWord += ' ';
		# if the checked word is the same as the secret word the user has won
		if checkLetter(guess, secretWord):
			if checkWord == secretWord:
				finished = True
		# if the guess is not in the secret word then add the to hangman
		# check to see if all the incorrect guesses have been used
		elif not checkLetter(guess, secretWord) and guess not in incorrectGuesses:
			incorrectGuesses.append(guess)
			new_noose[3].append(' ' + guess);
			new_noose = addToMan(new_noose);
			if new_noose[4][3] == '':
				finished = True

		printBoard(new_noose);
		print guessedWord

	#if the game is over ask if the user wants to play again
	if finished == True:
		again(new_noose);

#
# Provides an empty board for an user
#
def newBoard():
	noose = [[' ',' ','_', '_', '_'],[' ','|', ' ', ' ',' ', '|'],[' ',' ', ' ', ' ',' ', '|', '   Incorrect Guesses:'], [' ',' ', ' ', ' ',' ', '|', '  '],[' ',' ',' ', ' ',' ', '|'],[' ',' ','_','_','_','|','_','_','_']];
	return noose

#
# Start over sequence, prompts user for choice and restarts or exits
#
def again(new_noose):

	if new_noose[4][3] == '':
		again = raw_input('You Lose! Would you live to play again? (Y/N) ').upper();
	elif new_noose[4][3] == ' ':
		again = raw_input('You win! Would you like to play again? (Y/N)').upper();
	
	if again == 'Y':
		board = newBoard();
		play(board);
	else:
		return

#
# Starts the evaluation of the script
#
if __name__ == '__main__':
	noose = [[' ',' ','_', '_', '_'],[' ','|', ' ', ' ',' ', '|'],[' ',' ', ' ', ' ',' ', '|', '   Incorrect Guesses:'], [' ',' ', ' ', ' ',' ', '|', '  '],[' ',' ',' ', ' ',' ', '|'],[' ',' ','_','_','_','|','_','_','_']];
	play(noose);