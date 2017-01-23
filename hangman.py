import time

def clear():
	print("\x1b[2J")
	print("\x1b[1;1f")

def printBoard(noose):
	clear();
	for line in noose:
		printline = ''
		for element in line:
			printline += element;
		print printline

def welcomeMessage():
	clear();
	word = raw_input('Welcome to Hangman, what would you like to the word to be? ').upper();
	print 'You will only be allowed 6 incorrect guesses to guess this word correctly'
	return word

def printWord(word):
	list1 = ''
	for i in word:
		list1 += ' _'
	print list1

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

def setup(noose):
	word = welcomeMessage();
	printBoard(noose);
	printWord(word);
	return word

def checkLetter(letter, word):
	if letter in word:
		return True
	else:
		return False

def guess_letter():
	letter = raw_input('What letter would you like to guess? ').upper()
	return letter

def play(new_noose):
	secretWord = setup(new_noose);
	finished = False;
	guesses = []
	incorrectGuesses = []
	
	guessedWord = ' '
	for letter in secretWord:
		if letter in guesses:
			guessedWord += letter + ' ';
		else:
			guessedWord += '_ ';
	
	while finished != True:
		guess = guess_letter();
		
		if len(guess) != 1:
			print 'Each guess must be exactly 1 letter long'
			time.sleep(1)
			clear();
			printBoard(new_noose)
			print guessedWord
			guess = guess_letter();

		if guess not in guesses:
			guesses.append(guess);
		else:
			print "You've already guessed that letter!"
			time.sleep(1)
		guessedWord = ' '
		checkWord = ''
		for letter in secretWord:
			if letter in guesses:
				guessedWord += letter + ' ';
				checkWord += letter;
			else:
				guessedWord += '_ ';
				checkWord += ' ';
		if checkLetter(guess, secretWord):
			if checkWord == secretWord:
				finished = True

		elif not checkLetter(guess, secretWord) and guess not in incorrectGuesses:
			incorrectGuesses.append(guess)
			new_noose[3].append(' ' + guess);
			new_noose = addToMan(new_noose);
			if new_noose[4][3] == '':
				finished = True

		printBoard(new_noose);
		print guessedWord

	if finished == True:
		again(new_noose);

def newBoard():
	noose = [[' ',' ','_', '_', '_'],[' ','|', ' ', ' ',' ', '|'],[' ',' ', ' ', ' ',' ', '|', '   Incorrect Guesses:'], [' ',' ', ' ', ' ',' ', '|', '  '],[' ',' ',' ', ' ',' ', '|'],[' ',' ','_','_','_','|','_','_','_']];
	return noose

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

if __name__ == '__main__':
	noose = [[' ',' ','_', '_', '_'],[' ','|', ' ', ' ',' ', '|'],[' ',' ', ' ', ' ',' ', '|', '   Incorrect Guesses:'], [' ',' ', ' ', ' ',' ', '|', '  '],[' ',' ',' ', ' ',' ', '|'],[' ',' ','_','_','_','|','_','_','_']];
	play(noose);