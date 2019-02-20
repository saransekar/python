import re
import random
import sys
def get_random_word():
	Words = ['saran', 'arun', 'raja', 'kumar', 'ram']
	secure_random = random.SystemRandom()
	Word = secure_random.choice(Words)
	return Word

def replace_word(pattern,Word):
	ReplacedWord = ((re.sub(pattern, "_", Word)))
	print ReplacedWord
	return ReplacedWord

def check_letters(Limit,Word):
	GuessLetter = ''
	
	while Limit > 0:
		Guess = raw_input("Enter a Character:")

		if len(Guess) == 1:
			GuessLetter =  GuessLetter + Guess
			rex = r'[^'+str(GuessLetter)+']'
			Match = replace_word(rex,Word)

			if Match == Word:            	
				print "You Won"  
				break
			if Guess not in Word:  
				Limit -= 1         
				print "Wrong\nYou have", Limit, "Chances\nyou have entered the characters", GuessLetter,"yet"
				if Limit == 0:                     
					print "You Lost" 		
		else:
			print "Please incorrect a character input" 

def main():
	Word = get_random_word()
	Result = replace_word(r'\w',Word)
	Limit = check_letters(5,Word)
		
if __name__ == '__main__':
	 main()

